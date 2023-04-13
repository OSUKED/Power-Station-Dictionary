import json
import uuid
import pathlib
from typing import Optional
import datetime
from enum import Enum
from sqlmodel import Field, SQLModel, Session, Relationship, create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session
import sys, inspect
from pydantic import parse_obj_as

from powerdict import schemas


## DB Tables
class DataLicenseTable(schemas.DataLicense, table=True):
    __tablename__ = 'fd__data_license'
    path: Optional[str]
    data_license_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    data_resource_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_resource.data_resource_id')
    data_package_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_package.data_package_id')
    data_resource: Optional['DataResourceTable'] = Relationship(back_populates='licenses')
    data_package: Optional['DataPackageTable'] = Relationship(back_populates='licenses')


class DataContributorTable(schemas.DataContributor, table=True):
    __tablename__ = 'fd__data_contributor'
    path: Optional[str]
    data_contributor_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    data_package_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_package.data_package_id')
    data_package: Optional['DataPackageTable'] = Relationship(back_populates='contributors')


class DataSourceTable(schemas.DataSource, table=True):
    __tablename__ = 'fd__data_source'
    path: Optional[str]
    data_source_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    data_resource_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_resource.data_resource_id')
    data_package_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_package.data_package_id')
    data_resource: Optional['DataResourceTable'] = Relationship(back_populates='sources')
    data_package: Optional['DataPackageTable'] = Relationship(back_populates='sources')
    

class FieldDescriptorTable(schemas.FieldDescriptor, table=True):
    __tablename__ = 'fd__field_descriptor'
    rdfType: Optional[str]
    description: Optional[str]
    example: Optional[str]
    constraints: Optional[str]
    field_descriptor_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    data_schema_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_schema.data_schema_id')
    data_schema: Optional['DataSchemaTable'] = Relationship(back_populates='fields')

    
class DataSchemaTable(schemas.DataSchemaBase, table=True):
    __tablename__ = 'fd__data_schema'
    data_schema_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    fields: Optional[list[FieldDescriptorTable]] = Relationship()


class DataResourceTable(schemas.DataResourceBase, table=True):
    __tablename__ = 'fd__data_resource'
    data: Optional[str]
    path: Optional[str]
    data_resource_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    data_package_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_package.data_package_id')
    data_schema_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_schema.data_schema_id')
    fd_schema: Optional[DataSchemaTable] = Relationship()
    sources: Optional[list[DataSourceTable]] = Relationship()
    licenses: Optional[list[DataLicenseTable]] = Relationship()


class DataPackageTable(schemas.DataPackageBase, table=True):
    __tablename__ = 'fd__data_package'
    id: Optional[str]
    homepage: Optional[str]
    image: Optional[str]
    data_package_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    resources: Optional[list[DataResourceTable]] = Relationship()
    licenses: Optional[list[DataLicenseTable]] = Relationship()
    sources: Optional[list[DataSourceTable]] = Relationship()
    contributors: Optional[list[DataContributorTable]] = Relationship()


class SecureAPIUserTable(schemas.SecureAPIUser, table=True):
    __tablename__ = 'api__secure_user'
    username: str = Field(primary_key=True, default='anonymous')
    id: Optional[str]


class TokenRecordTable(schemas.ExtendedSQLModel, table=True):
    __tablename__ = 'api__tokens'
    token: str = Field(primary_key=True)
    username: str = Field(default="anonymous")
    expires: datetime.datetime = Field(
        primary_key=True,
        default=datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
    )


# Creating a helper mapping from the table name to the SQLModel class
is_class_member = lambda member: inspect.isclass(member) and member.__module__ == __name__
cls_members = inspect.getmembers(sys.modules[__name__], is_class_member)

table_name_to_schema = {
    cls_member[-1].__tablename__: cls_member[-1]
    for cls_member
    in cls_members
    if hasattr(cls_member[-1], '__tablename__')
}


## DB client
def filter_db_record_attrs(
    db_class: schemas.ExtendedSQLModel,
    public_only: bool = True,
    table_only: bool = True
):
    attr_names = []
    
    for attr_name in dir(db_class):
        # filtering for public attributes if specified
        is_public = attr_name[0] != '_'
        
        if (is_public == False) & public_only:
            continue
            
        # extracting the attribute value
        attr_value = getattr(db_class, attr_name)
        
        # identifying the attribute type (only allowing one type for lists of objects)
        if isinstance(attr_value, list):
            attr_types = {type(attr_item_value) for attr_item_value in attr_value}
            
            if len(attr_types) == 0:
                continue
            
            assert len(attr_types) == 1, f'Attributes which are lists should contain items of the same type, found multiple types for {attr_name}'
            attr_type = list(attr_types)[0]
        else:
            attr_type = type(attr_value)
        
        # filtering for table attributes if specified
        is_table = issubclass(attr_type, schemas.ExtendedSQLModel)
        
        if (is_table == False) & table_only:
            continue
        
        # adding attributes that pass the checks
        attr_names += [attr_name]
            
    return attr_names

def jsonise_attr_value(attr_value):
    json_obj_types = [
        dict,
        list,
        str,
        int,
        float,
        bool,
        type(None)
    ]
    
    str_types = [
        uuid.UUID,
        pathlib.PosixPath
    ]
    
    if type(attr_value) in json_obj_types:
        return attr_value
    elif issubclass(type(attr_value), Enum):
        return attr_value.value
    elif type(attr_value) in str_types:
        return str(attr_value)
    else:
        raise ValueError(f'{attr_value} of type `{type(attr_value)}` could not be converted into a JSON friendly format')

def db_record_to_dict_repr(
    db_record: schemas.ExtendedSQLModel,
    parent_name: Optional[str] = None,
    grandparent_name: Optional[str] = None
) -> dict:
    dict_repr = {
        k: jsonise_attr_value(v)
        for k, v
        in db_record.dict().items()
        if v is not None
    }
    
    for attr_name in filter_db_record_attrs(db_record):
        if (attr_name == parent_name) | (attr_name == grandparent_name):
            continue
        
        attr_value = getattr(db_record, attr_name)

        if isinstance(attr_value, list):
            dict_repr[attr_name] = [db_record_to_dict_repr(attr_item, attr_name, parent_name) for attr_item in attr_value]
        else:
            dict_repr[attr_name] = db_record_to_dict_repr(attr_value, attr_name, parent_name)

    return dict_repr


def select_schema(
    schema_class: schemas.ExtendedSQLModel,
    use_table_schema: bool = False
):
    if use_table_schema:
        if schema_class.__name__[-5:] != 'Table':
            schema_class = getattr(locals(), schema_class.__name__ + 'Table')
        return schema_class

    return getattr(schemas, schema_class.__name__.replace('Table', ''))


class DbClient:
    def __init__(
        self,
        user: Optional[str] = 'postgres',
        password: Optional[str] = None,
        host: Optional[str] = 'localhost',
        port: Optional[int] = 5632,
        database_name: str = 'analytics',
        dialect: str = 'postgresql',
        driver: Optional[str] = 'psycopg2'
    ):
        if driver is not None:
            driver = '+' + driver
        else:
            driver = ''
            
        if (
            (user is not None) and
            (password is not None) and
            (host is not None) and
            (port is not None)
        ):
            remote_db_str = f'{user}:{password}@{host}:{port}'
        else:
            remote_db_str = ''
            
        connect_str = f'{dialect}{driver}://{remote_db_str}/{database_name}'
        self._engine = create_engine(connect_str, pool_pre_ping=True)
        
    def create_tables(
        self,
        tables_to_create: Optional[list] = [
            DataLicenseTable.__table__,
            DataContributorTable.__table__,
            DataSourceTable.__table__,
            FieldDescriptorTable.__table__,
            DataSchemaTable.__table__,
            DataResourceTable.__table__,
            DataPackageTable.__table__
        ]
    ):
        SQLModel.metadata.create_all(self._engine, tables=tables_to_create)

    def run_query(
        self,
        query_str: str
    ):
        with Session(self._engine) as session:
            results = session.execute(text(query_str))
        
        return results

    def create_record(
        self,
        record: dict,
        tablename: str
    ): 
        schema = table_name_to_schema[tablename]
        
        if isinstance(record, dict):
            record = schema(**record)

        with Session(self._engine) as session:
            schema.create_record(session, record)
        
        return record

    def get_record(
        self,
        record_id: str,
        table_name: str
    ):
        schema = table_name_to_schema[table_name]

        with Session(self._engine) as session:
            record = schema.get_record(session, record_id)

        return record

    def get_all(
        self,
        table_name: str,
        return_dicts: bool = True
    ):
        schema = table_name_to_schema[table_name]
        
        with Session(self._engine) as session:
            obj = schema.get_all_records(session)

            if return_dicts:
                # need a way to load any nested sqlmodel attrs
                base_schema = select_schema(schema, use_table_schema=False)
                return [schemas.sqlmodel_obj_to_dict(parse_obj_as(base_schema, elem)) for elem in obj]

        return obj
    
    def create_multi_table_records(
        self,
        db_records: dict[str, list]
    ):
        with Session(self._engine) as session:
            for table_name, table_records in db_records.items():
                table_schema = table_name_to_schema[table_name]

                for table_record in table_records:
                    if isinstance(table_record, SQLModel) or isinstance(table_record, dict):
                        record_obj = table_schema.parse_obj(table_record)
                    else:
                        raise ValueError(f"The input type {type(table_record)} can not be processed for table: {table_name}")

                    session.add(record_obj)

            session.commit()

    def get_data_package(
        self, 
        data_package_id: str,
        return_type: schemas.DataPackageReturnType = 'data_package'
    ):
        with Session(self._engine) as session:
            data_package = DataPackageTable.get_record(session, data_package_id)

            data_package.licenses
            data_package.resources
            data_package.contributors
            data_package.sources
            [resource.fd_schema for resource in data_package.resources]
            [resource.fd_schema.fields for resource in data_package.resources]

            if return_type == schemas.DataPackageReturnType.data_package:
                return data_package
            elif return_type == schemas.DataPackageReturnType.dictionary:
                return db_record_to_dict_repr(data_package)
            elif return_type == schemas.DataPackageReturnType.raw_dict:
                return json.loads(data_package.json(exclude_none=True))
            else:
                return None

    def get_all_data_packages(
        self,
        return_type: schemas.DataPackageReturnType = 'data_package'
    ):
        with Session(self._engine) as session:
            records = DataPackageTable.get_all_records(session)

            return [
                self.get_data_package(record.data_package_id, return_type)
                for record
                in records
            ]

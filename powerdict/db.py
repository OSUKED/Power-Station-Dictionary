import uuid
import datetime
import pathlib
import pandas as pd
from typing import Any, Union, Optional

from enum import Enum
from pydantic import AnyHttpUrl, EmailStr, validator, constr, parse_obj_as
from sqlmodel import Field, SQLModel, Session, Relationship, create_engine, select
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from sqlalchemy.future import select
import sys, inspect


## SQLModel Schema Base
class ExtendedSQLModel(SQLModel):
    @classmethod
    def get_record(
        cls, 
        session: Session, 
        id_: Any
    ):
        obj = session.get(cls, id_)
        if obj is None:
            raise NoResultFound(f"{cls.__name__} with id {id_} not found")
        return obj

    @classmethod
    def get_all_records(cls, session: Session):
        res = session.execute(select(cls))
        return res.scalars().all()

    @classmethod
    def create_record(
        cls, session: Session, source: Union[dict[Any, Any], SQLModel]
    ):
        if isinstance(source, SQLModel) or isinstance(source, dict):
            obj = cls.parse_obj(source)
        else:
            raise ValueError(f"The input type {type(source)} can not be processed")

        session.add(obj)
        session.flush()

        return obj
    
    
## Enumerations
class DataContributorRole(str, Enum):
    author = 'author'
    publisher = 'publisher'
    maintainer = 'maintainer'
    wrangler = 'wrangler'
    contributor = 'contributor'


class DataPackageProfile(str, Enum):
    tabular_data_package = 'tabular-data-package'


class DataResourceProfile(str, Enum):
    tabular_data_resource = 'tabular-data-resource'
    data_resource = 'data-resource'


class DataResourceFormat(str, Enum):
    csv = 'csv'
    xls = 'xls'
    json = 'json'
    zip = 'zip'


## Frictionless Schemas
class DataLicense(ExtendedSQLModel):
    name: Optional[str]
    path: Optional[Union[pathlib.Path, AnyHttpUrl]]
    title: Optional[str]

    @validator('path')
    def check_name_or_path(cls, v, values):
        if v is None and values['name'] is None:
            raise ValueError('One of `name` or `path` is required')
        return v

    class Config:
        @staticmethod
        def schema_extra(schema: dict[str, Any], model: type['DataResource']) -> None:
            if 'anyOf' not in schema.keys():
                schema['anyOf'] = []
            
            schema['anyOf'] += [{'required' : ['path']}]
            schema['anyOf'] += [{'required' : ['name']}]
            
            
class DataContributor(ExtendedSQLModel):
    title: str
    path: Optional[Union[pathlib.Path, AnyHttpUrl]]
    email: Optional[EmailStr]
    role: Optional[DataContributorRole] = 'contributor'
    organization: Optional[str]


class DataSource(ExtendedSQLModel):
    title: str
    path: Optional[Union[pathlib.Path, AnyHttpUrl]]
    email: Optional[EmailStr]
    
    
class FieldDescriptor(ExtendedSQLModel):
    name: str
    title: Optional[str]
    description: Optional[Union[str, Any]]
    type: Optional[str]
    format: Optional[str]
    example: Optional[Union[str, Any]]
    rdfType: Optional[Union[pathlib.Path, AnyHttpUrl]]
    constraints: Optional[Union[str, Any]]

    
class DataSchemaBase(ExtendedSQLModel):
    missingValues: Optional[list[str]]
    primaryKey: Optional[str]
    foreignKeys: Optional[list[str]]

    
class DataSchema(DataSchemaBase):
    fields: list[FieldDescriptor]


class DataResourceBase(ExtendedSQLModel):
    name: constr(regex='^[a-z0-9_\.,-]*$')
    data: Optional[list[dict[str, Any]]]
    path: Optional[Union[pathlib.Path, AnyHttpUrl]]
    profile: Optional[DataResourceProfile] = 'tabular-data-resource'
    title: Optional[str]
    description: Optional[str]
    format: Optional[DataResourceFormat]
    mediatype: Optional[str]
    encoding: Optional[str]
    bytes: Optional[int]
    hash: Optional[str]

    @validator('path')
    def check_data_or_path(cls, v, values):
        if v is None and values['data'] is None:
            raise ValueError('One of `data` or `path` is required')
        return v

    class Config:
        @staticmethod
        def schema_extra(schema: dict[str, Any], model: type['DataResource']) -> None:
            if 'anyOf' not in schema.keys():
                schema['anyOf'] = []
            
            schema['anyOf'] += [{'required' : ['path']}]
            schema['anyOf'] += [{'required' : ['data']}]


class DataResource(DataResourceBase):
    fd_schema: Optional[DataSchema] = Field(alias='schema')
    sources: Optional[list[DataSource]]
    licenses: Optional[list[DataLicense]]


class DataPackageBase(ExtendedSQLModel):
    name: constr(regex='^[a-z0-9_\.,-]*$')
    id: Optional[Union[uuid.UUID, Any]]
    profile: Optional[DataPackageProfile] = DataPackageProfile.tabular_data_package
    title: Optional[str]
    description: Optional[str]
    homepage: Optional[pathlib.Path]
    version: constr(regex='^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$')
    keywords: Optional[list[str]]
    image: Optional[Union[pathlib.Path, AnyHttpUrl]]
    created: Optional[datetime.datetime]


class DataPackage(DataPackageBase):
    resources: list[DataResource]
    licenses: Optional[list[DataLicense]]
    sources: Optional[list[DataSource]]
    contributors: Optional[list[DataContributor]]


## Dictionary Schemas


## DB Tables
class DataLicenseTable(DataLicense, table=True):
    __tablename__ = 'fd__data_license'
    path: str
    data_license_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    data_resource_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_resource.data_resource_id')
    data_package_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_package.data_package_id')
    data_resource: Optional['DataResourceTable'] = Relationship(back_populates='licenses')
    data_package: Optional['DataPackageTable'] = Relationship(back_populates='licenses')


class DataContributorTable(DataContributor, table=True):
    __tablename__ = 'fd__data_contributor'
    path: str
    data_contributor_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    data_package_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_package.data_package_id')
    data_package: Optional['DataPackageTable'] = Relationship(back_populates='contributors')


class DataSourceTable(DataSource, table=True):
    __tablename__ = 'fd__data_source'
    path: str
    data_source_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    data_resource_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_resource.data_resource_id')
    data_package_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_package.data_package_id')
    data_resource: Optional['DataResourceTable'] = Relationship(back_populates='sources')
    data_package: Optional['DataPackageTable'] = Relationship(back_populates='sources')
    

class FieldDescriptorTable(FieldDescriptor, table=True):
    __tablename__ = 'fd__field_descriptor'
    rdfType: str
    description: str
    example: str
    constraints: str
    field_descriptor_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    data_schema_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_schema.data_schema_id')
    data_schema: Optional['DataSchemaTable'] = Relationship(back_populates='fields')

    
class DataSchemaTable(DataSchemaBase, table=True):
    __tablename__ = 'fd__data_schema'
    data_schema_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    fields: Optional[list[FieldDescriptorTable]] = Relationship()


class DataResourceTable(DataResourceBase, table=True):
    __tablename__ = 'fd__data_resource'
    data: str
    path: str
    data_resource_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    data_package_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_package.data_package_id')
    data_schema_id: Optional[uuid.UUID] = Field(foreign_key='fd__data_schema.data_schema_id')
    schema: Optional[DataSchemaTable] = Relationship()
    sources: Optional[list[DataSourceTable]] = Relationship()
    licenses: Optional[list[DataLicenseTable]] = Relationship()


class DataPackageTable(DataPackageBase, table=True):
    __tablename__ = 'fd__data_package'
    id: str
    homepage: str
    image: str
    data_package_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    resources: Optional[list[DataResourceTable]] = Relationship()
    licenses: Optional[list[DataLicenseTable]] = Relationship()
    sources: Optional[list[DataSourceTable]] = Relationship()
    contributors: Optional[list[DataContributorTable]] = Relationship()


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
class DbClient:
    def __init__(
        self,
        user: Optional[str] = 'postgres',
        password: Optional[str] = None,
        host: Optional[str] = 'localhost',
        port: Optional[int] = 5632,
        database_name: str = 'analytics',
        tables_to_create: Optional = None,
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
        SQLModel.metadata.create_all(self._engine, tables=tables_to_create)

    def run_query(
        self,
        query_str: str
    ):
        with Session(self._engine) as session:
            results = session.execute(text(query_str))
        
        return results

    def create(
        self,
        record: Any,
        tablename: str
    ): 
        schema = table_name_to_schema[tablename]
        
        if isinstance(record, dict):
            record = schema(**record)

        with Session(self._engine) as session:
            schema.create(session, record)
        
        return

    def create_multiple(
        self,
        records: Union[Any, pd.DataFrame],
        table_name: str
    ):      
        schema = table_name_to_schema[table_name]
        
        if isinstance(records, pd.DataFrame):
            records = records.fillna(-99999).replace(-99999, None)

            records = parse_obj_as(
                list[schema],
                records.reset_index().to_dict(orient='records')
            )

        with Session(self._engine) as session:
            schema.create_multiple(session, records)
        
        return

    def get_all(
        self,
        table_name: str,
        return_df: bool = True
    ):
        schema = table_name_to_schema[table_name]
        
        with Session(self._engine) as session:
            obj = schema.all(session)
            
        if return_df:
            return pd.DataFrame([elem.dict() for elem in obj])

        return obj

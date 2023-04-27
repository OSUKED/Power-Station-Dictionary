import logging
import uuid
import datetime
import pathlib
from typing import Any, Union, Optional

from enum import Enum
from pydantic import EmailStr, validator, constr, BaseModel, Field
from sqlmodel import SQLModel, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from sqlalchemy.future import select


## SQLModel Schema Base
def filter_db_table_attrs(
        db_class: SQLModel,
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

            assert len(
                attr_types) == 1, f'Attributes which are lists should contain items of the same type, found multiple types for {attr_name}'
            attr_type = list(attr_types)[0]
        else:
            attr_type = type(attr_value)

        # filtering for table attributes if specified
        is_table = hasattr(attr_type, '__table__')

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
        pathlib.PosixPath,
        datetime.datetime
    ]

    if type(attr_value) in json_obj_types:
        return attr_value
    elif issubclass(type(attr_value), Enum):
        return attr_value.value
    elif type(attr_value) in str_types:
        return str(attr_value)
    else:
        raise ValueError(
            f'{attr_value} of type `{str(type(attr_value))}` could not be converted into a JSON friendly format')


def sqlmodel_obj_to_dict(
    sqlmodel_obj
) -> dict:
    dict_repr = {
        k: jsonise_attr_value(v)
        for k, v
        in sqlmodel_obj.dict().items()
        if v is not None
    }

    for attr_name in filter_db_table_attrs(sqlmodel_obj):
        attr_value = getattr(sqlmodel_obj, attr_name)

        if attr_value is None:
            continue

        if isinstance(attr_value, list):
            dict_repr[attr_name] = [sqlmodel_obj_to_dict(attr_item) for attr_item in attr_value]
        else:
            dict_repr[attr_name] = sqlmodel_obj_to_dict(attr_value)

    return dict_repr


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
        cls,
        session: Session,
        source: Union[dict[Any, Any], SQLModel]
    ):
        if isinstance(source, SQLModel) or isinstance(source, dict):
            obj = cls.parse_obj(source)
        else:
            raise ValueError(f"The input type {type(source)} can not be processed")

        session.add(obj)
        session.commit()

        return obj

    @classmethod
    def create_records(
        cls,
        session: Session,
        sources: list[Union[dict[Any, Any], SQLModel]]
    ):
        for source in sources:
            if isinstance(source, SQLModel) or isinstance(source, dict):
                obj = cls.parse_obj(source)
                session.add(obj)
            else:
                raise ValueError(f"The input type {type(source)} can not be processed")

        session.commit()

        return 


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


class DataPackageReturnType(str, Enum):
    data_package = 'data_package'
    dictionary = 'dict'
    raw_dict = 'raw_dict'


class AssetType(str, Enum):
    power_station = 'power_station'


class Subject(str, Enum):
    link_id = 'link_id'
    data_package = 'data_package'
    dictionary_id = 'dictionary_id'


class Crud(str, Enum):
    create = 'create'
    read = 'read'
    update = 'update'
    delete = 'delete'


class BmrsPhysicalDataset(str, Enum):
    PN = 'PN'
    QPN = 'QPN'
    MILS = 'MILS'
    MELS = 'MELS'


class BmrsPhysicalType(str, Enum):
    PN = 'PN'
    QPN = 'QPN'
    MILS = 'MILS'
    MELS = 'MELS'


class BmrsResponseFormat(str, Enum):
    json = 'json'
    xml = 'xml'
    csv = 'csv'


## Frictionless Schemas
class DataLicense(ExtendedSQLModel):
    name: Optional[str]
    path: Optional[str]
    title: Optional[str]

    @classmethod
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
    path: Optional[str]
    email: Optional[EmailStr]
    role: Optional[DataContributorRole] = 'contributor'
    organization: Optional[str]


class DataSource(ExtendedSQLModel):
    title: str
    path: Optional[str]
    email: Optional[EmailStr]


class FieldDescriptor(ExtendedSQLModel):
    name: str
    title: Optional[str]
    description: Optional[Union[str, Any]]
    type: Optional[str]
    format: Optional[str]
    example: Optional[Union[str, Any]]
    rdfType: Optional[str]
    constraints: Optional[Union[str, Any]]


class DataSchemaBase(ExtendedSQLModel):
    missingValues: Optional[list[str]]
    primaryKey: Optional[str]
    foreignKeys: Optional[list[str]]


class DataSchema(DataSchemaBase):
    fields: list[FieldDescriptor]


class DataResourceBase(ExtendedSQLModel):
    name: constr(regex=r'^[a-z0-9_\.,-]*$')
    data: Optional[list[dict[str, Any]]]
    path: Optional[str]
    profile: Optional[DataResourceProfile] = 'tabular-data-resource'
    title: Optional[str]
    description: Optional[str]
    format: Optional[DataResourceFormat]
    mediatype: Optional[str]
    encoding: Optional[str]
    bytes: Optional[int]
    hash: Optional[str]

    @classmethod
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
    fd_schema: Optional[DataSchema]
    sources: Optional[list[DataSource]]
    licenses: Optional[list[DataLicense]]


class DataPackageBase(ExtendedSQLModel):
    name: constr(regex=r'^[a-z0-9_\.,-]*$')
    id: Optional[Union[uuid.UUID, Any]]
    profile: Optional[DataPackageProfile] = DataPackageProfile.tabular_data_package
    title: Optional[str]
    description: Optional[str]
    homepage: Optional[str]
    version: constr(regex=r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$')
    keywords: Optional[list[str]]
    image: Optional[str]
    created: Optional[datetime.datetime]


class DataPackage(DataPackageBase):
    resources: list[DataResource]
    licenses: Optional[list[DataLicense]]
    sources: Optional[list[DataSource]]
    contributors: Optional[list[DataContributor]]


## API Schemas
class TokenData(BaseModel):
    username: Optional[str] = None


class Token(SQLModel):
    access_token: str
    token_type: str


class APIUser(ExtendedSQLModel):
    username: str
    name: str
    email: Optional[str] = None
    scopes: Optional[str] = None
    disabled: Optional[bool] = None
    is_superuser: Optional[bool] = None


class SecureAPIUser(APIUser):
    hashed_password: Optional[str] = None


class UserEvent(ExtendedSQLModel):
    event_id: uuid.UUID
    username: str
    datetime: datetime.datetime
    subject: Subject
    crud: Crud
    # could look at saving the full request body here


## Dictionary Schemas
class SourceLink(ExtendedSQLModel):
    data_resource_id: uuid.UUID
    linked_id_column: str
    date_added: datetime.datetime
    date_removed: Optional[datetime.datetime]
    linked_id_type: str # with a 1:1 mapping to a link table name
    resource_table_name: str


class Register(ExtendedSQLModel):
    osuked_id: int
    date_added: datetime.datetime
    date_removed: Optional[datetime.datetime]
    asset_type: AssetType = AssetType.power_station
    common_name: str


class RepdIdLink(ExtendedSQLModel):
    osuked_id: int
    repd_id: int
    date_added: datetime.datetime
    date_removed: Optional[datetime.datetime]
    # can later look at adding a 'relationship' field: PartOf, SameAs, etc


class BmuIdLink(ExtendedSQLModel):
    osuked_id: int
    bmu_id: int
    date_added: datetime.datetime
    date_removed: Optional[datetime.datetime]


# BMRS Schemas
class BmrsPhysicalData(ExtendedSQLModel):
    dataset: BmrsPhysicalType
    settlementDate: datetime.date
    settlementPeriod: int
    timeFrom: datetime.datetime
    timeTo: datetime.datetime
    levelFrom: int
    levelTo: float
    nationalGridBmUnit: str
    bmUnit: str | None

class BmrsPhysicalMetadata(BaseModel):
    datasets: list[BmrsPhysicalType]

class BmrsPhysicalResponse(BaseModel):
    data: list[BmrsPhysicalData]
    metadata: BmrsPhysicalMetadata

class BmrsPhysicalRequest(BaseModel):
    dataset: BmrsPhysicalType
    settlementDate: datetime.date
    settlementPeriod: int | None
    bmUnit: str | None
    format: BmrsResponseFormat | None = BmrsResponseFormat.json

import uuid
import datetime
import pathlib
import pandas as pd
from typing import Any, Sequence, Union, Optional, List
from loguru import logger
from sqlalchemy.exc import IntegrityError

from enum import Enum
from pydantic import BaseModel, AnyHttpUrl, EmailStr, validator, constr, parse_obj_as
from sqlmodel import Field, SQLModel, Session, Relationship, create_engine, select, desc
from sqlalchemy import Column, DateTime, func, and_, text
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select
import sys, inspect


## SQLModel Schema Base
class EnrichedSQLModel(SQLModel):
    @classmethod
    def by_id(
        cls, 
        session: Session, 
        id_: Any
    ):
        obj = session.get(cls, id_)
        if obj is None:
            raise NoResultFound(f"{cls.__name__} with id {id_} not found")
        return obj

    @classmethod
    def all(cls, session: Session):
        res = session.execute(select(cls))
        return res.scalars().all()

    @classmethod
    def all_currently_valid(cls, session: Session):
        # TODO make this work when valid_to is a parameter
        res = session.execute(select(cls).filter_by(valid_to=None))
        return res.scalars().all()

    @classmethod
    def create(
        cls, session: Session, source: Union[dict[Any, Any], SQLModel]
    ):
        if isinstance(source, SQLModel) or isinstance(source, dict):
            obj = cls.parse_obj(source)
        else:
            raise ValueError(f"The input type {type(source)} can not be processed")

        session.add(obj)
        session.flush()

        return obj

    @classmethod
    def create_multiple(
        cls, 
        session: Session, 
        sources: Sequence[Union[dict[str, Any], SQLModel]]
    ) -> None:
        for source in sources:
            if isinstance(source, SQLModel):
                obj = cls.from_orm(source)
            elif isinstance(source, dict):
                obj = cls.parse_obj(source)
            else:
                raise ValueError(f"The input type {type(source)} can not be processed")

            session.add(obj)
        
        try:
            session.commit()
        except IntegrityError as e:
            err_msg = f'{str(e.orig).strip()}\nN.b. this error was caught with the first entry but could apply to subsequent rows'
            logger.warning(err_msg)

    def save(self, session: Session) -> None:
        session.add(self)
        session.flush()

    def update(
        self, 
        session: Session, 
        source: Union[dict[Any, Any], SQLModel]
    ):
        if isinstance(source, SQLModel):
            source = source.dict(exclude_unset=True)

        for key, value in source.items():
            setattr(self, key, value)

        session.flush()
        return self

    @classmethod
    def update_by_id(
        cls, 
        session: Session, 
        id_: Union[uuid.UUID, int], 
        update_values: dict[Any, Any]
    ):
        obj = session.get(cls, id_)

        if obj is None:
            raise NoResultFound(f"{cls.__name__} with id {id_} not found")

        for key, value in update_values.items():
            setattr(obj, key, value)

        obj.save(session)

        return obj

    def delete(self, session: Session) -> None:
        session.delete(self)
        session.commit()

    @classmethod
    def delete_by_id(
        cls, 
        session: Session, 
        id_: Union[uuid.UUID, int]
    ):
        obj = session.get(cls, id_)

        if obj is None:
            raise NoResultFound(f"{cls.__name__} with id {id_} not found")

        obj.delete(session)
        session.commit()

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
class DataLicence(EnrichedSQLModel):
    name: Optional[str]
    path: Optional[Union[pathlib.Path, AnyHttpUrl]]
    title: Optional[str]

    @validator('path')
    def check_name_or_path(cls, v, values):
        if v is None and values['name'] is None:
            raise ValueError('One of `name` or `path` is required')

    class Config:
        @staticmethod
        def schema_extra(schema: dict[str, Any], model: type['DataResource']) -> None:
            if 'anyOf' not in schema.keys():
                schema['anyOf'] = []
            
            schema['anyOf'] += [{'required' : ['path']}]
            schema['anyOf'] += [{'required' : ['name']}]


class DataContributor(EnrichedSQLModel):
    title: str
    path: Optional[Union[pathlib.Path, AnyHttpUrl]]
    email: Optional[EmailStr]
    role: Optional[DataContributorRole] = 'contributor'
    organization: Optional[str]


class DataSource(EnrichedSQLModel):
    title: str
    path: Optional[Union[pathlib.Path, AnyHttpUrl]]
    email: Optional[EmailStr]
    
    
class FieldDescriptor(EnrichedSQLModel):
    name: str
    title: Optional[str]
    description: Optional[Any]
    type: Optional[str]
    format: Optional[str]
    example: Optional[Any]
    rdfType: Optional[Union[pathlib.Path, AnyHttpUrl]]
    constraints: Optional[Any]

    
class DataSchema(EnrichedSQLModel):
    fields: list[FieldDescriptor]
    missingValues: list[str]
    primaryKey: str
    foreignKeys: list[str]


class DataResource(EnrichedSQLModel):
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
    # schema
    sources: Optional[list[DataSource]]
    licenses: Optional[list[DataLicence]]

    @validator('path')
    def check_data_or_path(cls, v, values):
        if v is None and values['data'] is None:
            raise ValueError('One of `data` or `path` is required')

    class Config:
        @staticmethod
        def schema_extra(schema: dict[str, Any], model: type['DataResource']) -> None:
            if 'anyOf' not in schema.keys():
                schema['anyOf'] = []
            
            schema['anyOf'] += [{'required' : ['path']}]
            schema['anyOf'] += [{'required' : ['data']}]


class DataPackage(EnrichedSQLModel):
    name: constr(regex='^[a-z0-9_\.,-]*$')
    resources: list[DataResource]
    id: Optional[Union[uuid.UUID, Any]]
    licenses: Optional[list[DataLicence]]
    sources: Optional[list[DataSource]]
    contributors: Optional[list[DataContributor]]
    profile: Optional[DataPackageProfile] = 'tabular-data-resource'
    title: Optional[str]
    description: Optional[str]
    homepage: Optional[pathlib.Path]
    version: constr(regex='^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$')
    keywords: Optional[list[str]]
    image: Optional[Union[pathlib.Path, AnyHttpUrl]]
    created: Optional[datetime.datetime]


## Dictionary Schemas


## DB Tables


# Creating a helper mapping from the table name to the SQLModel class
is_class_member = lambda member: inspect.isclass(member) and member.__module__ == __name__
cls_members = inspect.getmembers(sys.modules[__name__], is_class_member)
    
tablename_to_schema = {
    cls_member[-1].__tablename__: cls_member[-1]
    for cls_member
    in cls_members
    if hasattr(cls_member[-1], '__tablename__')
}


## DB manager
class DbManager:
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
        schema = tablename_to_schema[tablename]
        
        if isinstance(record, dict):
            record = schema(**record)

        with Session(self._engine) as session:
            schema.create(session, record)
        
        return

    def create_multiple(
        self,
        records: Union[Any, pd.DataFrame],
        tablename: str,
        handle_nulls: bool = True
    ):      
        schema = tablename_to_schema[tablename]
        
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
        tablename: str,
        return_df: bool = True
    ):
        schema = tablename_to_schema[tablename]
        
        with Session(self._engine) as session:
            obj = schema.all(session)
            
        if return_df:
            return pd.DataFrame([elem.dict() for elem in obj])

        return obj

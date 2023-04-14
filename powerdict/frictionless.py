import json
import logging
import pathlib
import uuid
from enum import Enum
from typing import Optional
from powerdict import schemas, db

def filter_db_table_attrs(
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

def python_obj_to_dict_repr(
    table_obj: schemas.ExtendedSQLModel
) -> dict:
    dict_repr = {
        k: jsonise_attr_value(v)
        for k, v
        in table_obj.dict().items()
        if v is not None
    }
    
    for attr_name in filter_db_table_attrs(table_obj):
        attr_value = getattr(table_obj, attr_name)

        if isinstance(attr_value, list):
            dict_repr[attr_name] = [python_obj_to_dict_repr(attr_item) for attr_item in attr_value]
        else:
            dict_repr[attr_name] = python_obj_to_dict_repr(attr_value)

    return dict_repr

def select_schema(
    schema_class: schemas.ExtendedSQLModel,
    use_table_schema: bool = False
):
    if use_table_schema:
        if schema_class.__name__[-5:] != 'Table':
            schema_class = getattr(db, schema_class.__name__+'Table')
        return schema_class
    
    return getattr(schemas, schema_class.__name__.replace('Table', ''))

def parse_obj_list(
    raw_objs: list[dict],
    obj_table_class: schemas.ExtendedSQLModel, 
    use_table_schema: bool = False
):  
    obj_schema = select_schema(obj_table_class, use_table_schema)
    
    return [
        raw_obj
        if issubclass(type(raw_obj), schemas.ExtendedSQLModel)
        else obj_schema.parse_obj(raw_obj)
        for raw_obj
        in raw_objs
    ]

def parse_fd_schema_obj(
    schema: dict, 
    use_table_schema: bool = False
):
    obj_schema = select_schema(db.DataSchemaTable, use_table_schema)
    
    if 'fields' in schema.keys():
        schema['fields'] = parse_obj_list(
            schema['fields'], 
            db.FieldDescriptorTable,
            use_table_schema
        )

    return obj_schema.parse_obj(schema)

def parse_fd_resource_obj(
    resource: dict, 
    use_table_schema: bool = False
):
    obj_schema = select_schema(db.DataResourceTable, use_table_schema)
    
    if 'schema' in resource.keys():
        resource['fd_schema'] = resource.pop('schema')
    
    if 'fd_schema' in resource.keys():
        resource['fd_schema'] = parse_fd_schema_obj(resource['fd_schema'], use_table_schema)

    return obj_schema.parse_obj(resource)

def parse_fd_resource_objs(
    resources: list[dict], 
    use_table_schemas: bool = False
):
    resource_profile_to_schema = {
        'tabular-data-resource': parse_fd_resource_obj
    }
    
    resource_objs = []
    
    for resource in resources:
        if resource['profile'] in resource_profile_to_schema.keys():
            resource_objs += [resource_profile_to_schema[resource['profile']](resource, use_table_schemas)]

    return resource_objs

def attr_filter(
    schema_class: type,
    public_only: bool = True,
    subclass_of: Optional[type] = None
):
    attrs = []
    
    for attr in dir(schema_class):
        if (
            (public_only == True) and
            (attr[0] == '_')
        ):
            continue
        
        if isinstance(getattr(schema_class, attr), list):
            attr_values = getattr(schema_class, attr)
            if len(attr_values) == 0:
                continue
            attr_type = type(getattr(schema_class, attr)[0])
        else:
            attr_type = type(getattr(schema_class, attr))
        
        if (
            (public_only == True) and
            (attr[0] == '_')
        ):
            pass
        
        elif (
            (subclass_of is not None) and
            (issubclass(attr_type, subclass_of) == False)
        ):
            pass
        
        else:
            attrs += [attr]
        
    return attrs

def fd_sqlmodel_schema_to_id_attrs(sqlmodel_schema):
    id_name = sqlmodel_schema.__tablename__.split('__')[1] + '_id'
    id_value = getattr(sqlmodel_schema, id_name)
    return id_name, id_value

def add_linked_ids_to_fd_sqlmodel_schema(fd_sqlmodel_schema):
    # to help generalise could have fd_sqlmodel_schema_to_id_attrs as an input
    child_attr_names = attr_filter(fd_sqlmodel_schema, subclass_of=schemas.ExtendedSQLModel)
    
    if len(child_attr_names) == 0:
        return fd_sqlmodel_schema
    
    parent_id_name, parent_id_value = fd_sqlmodel_schema_to_id_attrs(fd_sqlmodel_schema)

    for child_attr_name in child_attr_names:
        child_attr_obj = getattr(fd_sqlmodel_schema, child_attr_name)
        
        # if it's a list then the parent id needs putting in the child
        if isinstance(child_attr_obj, list):
            child_attr_objs_with_parent_id = []

            for child_attr_obj_item in child_attr_obj:
                setattr(child_attr_obj_item, parent_id_name, parent_id_value)
                child_attr_obj_item = add_linked_ids_to_fd_sqlmodel_schema(child_attr_obj_item)
                child_attr_objs_with_parent_id += [child_attr_obj_item]

            setattr(fd_sqlmodel_schema, child_attr_name, child_attr_objs_with_parent_id)

        # if it's not a list then the child id needs adding to the parent id
        else:
            child_attr_obj = add_linked_ids_to_fd_sqlmodel_schema(child_attr_obj)
            child_id_name, child_id_value = fd_sqlmodel_schema_to_id_attrs(child_attr_obj)
            setattr(fd_sqlmodel_schema, child_id_name, child_id_value)

    return fd_sqlmodel_schema

def parse_fd_package_obj(
    package: dict, 
    use_table_schemas: bool = False
):
    if not isinstance(package, dict):
        package = python_obj_to_dict_repr(package)

    if 'resources' in package.keys():
        package['resources'] = parse_fd_resource_objs(package['resources'], use_table_schemas)
        
    if 'licenses' in package.keys():
        package['licenses'] = parse_obj_list(package['licenses'], db.DataLicenseTable, use_table_schemas)
        
    if 'contributors' in package.keys():
        package['contributors'] = parse_obj_list(package['contributors'], db.DataContributorTable, use_table_schemas)

    obj_schema = select_schema(db.DataPackageTable, use_table_schemas)
    parsed_package = obj_schema.parse_obj(package)
    
    if use_table_schemas:
        parsed_package = add_linked_ids_to_fd_sqlmodel_schema(parsed_package)
    
    return parsed_package


def fd_package_to_db_records(
        sqlmodel_schema,
        db_records: Optional[dict[str, list]] = None
):
    if db_records is None:
        db_records = {}

    schema_table_name = sqlmodel_schema.__tablename__

    # adding the parent db record
    if schema_table_name not in db_records.keys():
        db_records[schema_table_name] = []

    db_records[schema_table_name] += [sqlmodel_schema.dict()]

    # handling children records
    child_attr_names = attr_filter(sqlmodel_schema, subclass_of=schemas.ExtendedSQLModel)

    if len(child_attr_names) == 0:
        return db_records

    for child_attr_name in child_attr_names:
        child_attr_obj = getattr(sqlmodel_schema, child_attr_name)

        # adding enumerated child records
        if isinstance(child_attr_obj, list):
            for child_attr_obj_item in child_attr_obj:
                db_records = fd_package_to_db_records(child_attr_obj_item, db_records)

        # adding single child records
        else:
            db_records = fd_package_to_db_records(child_attr_obj, db_records)

    return db_records


def save_fd_package_to_db(
    raw_package_metadata: dict, 
    db_client
):
    fd_package = parse_fd_package_obj(raw_package_metadata, use_table_schemas=True)
    db_records = fd_package_to_db_records(fd_package)
    db_client.create_multi_table_records(db_records)
    
    return fd_package

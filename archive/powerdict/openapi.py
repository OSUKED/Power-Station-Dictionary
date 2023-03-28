import yaml
import numpy as np
import pandas as pd

import os
import requests
from tqdm import tqdm
from copy import deepcopy
from jinja2 import Template


def load_api_spec(spec_url):
    with requests.get(spec_url, headers=headers) as r:
        api_spec = yaml.load(r.content, Loader=yaml.FullLoader)

    return api_spec


def get_server_url(api_spec):
    assert 'servers' in api_spec.keys(), '`servers` must be specified within the specification'
    assert len(api_spec['servers']) > 0, 'There must be at least one server specified'

    server = api_spec['servers'][0]['url']

    return server


def extract_item_from_dict_path(dict_, path):
    item = dict_

    if not isinstance(item, dict):
        return None

    for path_component in path:
        if path_component not in item.keys():
            return None
        else:
            item = item[path_component]

    return item


def construct_meta_attr_values(
    api_spec,
    meta_attr_to_spec_path: dict = {
        'title': ['info', 'title'],
        'version': ['info', 'version'],
        'description': ['info', 'description'],
        'license_name': ['info', 'license', 'name'],
        'license_url': ['info', 'license', 'url'],
        'documentation': ['info', 'externalDocs', 'url'],
    },
):
    meta_attr_values = {}

    for meta_attr, spec_path in meta_attr_to_spec_path.items():
        meta_value = extract_item_from_dict_path(api_spec, spec_path)

        if meta_value is not None:
            meta_attr_values[meta_attr] = meta_value

    return meta_attr_values


def get_metadata_md_str(meta_attr_values):
    s_metadata = pd.Series(meta_attr_values)
    s_metadata.index.name = 'Attribute'
    s_metadata.name = 'Value(s)'

    return s_metadata.to_markdown()


def construct_package_elements_overview(api_spec):
    meta_attr_values = construct_meta_attr_values(api_spec)

    package_elements = {
        'title': meta_attr_values.pop('title'),
        'description': (meta_attr_values.pop('description') if 'description' in meta_attr_values.keys() else False),
        'metadata': get_metadata_md_str(meta_attr_values),
    }

    return package_elements


extract_endpoint_title = lambda endpoint: endpoint.replace('/', ' ').strip().title()

extract_tags = lambda api_spec, endpoint, method='get': extract_item_from_dict_path(
    api_spec['paths'][endpoint][method], ['tags']
)


def get_ref_item(api_spec, ref_path):
    item = api_spec

    for path_component in ref_path[2:].split('/'):
        item = item[path_component]

    return item


def populate_from_ref_json(json_, ref_json):
    json_out = json_.copy()

    if isinstance(json_, list):
        for i, json_item in enumerate(json_):
            if type(json_item) in [list, dict]:
                json_out[i] = populate_from_ref_json(json_item, ref_json)

    if isinstance(json_, dict):
        for k, json_item in json_.items():
            if type(json_item) in [list, dict]:
                json_out[k] = populate_from_ref_json(json_item, ref_json)
            elif k == '$ref':
                ref_item = get_ref_item(ref_json, json_item)
                if type(ref_item) in [list, dict]:
                    ref_item = populate_from_ref_json(ref_item, ref_json)
                json_out[k] = ref_item

    if len(json_out) == 1 and '$ref' in json_out.keys():
        json_out = json_out['$ref']

    return json_out


def get_path_schema(
    path_spec,
    status_code: int = 200,
    response_headers: dict = {'Content-Type': 'application/json'},
):
    response_content = path_spec['get']['responses'][str(status_code)]['content']
    returned_content_types = [ct for ct in response_headers['Content-Type'].split(';') if ct in response_content.keys()]
    assert len(returned_content_types) == 1
    content_type = returned_content_types[0]

    schema = populate_from_ref_json(response_content[content_type]['schema'], api_spec)

    return schema


def get_schema_properties(schema):
    def extract_properties(schema):
        if schema['type'] == 'array':
            properties = schema['items']['properties'].copy()
        else:
            properties = schema['properties'].copy()

        return properties

    properties = extract_properties(schema)

    if 'data' in properties.keys():
        sub_schema = properties.pop('data')
        properties.update(extract_properties(sub_schema))

    if 'metadata' in properties.keys():
        properties.pop('metadata')

    return properties


def construct_response_fields_df(api_spec, endpoint):
    endpoint_field_properties = get_schema_properties(get_path_schema(api_spec['paths'][endpoint]))

    response_fields = [{'field': field} for field in endpoint_field_properties.keys()]
    [response_fields[i].update(v) for i, (k, v) in enumerate(endpoint_field_properties.items())]

    df_response_fields = pd.DataFrame(response_fields).dropna(how='all').replace(np.nan, '-')
    df_response_fields.columns = df_response_fields.columns.str.capitalize()
    df_response_fields = df_response_fields.set_index('Field')

    return df_response_fields


def construct_request_parameters_df(api_spec, endpoint):
    params = deepcopy(api_spec['paths'][endpoint]['get']['parameters'])
    cleaned_params = []

    for i, param in enumerate(params):
        cleaned_params += [{}]

        if 'schema' in param.keys():
            cleaned_params[i].update(param.pop('schema'))

        cleaned_params[i].update(param)

        if 'type' in cleaned_params[i].keys():
            if cleaned_params[i]['type'] == 'array' and 'items' in cleaned_params[i].keys():
                if 'type' in cleaned_params[i]['items'].keys():
                    cleaned_params[i]['type'] += ', ' + cleaned_params[i]['items']['type']
                    cleaned_params[i].pop('items')

    df_request_params = pd.DataFrame(cleaned_params)

    df_request_params = pd.DataFrame(df_request_params).dropna(how='all').replace(np.nan, '-')
    df_request_params.columns = df_request_params.columns.str.capitalize()
    df_request_params = df_request_params.set_index('Name')
    df_request_params.index.name = 'Parameters'

    return df_request_params


def construct_endpoint_element(api_spec, endpoint):
    endpoint_element = {
        'title': extract_endpoint_title(endpoint),
        'keywords': ', '.join(extract_tags(api_spec, endpoint)),
        'endpoint_url': get_server_url(api_spec) + endpoint,
        'description': None,
        'response_fields': construct_response_fields_df(api_spec, endpoint).to_markdown(),
        'request_params': construct_request_parameters_df(api_spec, endpoint).to_markdown(),
    }

    endpoint_element = {k: (v if v is not None else False) for k, v in endpoint_element.items()}

    return endpoint_element


def construct_package_elements(fk_obj):
    spec_url = fk_obj['reference']['openapi']
    endpoints = fk_obj['reference']['paths']

    package_elements = construct_package_elements_overview(api_spec)
    package_elements['endpoint_elements'] = []

    for endpoint in endpoints:
        package_elements['endpoint_elements'] += [construct_endpoint_element(api_spec, endpoint)]

    return package_elements

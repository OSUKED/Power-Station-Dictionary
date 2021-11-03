# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/09-id-submission.ipynb (unless otherwise specified).

__all__ = ['SheetManager', 'load_powerdict_data', 'construct_field_title_to_name_map', 'assign_new_id_value',
           'assign_all_new_id_values', 'update_powerdict_ids_df', 'app']

# Cell
import json
import numpy as np
import pandas as pd

import os
import typer
from typing import Any
from dataclasses import dataclass

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Cell
@dataclass
class SheetManager:
    creds_fp: str='../gcloud/power-station-dictionary-9cca2a03718d.json'
    sheet_name: str='Power Station Dictionary - ID Submission (Responses)'
    sheet_index: int=0

    def __post_init__(self):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

        if os.path.exists(self.creds_fp) == True:
            creds = ServiceAccountCredentials.from_json_keyfile_name(self.creds_fp, scope)
        elif 'GCP_SA_KEY' in os.environ.keys():
            creds = json.loads(os.getenv('GCP_SA_KEY'))
        else:
            raise ValueError('No valid credentials (or filepath) was passed')

        self.client = gspread.authorize(creds)

        sheet = self.client.open(self.sheet_name)
        self.sheet_instance = sheet.get_worksheet(self.sheet_index)

        return

    load_sheet_df = lambda self: pd.DataFrame.from_dict(self.sheet_instance.get_all_records())

    def update_sheet_col_values(
        self,
        df_sheet: pd.DataFrame,
        col_name: str='Processed'
    ):
        col_insert = [[col_name]+df_sheet[col_name].to_list()]
        col_idx = [idx+1 for idx, idx_col_name in enumerate(df_sheet.columns) if idx_col_name==col_name][0]

        self.sheet_instance.delete_columns(col_idx)
        self.sheet_instance.insert_cols(col_insert, col=col_idx)

        return

# Cell
def load_powerdict_data(
    ids_fp: str='../data/dictionary/ids.csv',
    metadata_fp: str='../data/dictionary/datapackage.json'
):
    df_powerdict_ids = pd.read_csv(ids_fp)
    df_powerdict_ids = df_powerdict_ids.set_index('osuked_id')

    with open(metadata_fp) as f:
        powerdict_metadata = json.load(f)

    return df_powerdict_ids, powerdict_metadata

# Cell
def construct_field_title_to_name_map(powerdict_metadata: dict):
    field_title_to_name_map = {
        field['title']: field['name']
        for field
        in powerdict_metadata['resources'][0]['schema']['fields']
    }

    return field_title_to_name_map

# Cell
def assign_new_id_value(
    df_powerdict_ids: pd.DataFrame,
    dictionary_id: int,
    new_id_title: str,
    new_id_value: Any,
    field_title_to_name_map: dict,
):
    new_id_name = field_title_to_name_map[new_id_title]
    current_id = df_powerdict_ids.loc[dictionary_id, new_id_name]
    new_id_in_old_ids = str(new_id_value) in str(current_id).split(', ')

    if isinstance(current_id, (int, float)):
        no_previous_id = np.isnan(current_id)
    elif current_id == '' or current_id == 'np.nan':
        no_previous_id = True
    else:
        no_previous_id = False

    if new_id_in_old_ids:
        pass
    elif no_previous_id:
        df_powerdict_ids.loc[dictionary_id, new_id_name] = new_id_value
    else:
        df_powerdict_ids.loc[dictionary_id, new_id_name] = str(current_id) + ', ' + new_id_value

    return df_powerdict_ids

def assign_all_new_id_values(
    df_powerdict_ids: pd.DataFrame,
    df_sheet: pd.DataFrame,
    field_title_to_name_map: dict
):
    idxs_to_process = df_sheet.index[df_sheet['Processed'].replace('', np.nan).isnull()]

    for dictionary_id, (new_id_title, new_id_value) in df_sheet.loc[idxs_to_process].set_index('Dictionary ID Value')[['ID Type', 'ID Value']].iterrows():
        df_powerdict_ids = assign_new_id_value(
            df_powerdict_ids,
            dictionary_id,
            new_id_title,
            new_id_value,
            field_title_to_name_map,
        )

    df_sheet.loc[idxs_to_process, 'Processed'] = 1

    return df_powerdict_ids, df_sheet

# Cell
app = typer.Typer()

@app.command()
def update_powerdict_ids_df(
    creds_fp: str ='gcloud/power-station-dictionary-9cca2a03718d.json',
    sheet_name: str ='Power Station Dictionary - ID Submission (Responses)',
    sheet_index: int=0,
    ids_fp: str ='data/dictionary/ids.csv',
    metadata_fp: str ='data/dictionary/datapackage.json',
    processed_col_name: str='Processed'
):
    sheet_manager = SheetManager(creds_fp=creds_fp, sheet_name=sheet_name, sheet_index=sheet_index)
    df_sheet = sheet_manager.load_sheet_df()

    df_powerdict_ids, powerdict_metadata = load_powerdict_data(ids_fp=ids_fp, metadata_fp=metadata_fp)
    field_title_to_name_map = construct_field_title_to_name_map(powerdict_metadata)

    df_powerdict_ids, df_sheet = assign_all_new_id_values(df_powerdict_ids, df_sheet, field_title_to_name_map)
    sheet_manager.update_sheet_col_values(df_sheet, col_name=processed_col_name)
    df_powerdict_ids.to_csv(ids_fp)

    return df_powerdict_ids

# Cell
if __name__ == '__main__' and '__file__' in globals():
    app()
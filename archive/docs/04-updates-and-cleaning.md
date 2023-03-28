# Data Checks, Updates & Cleaning



```python
#exports
import json
import pandas as pd

import os
import typing
from warnings import warn

from powerdict import construct
```

```python
from IPython.display import JSON
```

<br>

### User Inputs

```python
intermediate_data_dir = '../data/intermediate'
definitions_dir = '../data/definitions'
updates_data_dir = '../data/updates'
output_data_dir = '../data/output'
```

<br>

### Loading in Intermediate Data

```python
df = pd.read_csv(f'{intermediate_data_dir}/power_stations.csv').astype(str).set_index('osuked_id')

df.head()
```




|   ('Unnamed: 0_level_0', 'osuked_id') | ('esail_id', 'Unnamed: 1_level_1')   | ('fuel_type', 'Unnamed: 2_level_1')   | ('sett_bmu_id', 'Unnamed: 3_level_1')             |   ('longitude', 'Unnamed: 4_level_1') |   ('latitude', 'Unnamed: 5_level_1') |
|--------------------------------------:|:-------------------------------------|:--------------------------------------|:--------------------------------------------------|--------------------------------------:|-------------------------------------:|
|                                 10000 | MARK                                 | biomass                               | E_MARK-1, E_MARK-2                                |                             -3.60352  |                              57.4804 |
|                                 10001 | DIDC                                 | coal                                  | T_DIDC1, T_DIDC2, T_DIDC4, T_DIDC3                |                             -1.26757  |                              51.6236 |
|                                 10002 | ABTH                                 | coal                                  | T_ABTH7, T_ABTH8, T_ABTH9                         |                             -3.40487  |                              51.3873 |
|                                 10003 | COTPS                                | coal                                  | T_COTPS-1, T_COTPS-2, T_COTPS-3, T_COTPS-4        |                             -0.648193 |                              53.2455 |
|                                 10004 | DRAXX                                | coal                                  | T_DRAXX-1, T_DRAXX-2, T_DRAXX-3, T_DRAXX-4, T_... |                             -0.626221 |                              53.7487 |</div>



<br>

### Custom Data Checks

We'll start by confirming that none of the plants have multiple locations assigned to them

```python
#exports
def filter_cols_for_one_to_many(df, cols=['longitude', 'latitude']):
    df_one_to_many_filt = df[df[cols].astype(str).agg(''.join, axis=1).str.contains(', ')]
    return df_one_to_many_filt
```

```python
df_multiple_locs = filter_cols_for_one_to_many(df)

assert df_multiple_locs.size == 0, 'There should not be multiple locations for a single site'
```

```python
#exports
def apply_updates(df, updates_data_dir):
    update_files = [f for f in os.listdir(updates_data_dir) if f.replace('.json', '') in df.columns]

    for update_file in update_files:    
        with open(f'{updates_data_dir}/{update_file}', 'r') as f:
            update_dict = json.load(f)
            
        update_col = update_file.replace('.json', '')
        update_values = {k: v['new_value'] for k, v in update_dict.items()}
        
        df = construct.update_df_col(df, update_col, update_values)
        
    return df
```

```python
df = apply_updates(df, updates_data_dir)

df.head()
```




|   ('Unnamed: 0_level_0', 'osuked_id') | ('esail_id', 'Unnamed: 1_level_1')   | ('fuel_type', 'Unnamed: 2_level_1')   | ('sett_bmu_id', 'Unnamed: 3_level_1')             |   ('longitude', 'Unnamed: 4_level_1') |   ('latitude', 'Unnamed: 5_level_1') |
|--------------------------------------:|:-------------------------------------|:--------------------------------------|:--------------------------------------------------|--------------------------------------:|-------------------------------------:|
|                                 10000 | MARK                                 | biomass                               | E_MARK-1, E_MARK-2                                |                             -3.60352  |                              57.4804 |
|                                 10001 | DIDC                                 | coal                                  | T_DIDC1, T_DIDC2, T_DIDC4, T_DIDC3                |                             -1.26757  |                              51.6236 |
|                                 10002 | ABTH                                 | coal                                  | T_ABTH7, T_ABTH8, T_ABTH9                         |                             -3.40487  |                              51.3873 |
|                                 10003 | COTPS                                | coal                                  | T_COTPS-1, T_COTPS-2, T_COTPS-3, T_COTPS-4        |                             -0.648193 |                              53.2455 |
|                                 10004 | DRAXX                                | coal, biomass                         | T_DRAXX-1, T_DRAXX-2, T_DRAXX-3, T_DRAXX-4, T_... |                             -0.626221 |                              53.7487 |</div>



<br>

### Checking/Applying Output Definitions

```python
with open(f'{definitions_dir}/outputs.json', 'r') as f:
    output_defs = json.load(f)
    
JSON(output_defs)
```




    <IPython.core.display.JSON object>



```python
#exports
def check_output_col_values(df, output_col, output_defs):
    output_col_def = output_defs[output_col]
    
    if isinstance(output_col_def, list):
        output_col_elems = list()

        for elem in df[output_col].to_list():
            if ', ' in elem:
                output_col_elems += elem.split(', ')
            else:
                output_col_elems += [elem]

        unexpected_col_elems = sorted(list(set(output_col_elems) - set(output_col_def)))
        
        if len(unexpected_col_elems) > 0:
            warn(f"The following list elements were not expected in {output_col}: {', '.join(unexpected_col_elems)}")
        
    return
```

```python
output_col = 'fuel_type'

check_output_col_values(df, output_col, output_defs)
```

```python
#exports
def apply_output_col_types(df, output_col, output_defs):
    output_col_def = output_defs[output_col]
    
    if isinstance(output_col_def, list):
        dtype = type(output_col_def[0])
    else:
        dtype = output_col_def
        
    df[output_col] = df[output_col].astype(dtype)
        
    return df
```

```python
output_col = 'longitude'

apply_output_col_types(df, output_col, output_defs)['longitude'].dtype
```




    dtype('float64')



```python
#exports
def check_and_apply_output_defs(df, definitions_dir):
    with open(f'{definitions_dir}/outputs.json', 'r') as f:
        output_defs = json.load(f)

    for output_col in output_defs.keys():
        if output_col not in df.columns:
            warn(f'{output_col} was not found in the output dataset')
        else:
            check_output_col_values(df, output_col, output_defs)
            df = apply_output_col_types(df, output_col, output_defs)
            
    return df
```

```python
df = check_and_apply_output_defs(df, definitions_dir)

df.head()
```

    <ipython-input-15-424d1db4ecaf>:7: UserWarning: plant_type was not found in the output dataset
      warn(f'{output_col} was not found in the output dataset')
    <ipython-input-15-424d1db4ecaf>:7: UserWarning: capacity was not found in the output dataset
      warn(f'{output_col} was not found in the output dataset')
    




|   ('Unnamed: 0_level_0', 'osuked_id') | ('esail_id', 'Unnamed: 1_level_1')   | ('fuel_type', 'Unnamed: 2_level_1')   | ('sett_bmu_id', 'Unnamed: 3_level_1')             |   ('longitude', 'Unnamed: 4_level_1') |   ('latitude', 'Unnamed: 5_level_1') |
|--------------------------------------:|:-------------------------------------|:--------------------------------------|:--------------------------------------------------|--------------------------------------:|-------------------------------------:|
|                                 10000 | MARK                                 | biomass                               | E_MARK-1, E_MARK-2                                |                             -3.60352  |                              57.4804 |
|                                 10001 | DIDC                                 | coal                                  | T_DIDC1, T_DIDC2, T_DIDC4, T_DIDC3                |                             -1.26757  |                              51.6236 |
|                                 10002 | ABTH                                 | coal                                  | T_ABTH7, T_ABTH8, T_ABTH9                         |                             -3.40487  |                              51.3873 |
|                                 10003 | COTPS                                | coal                                  | T_COTPS-1, T_COTPS-2, T_COTPS-3, T_COTPS-4        |                             -0.648193 |                              53.2455 |
|                                 10004 | DRAXX                                | coal, biomass                         | T_DRAXX-1, T_DRAXX-2, T_DRAXX-3, T_DRAXX-4, T_... |                             -0.626221 |                              53.7487 |</div>



```python
# then start doing some matching with GPPDB
```

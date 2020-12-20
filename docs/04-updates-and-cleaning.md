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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>esail_id</th>
      <th>fuel_type</th>
      <th>sett_bmu_id</th>
      <th>longitude</th>
      <th>latitude</th>
    </tr>
    <tr>
      <th>osuked_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10000</th>
      <td>MARK</td>
      <td>biomass</td>
      <td>E_MARK-1, E_MARK-2</td>
      <td>-3.603516</td>
      <td>57.480403</td>
    </tr>
    <tr>
      <th>10001</th>
      <td>DIDC</td>
      <td>coal</td>
      <td>T_DIDC1, T_DIDC2, T_DIDC4, T_DIDC3</td>
      <td>-1.26757</td>
      <td>51.62363</td>
    </tr>
    <tr>
      <th>10002</th>
      <td>ABTH</td>
      <td>coal</td>
      <td>T_ABTH7, T_ABTH8, T_ABTH9</td>
      <td>-3.404866</td>
      <td>51.387312</td>
    </tr>
    <tr>
      <th>10003</th>
      <td>COTPS</td>
      <td>coal</td>
      <td>T_COTPS-1, T_COTPS-2, T_COTPS-3, T_COTPS-4</td>
      <td>-0.648193</td>
      <td>53.245495</td>
    </tr>
    <tr>
      <th>10004</th>
      <td>DRAXX</td>
      <td>coal</td>
      <td>T_DRAXX-1, T_DRAXX-2, T_DRAXX-3, T_DRAXX-4, T_...</td>
      <td>-0.626221</td>
      <td>53.748711</td>
    </tr>
  </tbody>
</table>
</div>



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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>esail_id</th>
      <th>fuel_type</th>
      <th>sett_bmu_id</th>
      <th>longitude</th>
      <th>latitude</th>
    </tr>
    <tr>
      <th>osuked_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10000</th>
      <td>MARK</td>
      <td>biomass</td>
      <td>E_MARK-1, E_MARK-2</td>
      <td>-3.603516</td>
      <td>57.480403</td>
    </tr>
    <tr>
      <th>10001</th>
      <td>DIDC</td>
      <td>coal</td>
      <td>T_DIDC1, T_DIDC2, T_DIDC4, T_DIDC3</td>
      <td>-1.267570</td>
      <td>51.623630</td>
    </tr>
    <tr>
      <th>10002</th>
      <td>ABTH</td>
      <td>coal</td>
      <td>T_ABTH7, T_ABTH8, T_ABTH9</td>
      <td>-3.404866</td>
      <td>51.387312</td>
    </tr>
    <tr>
      <th>10003</th>
      <td>COTPS</td>
      <td>coal</td>
      <td>T_COTPS-1, T_COTPS-2, T_COTPS-3, T_COTPS-4</td>
      <td>-0.648193</td>
      <td>53.245495</td>
    </tr>
    <tr>
      <th>10004</th>
      <td>DRAXX</td>
      <td>coal, biomass</td>
      <td>T_DRAXX-1, T_DRAXX-2, T_DRAXX-3, T_DRAXX-4, T_...</td>
      <td>-0.626221</td>
      <td>53.748711</td>
    </tr>
  </tbody>
</table>
</div>



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
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>esail_id</th>
      <th>fuel_type</th>
      <th>sett_bmu_id</th>
      <th>longitude</th>
      <th>latitude</th>
    </tr>
    <tr>
      <th>osuked_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10000</th>
      <td>MARK</td>
      <td>biomass</td>
      <td>E_MARK-1, E_MARK-2</td>
      <td>-3.603516</td>
      <td>57.480403</td>
    </tr>
    <tr>
      <th>10001</th>
      <td>DIDC</td>
      <td>coal</td>
      <td>T_DIDC1, T_DIDC2, T_DIDC4, T_DIDC3</td>
      <td>-1.267570</td>
      <td>51.623630</td>
    </tr>
    <tr>
      <th>10002</th>
      <td>ABTH</td>
      <td>coal</td>
      <td>T_ABTH7, T_ABTH8, T_ABTH9</td>
      <td>-3.404866</td>
      <td>51.387312</td>
    </tr>
    <tr>
      <th>10003</th>
      <td>COTPS</td>
      <td>coal</td>
      <td>T_COTPS-1, T_COTPS-2, T_COTPS-3, T_COTPS-4</td>
      <td>-0.648193</td>
      <td>53.245495</td>
    </tr>
    <tr>
      <th>10004</th>
      <td>DRAXX</td>
      <td>coal, biomass</td>
      <td>T_DRAXX-1, T_DRAXX-2, T_DRAXX-3, T_DRAXX-4, T_...</td>
      <td>-0.626221</td>
      <td>53.748711</td>
    </tr>
  </tbody>
</table>
</div>



```python
# then start doing some matching with GPPDB
```

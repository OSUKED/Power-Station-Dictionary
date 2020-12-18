# Data Checks, Updates & Cleaning



```python
#exports
import json
import pandas as pd

import os
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
updates_data_dir = '../data/updates'
definitions_dir = '../data/definitions'
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

### Data Checks

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
        df = construct.update_df_col(df, update_col, update_dict)
        
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
      <td>coal, biomass</td>
      <td>T_DRAXX-1, T_DRAXX-2, T_DRAXX-3, T_DRAXX-4, T_...</td>
      <td>-0.626221</td>
      <td>53.748711</td>
    </tr>
  </tbody>
</table>
</div>



```python
with open(f'{definitions_dir}/outputs.json', 'r') as f:
    outputs = json.load(f)
    
JSON(outputs)
```




    <IPython.core.display.JSON object>



```python
# apply output def checks then apply dtypes
```

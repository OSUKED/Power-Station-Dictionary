# Defining Outputs & Inputs



```python
import json
import pandas as pd

import os
from typing import Any
```

```python
from IPython.display import JSON
```

<br>

### User Inputs

```python
raw_data_dir = '../data/raw'
definitions_dir = '../data/definitions'
```

<br>

### Output Definitions

Before we collate the data sources into a single dataset we want to first define the attribute sets we want to have in our outputs, for attributes that are not categorical we will specify `None`.

```python
outputs = {
    'fuel_type': [
        'gas',
        'coal',
        'wind',
        'solar',
        'oil',
        'hydro',
        'nuclear',
        'biomass',
        'other' # e.g. for batteries or aggregators
    ],
    'plant_type': [
        'ccgt',
        'ocgt',
        'coal',
        'onshore_wind',
        'offshore_wind',
        'floating_wind',
        'conc_solar',
        'pv_solar',
        'oil',
        'run_of_river',
        'pumped_storage',
        'nuclear',
        'aggregator',
        'battery',
        'biomass',
        'other' # ideally no plants should come under this, the preference is to create a new category
    ],
    'capacity': 'float',
    'sett_bmu_id': 'str',
    'longitude': 'float',
    'latitude': 'float'
}

JSON(outputs)
```




    <IPython.core.display.JSON object>



<br>

We'll save this to the definitions directory

```python
with open(f'{definitions_dir}/outputs.json', 'w') as f:
    json.dump(outputs, f)
```

<br>

### Source Definitions

#### ESAIL

We'll start by loading the dataset in

```python
filename = 'ESAIL.csv'

df_ESAIL = pd.read_csv(f'{raw_data_dir}/{filename}')

df_ESAIL.head()
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
      <th>sett_bmu_id</th>
      <th>ngc_bmu_id</th>
      <th>bmu_root</th>
      <th>name</th>
      <th>primary_fuel_type</th>
      <th>detailed_fuel_type</th>
      <th>longitude</th>
      <th>latitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>E_MARK-1</td>
      <td>MARK-1</td>
      <td>MARK</td>
      <td>Rothes Bio-Plant CHP 1</td>
      <td>biomass</td>
      <td>bone</td>
      <td>-3.603516</td>
      <td>57.480403</td>
    </tr>
    <tr>
      <th>1</th>
      <td>E_MARK-2</td>
      <td>MARK-2</td>
      <td>MARK</td>
      <td>Rothes Bio-Plant CHP 2</td>
      <td>biomass</td>
      <td>bone</td>
      <td>-3.603516</td>
      <td>57.480403</td>
    </tr>
    <tr>
      <th>2</th>
      <td>T_DIDC1</td>
      <td>DIDC1</td>
      <td>DIDC</td>
      <td>Didcot A (G) 1</td>
      <td>coal</td>
      <td>coalgas_opt_out</td>
      <td>-1.267570</td>
      <td>51.623630</td>
    </tr>
    <tr>
      <th>3</th>
      <td>T_DIDC2</td>
      <td>DIDC2</td>
      <td>DIDC</td>
      <td>Didcot A (G) 2</td>
      <td>coal</td>
      <td>coalgas_opt_out</td>
      <td>-1.267570</td>
      <td>51.623630</td>
    </tr>
    <tr>
      <th>4</th>
      <td>T_DIDC4</td>
      <td>DIDC4</td>
      <td>DIDC</td>
      <td>Didcot A (G) 4</td>
      <td>coal</td>
      <td>coalgas_opt_out</td>
      <td>-1.267570</td>
      <td>51.623630</td>
    </tr>
  </tbody>
</table>
</div>



<br>

We'll then define the key column, as well as the mapping from the OSUKED key to the ESAIL key

```python
def check_key_input_col(df, key_input_col):
    df[key_input_col].isnull().sum() == 0, f'{key_input_col} can not contain missing values'
    return df

key_input_col = 'bmu_root'
key_output_col = 'esail_id'

key_map = (df_ESAIL
           .pipe(check_key_input_col, key_input_col)
           [[key_input_col]]
           .drop_duplicates()
           .reset_index()
           .pipe(lambda df: df.assign(index=df.index+10000))
           .set_index('index')
           [key_input_col]
           .to_dict()
          )

JSON([key_map])
```




    <IPython.core.display.JSON object>



<br>

We'll also define how we want to extract data from the attribute columns, specifically we provide the name of the new output column, the rank of the source in regards to this column, and the value mapping necessary for that columns content to match the desired output.

```python
attr_cols = {
    'primary_fuel_type': {
        'output_col': 'fuel_type',
        'output_rank': 0, # rank to determine which input to use when multiple are provided, 0 is highest
        'value_map': {
            'wind': 'wind', 
            'gas': 'gas', 
            'coal': 'coal', 
            'fuel_oil': 'oil', 
            'nuclear': 'nuclear', 
            'run_of_river': 'hydro',
            'pumped_storage': 'hydro', 
            'aggregator': 'other', 
            'other': 'other', 
            'rgt': 'gas', 
            'biomass': 'biomass', 
            'battery': 'other'
        }
    },
    'sett_bmu_id': {
        'output_col': 'sett_bmu_id',
        'output_rank': 0, 
        'value_map': None
    },
    'longitude': {
        'output_col': 'longitude',
        'output_rank': 0, 
        'value_map': None
    },
    'latitude': {
        'output_col': 'latitude',
        'output_rank': 0, 
        'value_map': None
    },
}
```

<br>

We can now combine this into a single metadata object for the source

```python
ESAIL_def = {
    'filename': filename,
    'key_input_col': key_input_col,
    'key_output_col': key_output_col,
    'key_map': key_map,
    'attr_cols': attr_cols
}

JSON(ESAIL_def)
```




    <IPython.core.display.JSON object>



<br>

We'll save this source definition before moving on

```python
with open(f'{definitions_dir}/ESAIL.json', 'w') as f:
    json.dump(ESAIL_def, f)
```

<br>

#### GPPDB

```python
# 
```

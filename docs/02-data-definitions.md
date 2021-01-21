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
    'name': 'str',
    'sett_bmu_id': 'str',
    'longitude': 'float',
    'latitude': 'float',
    'capacity_mw': 'float',
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
    ]
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

We'll start by loading the ESAIL dataset in

```python
filename = 'ESAIL.csv'

df_ESAIL = pd.read_csv(f'{raw_data_dir}/{filename}')

df_ESAIL.head()
```




|    | sett_bmu_id   | ngc_bmu_id   | bmu_root   | name                   | primary_fuel_type   | detailed_fuel_type   |   longitude |   latitude | common_name          |
|---:|:--------------|:-------------|:-----------|:-----------------------|:--------------------|:---------------------|------------:|-----------:|:---------------------|
|  0 | E_MARK-1      | MARK-1       | MARK       | Rothes Bio-Plant CHP 1 | biomass             | bone                 |    -3.60352 |    57.4804 | Rothes Bio-Plant CHP |
|  1 | E_MARK-2      | MARK-2       | MARK       | Rothes Bio-Plant CHP 2 | biomass             | bone                 |    -3.60352 |    57.4804 | Rothes Bio-Plant CHP |
|  2 | T_DIDC1       | DIDC1        | DIDC       | Didcot A (G) 1         | coal                | coalgas_opt_out      |    -1.26757 |    51.6236 | Didcot A (G)         |
|  3 | T_DIDC2       | DIDC2        | DIDC       | Didcot A (G) 2         | coal                | coalgas_opt_out      |    -1.26757 |    51.6236 | Didcot A (G)         |
|  4 | T_DIDC4       | DIDC4        | DIDC       | Didcot A (G) 4         | coal                | coalgas_opt_out      |    -1.26757 |    51.6236 | Didcot A (G)         |</div>



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
    'common_name': {
        'output_col': 'name',
        'output_rank': 0, 
        'value_map': None
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
    }
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
filename = 'GPPDB.csv'

df_GPPDB = pd.read_csv(f'{raw_data_dir}/{filename}')

df_GPPDB.head()
```




|    | country   | country_long   | name                                             | gppd_idnr    |   capacity_mw |   latitude |   longitude | primary_fuel   |   other_fuel1 |   other_fuel2 | ...   | geolocation_source   |       wepp_id |   year_of_capacity_data |   generation_gwh_2013 |   generation_gwh_2014 |   generation_gwh_2015 |   generation_gwh_2016 |   generation_gwh_2017 |   generation_data_source |   estimated_generation_gwh |
|---:|:----------|:---------------|:-------------------------------------------------|:-------------|--------------:|-----------:|------------:|:---------------|--------------:|--------------:|:------|:---------------------|--------------:|------------------------:|----------------------:|----------------------:|----------------------:|----------------------:|----------------------:|-------------------------:|---------------------------:|
|  0 | AFG       | Afghanistan    | Kajaki Hydroelectric Power Plant Afghanistan     | GEODB0040538 |            33 |     32.322 |     65.119  | Hydro          |           nan |           nan | ...   | GEODB                |   1.00979e+06 |                    2017 |                   nan |                   nan |                   nan |                   nan |                   nan |                      nan |                        nan |
|  1 | AFG       | Afghanistan    | Kandahar DOG                                     | WKS0070144   |            10 |     31.67  |     65.795  | Solar          |           nan |           nan | ...   | Wiki-Solar           | nan           |                     nan |                   nan |                   nan |                   nan |                   nan |                   nan |                      nan |                        nan |
|  2 | AFG       | Afghanistan    | Kandahar JOL                                     | WKS0071196   |            10 |     31.623 |     65.792  | Solar          |           nan |           nan | ...   | Wiki-Solar           | nan           |                     nan |                   nan |                   nan |                   nan |                   nan |                   nan |                      nan |                        nan |
|  3 | AFG       | Afghanistan    | Mahipar Hydroelectric Power Plant Afghanistan    | GEODB0040541 |            66 |     34.556 |     69.4787 | Hydro          |           nan |           nan | ...   | GEODB                |   1.0098e+06  |                    2017 |                   nan |                   nan |                   nan |                   nan |                   nan |                      nan |                        nan |
|  4 | AFG       | Afghanistan    | Naghlu Dam Hydroelectric Power Plant Afghanistan | GEODB0040534 |           100 |     34.641 |     69.717  | Hydro          |           nan |           nan | ...   | GEODB                |   1.0098e+06  |                    2017 |                   nan |                   nan |                   nan |                   nan |                   nan |                      nan |                        nan |</div>



<br>

First we need to filter this down to plants in the UK.

N.b. the GPPDB uses United Kingdom and GBR interchangeably which is particularly confusing when they're using separate networks - in this work we are currently focusing on GBR only.

```python
df_GPPDB_UK = df_GPPDB.query('country=="GBR"')

print(f'There are {df_GPPDB_UK.shape[0]} power plant entries for the UK')
```

    There are 2603 power plant entries for the UK
    

<br>

Looking at the sources we can see that most of these come from the renewable energy planning database which includes a large number of relatively small plants

```python
df_GPPDB_UK['geolocation_source'].value_counts()
```




    UK Renewable Energy Planning Database    2413
    Wiki-Solar                                 67
    GEODB                                      57
    CARMA                                      50
    GEO                                         9
    WRI                                         7
    Name: geolocation_source, dtype: int64



<br>

Looking at the average capacity of each source makes this clearer

```python
df_GPPDB_UK.groupby(df_GPPDB_UK['geolocation_source'])['capacity_mw'].mean().sort_values(ascending=False)
```




    geolocation_source
    GEODB                                    800.640351
    WRI                                      475.957143
    GEO                                      413.444444
    CARMA                                     50.699000
    UK Renewable Energy Planning Database     13.341912
    Wiki-Solar                                 7.889552
    Name: capacity_mw, dtype: float64



<br>

Sorting by capacity gives us a good basis for selecting which plants to start manually matching ids with

```python
df_GPPDB_UK_focused_sorted = df_GPPDB_UK.sort_values('capacity_mw', ascending=False)[['gppd_idnr', 'name', 'capacity_mw', 'latitude', 'longitude', 'primary_fuel', 'other_fuel1']]

df_GPPDB_UK_focused_sorted.head()
```




|       | gppd_idnr   | name        |   capacity_mw |   latitude |   longitude | primary_fuel   | other_fuel1   |
|------:|:------------|:------------|--------------:|-----------:|------------:|:---------------|:--------------|
| 23794 | GBR1000372  | Pembroke    |          2180 |    51.685  |     -4.99   | Gas            | nan           |
| 24421 | GBR1000143  | West Burton |          2012 |    53.3604 |     -0.8102 | Coal           | nan           |
| 22534 | GBR1000142  | Cottam      |          2008 |    53.304  |     -0.7815 | Coal           | nan           |
| 23888 | GBR1000496  | Ratcliffe   |          2000 |    52.8653 |     -1.255  | Coal           | nan           |
| 22663 | GBR0000174  | Drax        |          1980 |    53.7356 |     -0.9911 | Coal           | Biomass       |</div>



<br>

These were then manually matched to the BMU ids in the ESAIL dataset, confirming matches based on fuel, location and capacity (checked on NETA-Reports)

```python
BMU_root_to_gppd_idnr = {
    'HEYM2': 'GBR1000055', # Heysham 2 - complicated one, need to have HEYM1 and HEYM2 for the BMU root
    'HEYM1': 'GBR1000054', # Heysham 1
    'WHILW1': 'GBR0003489', # WHILW-1, see GBR0003981 for details on separation
    'WHILW2': 'GBR0003981', # This is the extension so should be separated from WHILW-1 like the HEYM group
    'WLNYW1': 'GBR0002500', # WLNYW1
    'WLNYW2': 'GBR0002506', # WLNYW2 - Whilst GPPDB has Walney 1 & 2 it doesnt have the extension included 
    'GNFSW0': 'GBR0002488', # change to GNFSW0
    'GNFSW1': 'GBR0002490', # change to GNFSW1
    'GNFSW2': 'GBR0002489', # change to GNFSW2
    'CRYRW2': 'GBR0003440', # change to CRYRW2 - Crystal Rig Wind Farm - Phase 2
    'CRYRW3': 'GBR0004215', # change to CRYRW3 - Crystal Rig III Wind Farm
    'BLLA1': 'GBR0003116', # change to BLLA1
    'BLLA2': 'GBR0004253', # change to BLLA2
    'WDNSO': 'GBR0002519', # West of Duddon Sands - how to handle OFTO and farm? only WDNSO has data on BMRS
    'THNTO': 'GBR0002499', # could only see FPN for THNTO on BMRS, seems like O is for offtake which is where measurements are made
    'BRYP': 'GBR2000125', # There's also AESB from when it was under AES ownership but no data 
    'CLDW': 'GBR0004178', # The GPPDB only includes the extension at 173 MW but this doesnt match to any of these BMU capacities as shown on netareports - fixed: https://github.com/OSUKED/Power-Station-Dictionary/issues/6
    'PEMB': 'GBR1000372',
    'WBUPS': 'GBR1000143',
    'COTPS': 'GBR1000142',
    'RATS': 'GBR1000496',
    'DRAXX': 'GBR0000174',
    'EGGPS': 'GBR1000147',
    'DINO': 'GBR1000151',
    'STAY': 'GBR1000373',
    'ABTH': 'GBR1000374',
    'DIDCB': 'GBR1000369',
    'GRAI': 'GBR1000495',
    'CNQPS': 'GBR1000492',
    'WBURB': 'GBR1000141',
    'SHBA': 'GBR1000074',
    'HUMR': 'GBR1000517',
    'SCCL': 'GBR2000263',
    'SIZB': 'GBR1000058',
    'TORN': 'GBR1000059',
    'HRTL': 'GBR1000053',
    'PEHEG': 'GBR2000723',
    'DNGB': 'GBR1000052',
    'HUNB': 'GBR1000057',
    'HINB': 'GBR1000056',
    'LAGA': 'GBR1000073',
    'CARR': 'GBR2000124',
    'SPLN': 'GBR0006165',
    'SVRP': 'GBR1000313',
    'MRWD': 'GBR1000311',
    'SUTB': 'GBR2000518',
    'SEAB': 'GBR2000806',
    'ROCK': 'GBR1000212',
    'DAMC': 'GBR1000465',
    'COSO': 'GBR1000211',
    'LBAR': 'GBR1000371',
    'RYHPS': 'GBR1000466',
    'MEDP': 'GBR1000437',
    'LARYW': 'GBR0002511',
    'KILNS': 'GBR1000500',
    'GYMRW': 'GBR0002543',
    'BAGE': 'GBR1000312',
    'DEEP': 'GBR2000262',
    'GRGBW': 'GBR0002510',
    'GYAR': 'GBR1000370',
    'SHOS': 'GBR2000769',
    'SEAB': 'GBR1000480',
    'EECL': 'GBR1000494',
    'CORB': 'GBR1000077',
    'CDCL': 'GBR1000493',
    'FFES': 'GBR1000152',
    'SHRSW': 'GBR0002512',
    'FOYE': 'GBR2000657',
    'RCBKO': 'GBR0002515',
    'LNCSW': 'GBR0002513',
    'BRBEO': 'GBR0002539',
    'PETEM': 'GBR2000128',
    'USKM': 'GBR2000811',
    'PNYCW': 'GBR0004595',
    'HMGTO': 'GBR0002544',
    'WTMSO': 'GBR0002545',
    'GRIFW': 'GBR0004028',
    'FELL': 'GBR1000317',
    'SLOY': 'GBR1000404',
    'BRGG': 'GBR2000126',
    'OMNDW': 'GBR0002509',
    'FALGW': 'GBR0004059',
    'TAYLG': 'GBR1000499',
    'INDQ': 'GBR1000150',
    'COWE': 'GBR1000376',
    'HRSTW': 'GBR0004119',
    'ARCHW': 'GBR0003258',
    'HADHW': 'GBR0003109',
    'BHLAW': 'GBR0004640',
    'DIDCG': 'GBR1000377',
    'GLNDO': 'GBR0000388',
    'FARR': 'GBR0004676',
    'BOWLW': 'GBR0002546',
    'RREW': 'GBR0002496',
    'RRWW': 'GBR0002497',
    'BURBO': 'GBR0002487',
    'BEINW': 'GBR0003787',
    'FERRG': 'GBR0000116',
    'PSTAT002': 'GBR0004627',
    'DRAXXG': 'GBR1000112',
    'BRDUW': 'GBR0003119',
    'GORDW': 'GBR0003662',
    'CGTHW': 'GBR0004664',
    'LCLTW': 'GBR0004123',
    'DRSLW': 'GBR0004269',
    'STRNW': 'GBR0004625',
    'KILBW': 'GBR0002673',
    'BRYBW': 'GBR0004261',
    'GLWSW': 'GBR0004368',
    'MILWW': 'GBR0002723',
    'PPGEN002': 'GBR0004687',
    'TESI': 'GBR0002514',
    'WISTW': 'GBR0004431',
    'CASCLU': 'GBR1000405',
    'AKGLW': 'GBR0004332',
    'MOYEW': 'GBR0003647',
    'PSTAT002': 'GBR0004667',
    'GRAIG': 'GBR1000497',
    'DPGEN001': 'GBR1000114',
    'MKHLW': 'GBR0003260',
    'MPGEN002': 'GBR1000113',
    'RHEI': 'GBR0003552',
    'BABAW': 'GBR0004021',
    'HBHDW': 'GBR0004225',
    'ABTHG': 'GBR1000375',
    'PPGEN001': 'GBR0003534',
    'PSTAT001': 'GBR0003951',
    'MPGEN001': 'GBR1000115',
    'PPGEN003': 'GBR0004006',
    'HLTWW': 'GBR0004014',
    'KILBW': 'GBR0003202',
    'CRMLW': 'GBR0004120',
    'CRGHW': 'GBR0004619',
    'BTUIW': 'GBR0004525',
    'ACHRW': 'GBR0004331',
    'PPGEN001': 'GBR0003534',
    'EDINW': 'GBR0004674',
    'CLAC': 'GBR1000401',
    'WBUGT': 'GBR1000146',
    'MILWW': 'GBR0004682',
    'MINSW': 'GBR0004517',
    'CLDRW': 'GBR0004623',
}
```

<br>

We'll now convert the mapping from BMU id to GPPDB id into one from osuked id to GPPDB id

```python
key_map = {
    k: BMU_root_to_gppd_idnr[v] 
    for k, v 
    in ESAIL_def['key_map'].items() 
    if v 
    in BMU_root_to_gppd_idnr.keys()
}

assert len(key_map) == len(BMU_root_to_gppd_idnr), 'Not all of the GPPDB ids matched to BMU ids were mapped to osuked ids'
```

```python
key_input_col = 'gppd_idnr'
key_output_col = 'gppd_idnr'

attr_cols = {
    'capacity_mw': {
        'output_col': 'capacity_mw',
        'output_rank': 0,
        'value_map': None
    }
}
```

<br>

We'll now combine this into a single metadata object

```python
GPPDB_def = {
    'filename': filename,
    'key_input_col': key_input_col,
    'key_output_col': key_output_col,
    'key_map': key_map,
    'attr_cols': attr_cols
}

JSON(GPPDB_def)
```




    <IPython.core.display.JSON object>



<br>

And finally save the source definition

```python
with open(f'{definitions_dir}/GPPDB.json', 'w') as f:
    json.dump(GPPDB_def, f)
```

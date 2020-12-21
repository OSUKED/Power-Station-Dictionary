# Database Construction



```python
#exports
import json
import pandas as pd

import os
from warnings import warn
```

```python
from IPython.display import JSON
```

<br>

### User Inputs

```python
raw_data_dir = '../data/raw'
definitions_dir = '../data/definitions'
intermediate_data_dir = '../data/intermediate'
```

<br>

### Constructing the Database

We'll begin by loading in and combining the definitions of each source

```python
#exports
def load_source_definitions(definitions_dir):
    source_definitions = dict()
    source_def_filenames = [f for f in os.listdir(definitions_dir) if '.json' in f and f != 'outputs.json']

    for filename in source_def_filenames:
        source_name = filename.replace('.json', '')

        with open(f'{definitions_dir}/{filename}', 'r') as f:
            source_definitions[source_name] = json.load(f)
            
    return source_definitions
```

```python
source_definitions = load_source_definitions(definitions_dir)
        
JSON(source_definitions)
```




    <IPython.core.display.JSON object>



```python
#exports
def identify_primary_keys(source_definitions):
    primary_keys = []

    for source in source_definitions.values():
        primary_keys += list(source['key_map'].keys())

    primary_keys = sorted(set(primary_keys))
    
    return primary_keys
```

```python
primary_keys = identify_primary_keys(source_definitions)
    
primary_keys[:5]
```




    ['10000', '10001', '10002', '10003', '10004']



```python
#exports
def check_source_for_disallowed_cols(attr_cols, outputs):
    output_cols_to_be_added = [attr_col['output_col'] for attr_col in attr_cols.values()]
    output_cols_allowed = outputs.keys()

    disallowed_output_cols = list(set(output_cols_to_be_added) - set(output_cols_allowed))

    assert len(disallowed_output_cols)==0, f"The following columns are not allowed in the output dataset: {', '.join(disallowed_output_cols)}"
    
def check_sources_for_disallowed_cols(source_definitions, definitions_dir):
    with open(f'{definitions_dir}/outputs.json', 'r') as f:
        outputs = json.load(f)
    
    for source, definition in source_definitions.items():
        check_source_for_disallowed_cols(definition['attr_cols'], outputs)
        
    return
```

```python
check_sources_for_disallowed_cols(source_definitions, definitions_dir)
```

```python
#exports
def identify_inputs_for_output_cols(source_definitions):
    keys_to_keep = ['output_col', 'output_rank']
    output_cols = list()
    inputs_for_output_cols = dict()
    
    for source, definition in source_definitions.items():
        for input_col, value in definition['attr_cols'].items():
            output_cols += [(source, input_col, value['output_col'], value['output_rank'])]
            
    df_output_cols = pd.DataFrame(output_cols, columns=['source', 'input_col', 'output_col', 'output_rank'])
    
    for output_col in df_output_cols['output_col']:
        inputs_for_output_cols[output_col] = (df_output_cols
                                              .query('`output_col`==@output_col')
                                              .sort_values('output_rank', ascending=False)
                                              [['source', 'input_col']]
                                              .apply(tuple, axis=1)
                                              .to_list()
                                             )
    return inputs_for_output_cols
```

```python
inputs_for_output_cols = identify_inputs_for_output_cols(source_definitions)

JSON(inputs_for_output_cols)
```




    <IPython.core.display.JSON object>



```python
pd.read_csv('https://raw.githubusercontent.com/OSUKED/Power-Station-Dictionary/main/data/output/power_stations.csv')
```




|     | osuked_id   | esail_id   | gppd_idnr   | name                 | sett_bmu_id                                       | longitude   | latitude   | fuel_type     | capacity_mw   |
|:----|:------------|:-----------|:------------|:---------------------|:--------------------------------------------------|:------------|:-----------|:--------------|:--------------|
| 0   | 10000       | MARK       | nan         | Rothes Bio-Plant CHP | E_MARK-1, E_MARK-2                                | -3.603516   | 57.480403  | biomass       | nan           |
| 1   | 10001       | DIDC       | nan         | Didcot A (G)         | T_DIDC1, T_DIDC2, T_DIDC4, T_DIDC3                | -1.267570   | 51.623630  | coal          | nan           |
| 2   | 10002       | ABTH       | GBR1000374  | Aberthaw B           | T_ABTH7, T_ABTH8, T_ABTH9                         | -3.404866   | 51.387312  | coal          | 1586.0        |
| 3   | 10003       | COTPS      | GBR1000142  | Cottam               | T_COTPS-1, T_COTPS-2, T_COTPS-3, T_COTPS-4        | -0.648193   | 53.245495  | coal          | 2008.0        |
| 4   | 10004       | DRAXX      | GBR0000174  | Drax                 | T_DRAXX-1, T_DRAXX-2, T_DRAXX-3, T_DRAXX-4, T_... | -0.626221   | 53.748711  | coal, biomass | 1980.0        |
| ... | ...         | ...        | ...         | ...                  | ...                                               | ...         | ...        | ...           | ...           |
| 285 | 10285       | ROOSB      | nan         | nan                  | E_ROOSB-1                                         | nan         | nan        | other         | nan           |
| 286 | 10286       | STLGW      | nan         | Stronelairg Windfarm | T_STLGW-1, T_STLGW-2                              | -4.461346   | 57.099869  | wind          | nan           |
| 287 | 10287       | TDRVE      | nan         | nan                  | E_TDRVE-1                                         | nan         | nan        | gas           | nan           |
| 288 | 10288       | TRFPK      | nan         | nan                  | E_TRFPK-1                                         | nan         | nan        | gas           | nan           |
| 289 | 10289       | WTRLN      | nan         | nan                  | E_WTRLN-1                                         | nan         | nan        | gas           | nan           |</div>



```python
#exports
def get_input_key_to_attr(df_input, key_input_col, input_col):
    df_key_input_non_duped = df_input[[key_input_col, input_col]].drop_duplicates()

    one_to_many_input_keys = list(df_key_input_non_duped
                                  [df_key_input_non_duped[key_input_col].duplicated(keep=False)]
                                  .sort_values(key_input_col)
                                  [key_input_col]
                                  .unique()
                                 )

    warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")

    # Creating one-to-one mapping
    input_key_to_attr = (df_key_input_non_duped
                         [~df_key_input_non_duped[key_input_col].isin(one_to_many_input_keys)]
                         .set_index(key_input_col)
                         [input_col]
                         .to_dict()
                        )
    
    # Creating one-to-many mapping
    for input_key in one_to_many_input_keys:
        many_inputs = (df_key_input_non_duped
                       .query(f'{key_input_col}=="{input_key}"')
                       [input_col]
                       .to_list()
                      )

        input_key_to_attr[input_key] = ', '.join([str(elem) for elem in many_inputs])
    
    return input_key_to_attr
```

```python
source = 'ESAIL'
key_input_col = 'bmu_root'
input_col = 'primary_fuel_type'
filename = 'ESAIL.csv'

df_input = pd.read_csv(f"{raw_data_dir}/{filename}")
input_key_to_attr = get_input_key_to_attr(df_input, key_input_col, input_col)

JSON([input_key_to_attr])
```

    <ipython-input-13-ea4c39131cdc>:12: UserWarning: The following bmu_root input keys were not unique w.r.t. primary_fuel_type, a one to many relationship will therefore be used: FAWLG, GRAI
    
      warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")
    




    <IPython.core.display.JSON object>



```python
#exports
def get_primary_key_to_attr(source, input_col, source_definitions, raw_data_dir):
    filename = source_definitions[source]['filename']
    key_input_col = source_definitions[source]['key_input_col']
    key_map = source_definitions[source]['key_map']
    value_map = source_definitions[source]['attr_cols'][input_col]['value_map']
    
    df_input = pd.read_csv(f"{raw_data_dir}/{filename}")
    
    if value_map is not None:
        assert df_input[input_col].isin(value_map.keys()).mean()==1, f'A mapping was provided for {input_col} but did not contain all of the values found within it'
        df_input[input_col] = df_input[input_col].map(value_map)
    
    input_key_to_attr = get_input_key_to_attr(df_input, key_input_col, input_col)

    primary_key_to_attr = (pd.Series(key_map)
                           .map(input_key_to_attr)
                           .dropna()
                           .to_dict())
    
    return primary_key_to_attr
```

```python
source = 'ESAIL'
input_col = 'primary_fuel_type'

primary_key_to_attr = get_primary_key_to_attr(source, input_col, source_definitions, raw_data_dir)

JSON([primary_key_to_attr])
```

    <ipython-input-13-ea4c39131cdc>:12: UserWarning: The following bmu_root input keys were not unique w.r.t. primary_fuel_type, a one to many relationship will therefore be used: FAWLG, GRAI
    
      warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")
    




    <IPython.core.display.JSON object>



```python
#exports
def update_df_col(df, update_col, update_dict):
    s_update = pd.Series(df.index.map(update_dict), df.index).dropna()
    df.loc[s_update.index, update_col] = s_update.values

    return df

def add_attr_cols(df, source_definitions, raw_data_dir):
    inputs_for_output_cols = identify_inputs_for_output_cols(source_definitions)
    
    for output_col, inputs in inputs_for_output_cols.items():
        for (source, input_col) in inputs:
            primary_key_to_attr = get_primary_key_to_attr(source, input_col, source_definitions, raw_data_dir)
            df = update_df_col(df, output_col, primary_key_to_attr)
            
    return df
```

```python
df = pd.DataFrame(index=primary_keys)
df = add_attr_cols(df, source_definitions, raw_data_dir)

df.head()
```

    <ipython-input-13-ea4c39131cdc>:12: UserWarning: The following bmu_root input keys were not unique w.r.t. common_name, a one to many relationship will therefore be used: 
    
      warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")
    <ipython-input-13-ea4c39131cdc>:12: UserWarning: The following bmu_root input keys were not unique w.r.t. sett_bmu_id, a one to many relationship will therefore be used: ABTH, ABTHG, BAGE, BANGE, BRWE, CARR, CNQPS, COCK, COTPS, COWE, CRUA, DDGNO, DIDC, DIDCB, DIDCG, DINO, DNGB, DRAXX, DRAXXG, DRKPS, DUNG, EGGPS, ERRO, FARR, FASN, FAWL, FAWLG, FERR, FERRG, FFES, FIDL, FIDLG, FIFO, FOYE, GANGE, GANW, GNFSW1, GNFSW2, GRAI, GRAIG, GRGBW, GRIFW, GYMR, GYMRW, HEYM1, HEYM2, HINB, HMGTO, HMRPS, HRTL, HUNB, IRNPS, KILLPG, KINO, KINOG, LARYW, LITTD, LITTDG, LNCSW, LOAN, LYNE, MARK, OLDS, OMNDW, PEHE, PEHEG, PEMB, RATS, RATSGT, RCBKO, RHEI, RMPNO, RUGGT, RUGPS, SCCL, SEAB, SHBA, SHRSW, SIZB, SIZEA, SLOY, STAY, STLGW, SVRP, TAYLG, TESI, THNTO, THNTW, TILB, TILBG, TORN, TULWW, USKM, WBUGT, WBUPS, WBURB, WDNSO, WDNSW, WLNYO, WYLF
    
      warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")
    <ipython-input-13-ea4c39131cdc>:12: UserWarning: The following bmu_root input keys were not unique w.r.t. longitude, a one to many relationship will therefore be used: 
    
      warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")
    <ipython-input-13-ea4c39131cdc>:12: UserWarning: The following bmu_root input keys were not unique w.r.t. latitude, a one to many relationship will therefore be used: 
    
      warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")
    <ipython-input-13-ea4c39131cdc>:12: UserWarning: The following bmu_root input keys were not unique w.r.t. primary_fuel_type, a one to many relationship will therefore be used: FAWLG, GRAI
    
      warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")
    <ipython-input-13-ea4c39131cdc>:12: UserWarning: The following gppd_idnr input keys were not unique w.r.t. capacity_mw, a one to many relationship will therefore be used: 
    
      warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")
    




|       | name                 | sett_bmu_id                                       |   longitude |   latitude | fuel_type   |   capacity_mw |
|------:|:---------------------|:--------------------------------------------------|------------:|-----------:|:------------|--------------:|
| 10000 | Rothes Bio-Plant CHP | E_MARK-1, E_MARK-2                                |   -3.60352  |    57.4804 | biomass     |           nan |
| 10001 | Didcot A (G)         | T_DIDC1, T_DIDC2, T_DIDC4, T_DIDC3                |   -1.26757  |    51.6236 | coal        |           nan |
| 10002 | Aberthaw B           | T_ABTH7, T_ABTH8, T_ABTH9                         |   -3.40487  |    51.3873 | coal        |          1586 |
| 10003 | Cottam               | T_COTPS-1, T_COTPS-2, T_COTPS-3, T_COTPS-4        |   -0.648193 |    53.2455 | coal        |          2008 |
| 10004 | Drax                 | T_DRAXX-1, T_DRAXX-2, T_DRAXX-3, T_DRAXX-4, T_... |   -0.626221 |    53.7487 | coal        |          1980 |</div>



```python
#exports
def add_key_cols(df, source_definitions):
    for source in source_definitions.keys():
        key_map = source_definitions[source]['key_map']
        key_output_col = source_definitions[source]['key_output_col']
        df = update_df_col(df, key_output_col, key_map)
        
    return df
```

```python
df = pd.DataFrame(index=primary_keys)
df = add_key_cols(df, source_definitions)

df.head()
```




|       | esail_id   | gppd_idnr   |
|------:|:-----------|:------------|
| 10000 | MARK       | nan         |
| 10001 | DIDC       | nan         |
| 10002 | ABTH       | GBR1000374  |
| 10003 | COTPS      | GBR1000142  |
| 10004 | DRAXX      | GBR0000174  |</div>



```python
#exports
def construct_output_df(definitions_dir, raw_data_dir):
    source_definitions = load_source_definitions(definitions_dir)
    primary_keys = identify_primary_keys(source_definitions)
    
    df = (pd.DataFrame(index=primary_keys)
          .pipe(add_key_cols, source_definitions)
          .pipe(add_attr_cols, source_definitions, raw_data_dir)
         )
    
    df.index.name = 'osuked_id'
    
    return df
```

```python
df = construct_output_df(definitions_dir, raw_data_dir)

df.head()
```

    <ipython-input-13-ea4c39131cdc>:12: UserWarning: The following bmu_root input keys were not unique w.r.t. common_name, a one to many relationship will therefore be used: 
    
      warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")
    <ipython-input-13-ea4c39131cdc>:12: UserWarning: The following bmu_root input keys were not unique w.r.t. sett_bmu_id, a one to many relationship will therefore be used: ABTH, ABTHG, BAGE, BANGE, BRWE, CARR, CNQPS, COCK, COTPS, COWE, CRUA, DDGNO, DIDC, DIDCB, DIDCG, DINO, DNGB, DRAXX, DRAXXG, DRKPS, DUNG, EGGPS, ERRO, FARR, FASN, FAWL, FAWLG, FERR, FERRG, FFES, FIDL, FIDLG, FIFO, FOYE, GANGE, GANW, GNFSW1, GNFSW2, GRAI, GRAIG, GRGBW, GRIFW, GYMR, GYMRW, HEYM1, HEYM2, HINB, HMGTO, HMRPS, HRTL, HUNB, IRNPS, KILLPG, KINO, KINOG, LARYW, LITTD, LITTDG, LNCSW, LOAN, LYNE, MARK, OLDS, OMNDW, PEHE, PEHEG, PEMB, RATS, RATSGT, RCBKO, RHEI, RMPNO, RUGGT, RUGPS, SCCL, SEAB, SHBA, SHRSW, SIZB, SIZEA, SLOY, STAY, STLGW, SVRP, TAYLG, TESI, THNTO, THNTW, TILB, TILBG, TORN, TULWW, USKM, WBUGT, WBUPS, WBURB, WDNSO, WDNSW, WLNYO, WYLF
    
      warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")
    <ipython-input-13-ea4c39131cdc>:12: UserWarning: The following bmu_root input keys were not unique w.r.t. longitude, a one to many relationship will therefore be used: 
    
      warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")
    <ipython-input-13-ea4c39131cdc>:12: UserWarning: The following bmu_root input keys were not unique w.r.t. latitude, a one to many relationship will therefore be used: 
    
      warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")
    <ipython-input-13-ea4c39131cdc>:12: UserWarning: The following bmu_root input keys were not unique w.r.t. primary_fuel_type, a one to many relationship will therefore be used: FAWLG, GRAI
    
      warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")
    <ipython-input-13-ea4c39131cdc>:12: UserWarning: The following gppd_idnr input keys were not unique w.r.t. capacity_mw, a one to many relationship will therefore be used: 
    
      warn(f"The following {key_input_col} input keys were not unique w.r.t. {input_col}, a one to many relationship will therefore be used: {', '.join(one_to_many_input_keys)}\n")
    




|   ('Unnamed: 0_level_0', 'osuked_id') | ('esail_id', 'Unnamed: 1_level_1')   | ('gppd_idnr', 'Unnamed: 2_level_1')   | ('name', 'Unnamed: 3_level_1')   | ('sett_bmu_id', 'Unnamed: 4_level_1')             |   ('longitude', 'Unnamed: 5_level_1') |   ('latitude', 'Unnamed: 6_level_1') | ('fuel_type', 'Unnamed: 7_level_1')   |   ('capacity_mw', 'Unnamed: 8_level_1') |
|--------------------------------------:|:-------------------------------------|:--------------------------------------|:---------------------------------|:--------------------------------------------------|--------------------------------------:|-------------------------------------:|:--------------------------------------|----------------------------------------:|
|                                 10000 | MARK                                 | nan                                   | Rothes Bio-Plant CHP             | E_MARK-1, E_MARK-2                                |                             -3.60352  |                              57.4804 | biomass                               |                                     nan |
|                                 10001 | DIDC                                 | nan                                   | Didcot A (G)                     | T_DIDC1, T_DIDC2, T_DIDC4, T_DIDC3                |                             -1.26757  |                              51.6236 | coal                                  |                                     nan |
|                                 10002 | ABTH                                 | GBR1000374                            | Aberthaw B                       | T_ABTH7, T_ABTH8, T_ABTH9                         |                             -3.40487  |                              51.3873 | coal                                  |                                    1586 |
|                                 10003 | COTPS                                | GBR1000142                            | Cottam                           | T_COTPS-1, T_COTPS-2, T_COTPS-3, T_COTPS-4        |                             -0.648193 |                              53.2455 | coal                                  |                                    2008 |
|                                 10004 | DRAXX                                | GBR0000174                            | Drax                             | T_DRAXX-1, T_DRAXX-2, T_DRAXX-3, T_DRAXX-4, T_... |                             -0.626221 |                              53.7487 | coal                                  |                                    1980 |</div>



```python
df.to_csv(f'{intermediate_data_dir}/power_stations.csv')
```

# Dataset Generation



<br>

### Sources



<br>

### Input/Output Definitions

```json
{
    "filename": "GPPDB.csv", 
    "key_input_col": "gppd_idnr", 
    "key_output_col": "gppd_idnr", 
    "key_map": {
        "10002": "GBR1000374", 
        "10003": "GBR1000142", 
        ...
        "10004": "GBR0000174", 
        "10005": "GBR1000147"
    }, 
    "attr_cols": {
        "capacity_mw": {
            "output_col": "capacity_mw", 
            "output_rank": 0, 
            "value_map": null
        }
    }
}
```

```json
{
    "name": "str", 
    "sett_bmu_id": "str", 
    "longitude": "float", 
    "latitude": "float", 
    "capacity_mw": "float", 
    "fuel_type": ["gas", "coal", "wind", ... , "biomass", "other"], 
    "plant_type": ["ccgt", "ocgt", "coal", ... , "battery", "biomass"]
}
```


<br>

### Updates/Corrections

A collection of JSON files are stored within the `data/updates` directory, each one relating to a specific attribute column in the output dataset. Each file contains a mapping between the osuked_id of the plant to a key/value set of metadata which must contain `new_value` and `md_description` keys. Below we have included a sample from the `fuel_type.json` update file.

```json
{
    "10004": {
        "new_value": "coal, biomass",
        "md_description": "Drax is currently converting its coal units to biomass before the 2024 coal ban - [evidence](https://www.drax.com/press_release/drax-closer-coal-free-future-fourth-biomass-unit-conversion/)"
    }
}
```

<br>

### Construction Steps

1. Download the latest versions of the external datasets
2. Load the JSON source definitions and identify which of their columns will be used for key matching and which will be used for populating the power plant attributes 
3. For each of the output columns rank their input sources as specified in the source definitions
4. Iterating over each of the output columns the lowest rank input is used to populate the DB first, with subsequent higher rank input sources overwriting earlier ones when they overlap 
5. The JSON files specifying corrections/updates are then loaded in and applied to each output column in turn
6. Finally the generated dataset is saved as a csv

Whilst the mapping between the `osuked_id` and source id keys must be one-to-one, the mapping between source id keys and attributes can be one-to-one, one-to-many, or many-to-one.
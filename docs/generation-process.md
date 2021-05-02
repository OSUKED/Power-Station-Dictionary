# Dataset Generation

<br>

### Sources



<br>

### Input/Output Definitions

Each of the source datasets has a matching input specification file stored under `data/definitions`. The specification is stored in a JSON format and contains the following key:value pairs.

* filename: name of the source csv file (stored under `data/raw`)
* key_input_col: the name of the column in the source file that contains the ids that will be used to join the source to the dictionary
* key_output_col: the name of the column in the output dictionary that will contain the relevant source ids
* key_map: a mapping from the unique `osuked_id` to the relevant source id
* attr_cols: a description of how to programmatically add the specified attribute columns to the output dictionary, including its name, rank (0 has higher priority), and value_map to be used if some of the values are to be standardised into another form

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

<br>

As well as having JSON specifications for the inputs, we employ a similar approach with the outputs. The `outputs.json` file specifies the datatypes of the output columns, and in the case of categorical data fields can be used to ensure that only expected categories are returned.

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

### Dictionary Generation Pipeline

The following steps described the automated pipeline that constructs the power station dictionary, this is run automatically whenever changes are pushed to the repository.

1. Download the latest versions of the external datasets
2. Load the JSON source definitions and identify which of their columns will be used for key matching and which will be used for populating the power plant attributes 
3. For each of the output columns rank their input sources as specified in the source definitions
4. Iterating over each of the output columns the lowest rank input is used to populate the DB first, with subsequent higher rank input sources overwriting earlier ones when they overlap 
5. The JSON files specifying corrections/updates are then loaded in and applied to each output column in turn
6. Finally the generated dataset is saved as a csv

N.b. Whilst the mapping between the `osuked_id` and source id keys must be one-to-one, the mapping between source id keys and attributes can be one-to-one, one-to-many, or many-to-one.
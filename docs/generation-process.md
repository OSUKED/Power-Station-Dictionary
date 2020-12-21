# Dataset Generation



<br>

### Sources



<br>

### Input/Output Definitions



<br>

### Updates/Corrections



<br>

### Construction Steps

1. Download the latest versions of the external datasets
2. Load the JSON source definitions and identify which of their columns will be used for key matching and which will be used for populating the power plant attributes 
3. For each of the output columns rank their input sources as specified in the source definitions
4. Iterating over each of the output columns the lowest rank input is used to populate the DB first, with subsequent higher rank input sources overwriting earlier ones when they overlap 
5. The JSON files specifying corrections/updates are then loaded in and applied to each output column in turn
6. Finally the generated dataset is saved as a csv

Whilst the mapping between the `osuked_id` and source id keys must be one-to-one, the mapping between source id keys and attributes can be one-to-one, one-to-many, or many-to-one.
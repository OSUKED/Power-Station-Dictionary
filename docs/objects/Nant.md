### Identifiers

| Relationship   | ID Type     | ID(s)    |
|:---------------|:------------|:---------|
| root           | osuked_id   | 10123    |
| element-of     | sett_bmu_id | T_NANT-1 |
| element-of     | ngc_bmu_id  | NANT-1   |
| same-as        | esail_id    | NANT     |
| same-as        | name        | Nant     |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -5.25 |
| Latitude    |   56.16 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    Value |
|:--------------------|-------:|---------:|
| Annual Output (MWh) |   2016 | 36184.76 |
| Annual Output (MWh) |   2017 | 36905.75 |
| Annual Output (MWh) |   2018 | 36755.70 |
| Annual Output (MWh) |   2019 | 34432.37 |
| Annual Output (MWh) |   2020 | 45295.67 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | NPSHYD  |

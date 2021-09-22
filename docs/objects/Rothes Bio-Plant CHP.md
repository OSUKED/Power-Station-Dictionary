### Identifiers

| Relationship   | ID Type     | ID(s)                |
|:---------------|:------------|:---------------------|
| root           | osuked_id   | 10000                |
| element-of     | sett_bmu_id | E_MARK-1, E_MARK-2   |
| element-of     | ngc_bmu_id  | MARK-1, MARK-2       |
| same-as        | esail_id    | MARK                 |
| same-as        | name        | Rothes Bio-Plant CHP |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.60 |
| Latitude    |   57.48 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     Value |
|:--------------------|-------:|----------:|
| Annual Output (MWh) |   2016 | 355704.93 |
| Annual Output (MWh) |   2017 | 387311.36 |
| Annual Output (MWh) |   2018 | 295847.59 |
| Annual Output (MWh) |   2019 | 389670.23 |
| Annual Output (MWh) |   2020 | 347661.62 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | BIOMASS |

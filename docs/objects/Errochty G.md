### Identifiers

| Relationship   | ID Type     | ID(s)                        |
|:---------------|:------------|:-----------------------------|
| root           | osuked_id   | 10115                        |
| element-of     | sett_bmu_id | T_ERRO-1, T_ERRO-2, T_ERRO-3 |
| element-of     | ngc_bmu_id  | ERRO-1, ERRO-2, ERRO-3       |
| same-as        | esail_id    | ERRO                         |
| same-as        | name        | Errochty G                   |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.79 |
| Latitude    |   56.73 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   ERRO-1 |   ERRO-2 |   ERRO-3 |
|:--------------------|-------:|---------:|---------:|---------:|
| Annual Output (MWh) |   2016 | 32304.97 | 19178.85 | 41301.73 |
| Annual Output (MWh) |   2017 | 41242.56 |   881.61 | 39118.14 |
| Annual Output (MWh) |   2018 | 25336.81 | 16830.54 | 27133.03 |
| Annual Output (MWh) |   2019 | 32969.14 | 28239.16 | 34927.63 |
| Annual Output (MWh) |   2020 | 41495.31 | 41134.97 | 38918.45 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | ERRO-1   | ERRO-2   | ERRO-3   |
|:------------|:---------|:---------|:---------|
| Fuel Type   | NPSHYD   | NPSHYD   | NPSHYD   |

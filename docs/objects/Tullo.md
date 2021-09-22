### Identifiers

| Relationship   | ID Type     | ID(s)                |
|:---------------|:------------|:---------------------|
| root           | osuked_id   | 10244                |
| element-of     | sett_bmu_id | E_TULWW-1, E_TULWW-2 |
| element-of     | ngc_bmu_id  | TULWW-1, TULWW-2     |
| same-as        | esail_id    | TULWW                |
| same-as        | name        | Tullo                |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -2.58 |
| Latitude    |   56.66 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Plant Type  | onshore |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   TULWW-1 |   TULWW-2 |
|:--------------------|-------:|----------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |  51340.39 |
| Annual Output (MWh) |   2017 |      0.00 |  50495.11 |
| Annual Output (MWh) |   2018 |      0.00 |  50399.73 |
| Annual Output (MWh) |   2019 |  34950.26 |  47009.29 |
| Annual Output (MWh) |   2020 |  35661.43 |  47615.80 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | TULWW-1   | TULWW-2   |
|:------------|:----------|:----------|
| Fuel Type   | WIND      | WIND      |

### Identifiers

| Relationship   | ID Type     | ID(s)                                  |
|:---------------|:------------|:---------------------------------------|
| root           | osuked_id   | 10143                                  |
| element-of     | sett_bmu_id | T_CRUA-1, T_CRUA-2, T_CRUA-3, T_CRUA-4 |
| element-of     | ngc_bmu_id  | CRUA-1, CRUA-2, CRUA-3, CRUA-4         |
| same-as        | esail_id    | CRUA                                   |
| same-as        | name        | Crauchan                               |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -5.22 |
| Latitude    |   56.37 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    CRUA-1 |    CRUA-2 |   CRUA-3 |   CRUA-4 |
|:--------------------|-------:|----------:|----------:|---------:|---------:|
| Annual Output (MWh) |   2016 |  94772.20 | 129230.96 | 22636.54 | 24691.62 |
| Annual Output (MWh) |   2017 |  95151.14 |  96342.94 | 30147.40 | 34270.94 |
| Annual Output (MWh) |   2018 | 114202.20 |  74677.38 |  9183.86 | 33938.50 |
| Annual Output (MWh) |   2019 |  94098.06 |  73404.10 | 25189.48 | 44980.04 |
| Annual Output (MWh) |   2020 | 114757.34 |  89555.32 | 21139.44 | 45380.08 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | CRUA-1   | CRUA-2   | CRUA-3   | CRUA-4   |
|:------------|:---------|:---------|:---------|:---------|
| Fuel Type   | PS       | PS       | PS       | PS       |

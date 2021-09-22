### Identifiers

| Relationship   | ID Type     | ID(s)                                                      |
|:---------------|:------------|:-----------------------------------------------------------|
| root           | osuked_id   | 10116                                                      |
| element-of     | sett_bmu_id | T_FASN-1, E_FASN-2, T_FASN-2, E_FASN-3, T_FASN-3, E_FASN-4 |
| element-of     | ngc_bmu_id  | FASN-1, FASN2, FASN3, FASN-4                               |
| same-as        | esail_id    | FASN                                                       |
| same-as        | name        | Fasnakyle G                                                |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -4.79 |
| Latitude    |   57.33 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    FASN-1 |   FASN-4 |    FASN2 |    FASN3 |
|:--------------------|-------:|----------:|---------:|---------:|---------:|
| Annual Output (MWh) |   2016 |  60338.92 | 64279.70 | 70583.88 | 49291.54 |
| Annual Output (MWh) |   2017 |  70610.31 | 41704.76 | 63872.53 | 71229.01 |
| Annual Output (MWh) |   2018 |  67672.39 | 61914.88 | 60833.52 | 41040.77 |
| Annual Output (MWh) |   2019 |  95855.12 | 64608.71 | 78198.05 | 28781.94 |
| Annual Output (MWh) |   2020 | 107850.12 | 63792.19 | 85808.69 | 55368.61 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | FASN-1   | FASN-4   | FASN2   | FASN3   |
|:------------|:---------|:---------|:--------|:--------|
| Fuel Type   | NPSHYD   | NPSHYD   | NPSHYD  | NPSHYD  |

### Identifiers

| Relationship   | ID Type     | ID(s)                           |
|:---------------|:------------|:--------------------------------|
| root           | osuked_id   | 10284                           |
| element-of     | sett_bmu_id | T_STLGW-1, T_STLGW-2, T_STLGW-3 |
| element-of     | ngc_bmu_id  | STLGW-1, STLGW-2, STLGW-3       |
| same-as        | esail_id    | STLGW                           |
| same-as        | name        | Stronelairg Windfarm            |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -4.46 |
| Latitude    |   57.10 |

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

| Attribute           |   Year |   STLGW-1 |   STLGW-2 |   STLGW-3 |
|:--------------------|-------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2017 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2018 | 102275.17 | 133101.72 |  56571.37 |
| Annual Output (MWh) |   2019 | 183012.61 | 214292.86 | 191655.30 |
| Annual Output (MWh) |   2020 | 139656.07 | 158080.54 | 138744.35 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | STLGW-1   | STLGW-2   | STLGW-3   |
|:------------|:----------|:----------|:----------|
| Fuel Type   | WIND      | WIND      | WIND      |

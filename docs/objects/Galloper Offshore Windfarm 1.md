### Identifiers

| Relationship   | ID Type             | ID(s)                                      |
|:---------------|:--------------------|:-------------------------------------------|
| root           | osuked_id           | 10194                                      |
| element-of     | sett_bmu_id         | T_GANW-11, T_GANW-13, T_GANW-22, T_GANW-24 |
| element-of     | ngc_bmu_id          | GAOFO-1, GAOFO-3, GAOFO-2, GAOFO-4         |
| same-as        | esail_id            | GANW                                       |
| same-as        | name                | Galloper Offshore Windfarm 1               |
| same-as        | 4c_offshore_id      | galloper-united-kingdom-uk62               |
| same-as        | windpowernet_id     | windfarm_en_16770_galloper                 |
| same-as        | wikidata_id         | Q56026054                                  |
| same-as        | power_technology_id | galloper-offshore-wind-farm                |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    2.04 |
| Latitude    |   51.89 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 88.0     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   GAOFO-1 |   GAOFO-2 |   GAOFO-3 |   GAOFO-4 |
|:--------------------|-------:|----------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2017 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2018 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2019 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2020 | 124611.95 | 124803.32 | 123607.07 | 121803.71 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | GAOFO-1   | GAOFO-2   | GAOFO-3   | GAOFO-4   |
|:------------|:----------|:----------|:----------|:----------|
| Fuel Type   | WIND      | WIND      | WIND      | WIND      |

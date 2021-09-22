### Identifiers

| Relationship   | ID Type             | ID(s)                                         |
|:---------------|:--------------------|:----------------------------------------------|
| root           | osuked_id           | 10234                                         |
| element-of     | sett_bmu_id         | T_RMPNO-1, T_RMPNO-2                          |
| element-of     | ngc_bmu_id          | RMPNO-1, RMPNO-2                              |
| same-as        | esail_id            | RMPNO                                         |
| same-as        | name                | Rampion Offshore Windfarm                     |
| same-as        | 4c_offshore_id      | rampion-united-kingdom-uk36                   |
| same-as        | windpowernet_id     | windfarm_en_16761_rampion                     |
| same-as        | wikidata_id         | Q7290043                                      |
| same-as        | wikipedia_id        | Rampion_Wind_Farm                             |
| same-as        | power_technology_id | rampion-offshore-wind-project-english-channel |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.27 |
| Latitude    |   50.67 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 80.0     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   RMPNO-1 |   RMPNO-2 |
|:--------------------|-------:|----------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |      0.00 |
| Annual Output (MWh) |   2017 |   8233.54 |      0.00 |
| Annual Output (MWh) |   2018 | 473911.01 | 446124.40 |
| Annual Output (MWh) |   2019 | 660502.91 | 366411.69 |
| Annual Output (MWh) |   2020 | 754945.80 | 812825.09 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | RMPNO-1   | RMPNO-2   |
|:------------|:----------|:----------|
| Fuel Type   | WIND      | WIND      |

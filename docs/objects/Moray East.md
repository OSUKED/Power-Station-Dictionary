### Identifiers

| Relationship   | ID Type             | ID(s)                                 |
|:---------------|:--------------------|:--------------------------------------|
| root           | osuked_id           | 10304                                 |
| element-of     | sett_bmu_id         | T_MOWEO-1, T_MOWEO-2, T_MOWEO-3       |
| element-of     | ngc_bmu_id          | MOWEO-1, MOWEO-2, MOWEO-3             |
| same-as        | name                | Moray East                            |
| same-as        | 4c_offshore_id      | moray-east-united-kingdom-uk40        |
| same-as        | windpowernet_id     | windfarm_en_16772_moray-east          |
| same-as        | power_technology_id | moray-offshore-windfarm-east-scotland |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -2.72 |
| Latitude    |   58.19 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 105.0    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | MOWEO-1   | MOWEO-2   | MOWEO-3   |
|:------------|:----------|:----------|:----------|
| Fuel Type   | WIND      | WIND      | WIND      |

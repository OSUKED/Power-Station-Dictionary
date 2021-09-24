### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                     |
|:---------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10304                                                                                                                     |
| Related        | Settlement BMU ID    | T_MOWEO-1, T_MOWEO-2, T_MOWEO-3                                                                                           |
| Related        | National Grid BMU ID | MOWEO-1, MOWEO-2, MOWEO-3                                                                                                 |
| Related        | EIC ID               | 48W000000MOWEO11, 48W00000MOWEO-2Y, 48W00000MOWEO-3W                                                                      |
| Equivalent     | Common Name          | Moray East                                                                                                                |
| Equivalent     | 4C-Offshore ID       | [moray-east-united-kingdom-uk40](https://www.4coffshore.com/windfarms/united-kingdom/moray-east-united-kingdom-uk40.html) |
| Equivalent     | WindPowerNet ID      | [windfarm_en_16772_moray-east](https://www.thewindpower.net/windfarm_en_16772_moray-east.php)                             |
| Equivalent     | Power-Technology ID  | [moray-offshore-windfarm-east-scotland](https://www.power-technology.com/projects/moray-offshore-windfarm-east-scotland)  |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | MOWEO-1   | MOWEO-2   | MOWEO-3   |
|:------------|:----------|:----------|:----------|
| Fuel Type   | WIND      | WIND      | WIND      |

<br><br>
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

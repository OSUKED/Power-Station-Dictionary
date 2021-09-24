### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:---------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10290                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Related        | Settlement BMU ID    | E_KINCW-1                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Related        | National Grid BMU ID | KINCW-1                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Related        | 4C-Offshore ID       | [kincardine---phase-1-united-kingdom-uk2h](https://www.4coffshore.com/windfarms/united-kingdom/kincardine---phase-1-united-kingdom-uk2h.html), [kincardine---phase-2-united-kingdom-uk4n](https://www.4coffshore.com/windfarms/united-kingdom/kincardine---phase-2-united-kingdom-uk4n.html), [kincardine---dolphyn---2-mw-demo-united-kingdom-uk4u](https://www.4coffshore.com/windfarms/united-kingdom/kincardine---dolphyn---2-mw-demo-united-kingdom-uk4u.html) |
| Equivalent     | Common Name          | Kincardine                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Equivalent     | WindPowerNet ID      | [windfarm_en_17376_kincardine-offshore-windfarm](https://www.thewindpower.net/windfarm_en_17376_kincardine-offshore-windfarm.php)                                                                                                                                                                                                                                                                                                                                   |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | WIND    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -1.88 |
| Latitude    |   56.98 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 102.5    |

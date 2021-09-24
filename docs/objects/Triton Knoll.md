### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                         |
|:---------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10306                                                                                                                         |
| Related        | Settlement BMU ID    | T_TKNEW-1, T_TKNWW-1                                                                                                          |
| Related        | National Grid BMU ID | TKNEW-1, TKNWW-1                                                                                                              |
| Equivalent     | Common Name          | Triton Knoll                                                                                                                  |
| Equivalent     | 4C-Offshore ID       | [triton-knoll-united-kingdom-uk30](https://www.4coffshore.com/windfarms/united-kingdom/triton-knoll-united-kingdom-uk30.html) |
| Equivalent     | WindPowerNet ID      | [windfarm_en_10786_triton-knoll-wind-farm](https://www.thewindpower.net/windfarm_en_10786_triton-knoll-wind-farm.php)         |
| Equivalent     | Wikidata ID          | [Q7844328](https://www.wikidata.org/wiki/Q7844328)                                                                            |
| Equivalent     | Wikipedia ID         | [Triton_Knoll](https://en.wikipedia.org/wiki/Triton_Knoll)                                                                    |
| Equivalent     | Power-Technology ID  | [triton-knoll-offshore-windfarm](https://www.power-technology.com/projects/triton-knoll-offshore-windfarm)                    |
| Equivalent     | CfD ID               | AR2-TKN-303                                                                                                                   |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | TKNEW-1   | TKNWW-1   |
|:------------|:----------|:----------|
| Fuel Type   | WIND      | WIND      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    0.84 |
| Latitude    |   53.48 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 140.0    |

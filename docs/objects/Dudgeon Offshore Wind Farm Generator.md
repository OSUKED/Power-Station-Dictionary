### Identifiers

| Relationship   | ID Type             | ID(s)                                      |
|:---------------|:--------------------|:-------------------------------------------|
| root           | osuked_id           | 10185                                      |
| element-of     | sett_bmu_id         | T_DDGNO-1, T_DDGNO-2, T_DDGNO-3, T_DDGNO-4 |
| element-of     | ngc_bmu_id          | DDGNO-1, DDGNO-2, DDGNO-3, DDGNO-4         |
| same-as        | esail_id            | DDGNO                                      |
| same-as        | name                | Dudgeon Offshore Wind Farm Generator       |
| same-as        | 4c_offshore_id      | dudgeon-united-kingdom-uk04                |
| same-as        | windpowernet_id     | windfarm_en_12072_dudgeon                  |
| same-as        | wikidata_id         | Q5311735                                   |
| same-as        | wikipedia_id        | Dudgeon_Offshore_Wind_Farm                 |
| same-as        | power_technology_id | dudgeon-offshore-wind-farm                 |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    1.39 |
| Latitude    |   53.25 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 110.0    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   DDGNO-1 |   DDGNO-2 |   DDGNO-3 |   DDGNO-4 |
|:--------------------|-------:|----------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2017 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2018 | 176743.81 | 172032.94 | 182301.18 | 185793.67 |
| Annual Output (MWh) |   2019 | 416007.83 | 366762.44 | 398173.59 | 417384.72 |
| Annual Output (MWh) |   2020 | 446123.36 | 398511.70 | 435760.64 | 442121.23 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | DDGNO-1   | DDGNO-2   | DDGNO-3   | DDGNO-4   |
|:------------|:----------|:----------|:----------|:----------|
| Fuel Type   | WIND      | WIND      | WIND      | WIND      |

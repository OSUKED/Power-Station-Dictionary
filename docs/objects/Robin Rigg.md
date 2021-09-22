### Identifiers

| Relationship   | ID Type             | ID(s)                          |
|:---------------|:--------------------|:-------------------------------|
| root           | osuked_id           | 10235                          |
| element-of     | gppd_idnr           | GBR0002496, GBR0002497         |
| element-of     | sett_bmu_id         | T_RREW-1, T_RRWW-1             |
| element-of     | ngc_bmu_id          | RREW-1, RRWW-1                 |
| same-as        | esail_id            | RREW, RRWW                     |
| same-as        | name                | Robin Rigg                     |
| same-as        | 4c_offshore_id      | robin-rigg-united-kingdom-uk20 |
| same-as        | windpowernet_id     | windfarm_en_7392_robin-rigg    |
| same-as        | wikidata_id         | Q1724197                       |
| same-as        | wikipedia_id        | Robin_Rigg_Wind_Farm           |
| same-as        | power_technology_id | robinriggwind                  |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.72 |
| Latitude    |   54.75 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 80.0     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | GBR0002496                                                               | GBR0002497                                                               |
|:------------------------------------|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------|
| Estimated Annual Generation in 2017 | 226.88                                                                   | 226.88                                                                   |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    | UK Renewable Energy Planning Database                                    |
| Installed Capacity (MW)             | 90.0                                                                     | 90.0                                                                     |
| Latitude                            | 54.7642                                                                  | 54.7473                                                                  |
| Longitude                           | -3.6955                                                                  | -3.7293                                                                  |
| Owner                               | E.On                                                                     | E.On                                                                     |
| PLATTS-WEPP ID                      | 1056904.0                                                                | 1056904.0                                                                |
| Primary Fuel Type                   | Wind                                                                     | Wind                                                                     |
| Source                              | UK Renewable Energy Planning Database                                    | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data | https://www.gov.uk/government/collections/renewable-energy-planning-data |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    RREW-1 |    RRWW-1 |
|:--------------------|-------:|----------:|----------:|
| Annual Output (MWh) |   2016 | 238460.02 | 255999.26 |
| Annual Output (MWh) |   2017 | 247941.79 | 282252.49 |
| Annual Output (MWh) |   2018 | 248906.54 | 286534.65 |
| Annual Output (MWh) |   2019 | 246943.94 | 278775.61 |
| Annual Output (MWh) |   2020 | 300224.43 | 327928.89 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | RREW-1   | RRWW-1   |
|:------------|:---------|:---------|
| Fuel Type   | WIND     | WIND     |

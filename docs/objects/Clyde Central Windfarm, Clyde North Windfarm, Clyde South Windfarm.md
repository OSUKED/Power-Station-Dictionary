### Identifiers

| Relationship   | ID Type     | ID(s)                                                              |
|:---------------|:------------|:-------------------------------------------------------------------|
| root           | osuked_id   | 10177                                                              |
| element-of     | sett_bmu_id | T_CLDCW-1, T_CLDNW-1, T_CLDSW-1                                    |
| element-of     | ngc_bmu_id  | CLDCW-1, CLDNW-1, CLDSW-1                                          |
| same-as        | gppd_idnr   | GBR0004178                                                         |
| same-as        | esail_id    | CLDW                                                               |
| same-as        | name        | Clyde Central Windfarm, Clyde North Windfarm, Clyde South Windfarm |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.35 |
| Latitude    |   55.31 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Plant Type  | onshore |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                    |
|:------------------------------------|:-------------------------------------------------------------------------|
| Installed Capacity (MW)             | 172.8                                                                    |
| Longitude                           | -3.5479                                                                  |
| Latitude                            | 55.5041                                                                  |
| Primary Fuel Type                   | Wind                                                                     |
| Owner                               | Scottish and Southern Energy (SSE)/ GIB                                  |
| Source                              | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    |
| Estimated Annual Generation in 2017 | 435.62                                                                   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   CLDCW-1 |   CLDNW-1 |   CLDSW-1 |
|:--------------------|-------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 | 258211.70 | 300339.19 | 278852.64 |
| Annual Output (MWh) |   2017 | 387415.42 | 481927.83 | 320280.22 |
| Annual Output (MWh) |   2018 | 490353.66 | 541773.11 | 320944.80 |
| Annual Output (MWh) |   2019 | 494431.85 | 533649.56 | 242403.49 |
| Annual Output (MWh) |   2020 | 503833.89 | 526718.25 | 296734.87 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | CLDCW-1   | CLDNW-1   | CLDSW-1   |
|:------------|:----------|:----------|:----------|
| Fuel Type   | WIND      | WIND      | WIND      |

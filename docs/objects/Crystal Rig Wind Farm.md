### Identifiers

| Relationship   | ID Type     | ID(s)                  |
|:---------------|:------------|:-----------------------|
| root           | osuked_id   | 10181                  |
| element-of     | gppd_idnr   | GBR0004215, GBR0003440 |
| element-of     | sett_bmu_id | T_CRYRW-2, T_CRYRW-3   |
| element-of     | ngc_bmu_id  | CRYRW-2, CRYRW-3       |
| same-as        | esail_id    | CRYRW                  |
| same-as        | name        | Crystal Rig Wind Farm  |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -2.40 |
| Latitude    |   55.89 |

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

| Attribute                           | GBR0003440                                                               | GBR0004215                                                               |
|:------------------------------------|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------|
| Estimated Annual Generation in 2017 | 347.89                                                                   | 34.78                                                                    |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    | UK Renewable Energy Planning Database                                    |
| Installed Capacity (MW)             | 138.0                                                                    | 13.8                                                                     |
| Latitude                            | 55.8995                                                                  | 55.9264                                                                  |
| Longitude                           | -2.5293                                                                  | -2.5345                                                                  |
| Owner                               | Fred Olsen Renewables                                                    | Fred Olsen Renewables                                                    |
| PLATTS-WEPP ID                      | 1056261.0                                                                | 1056261.0                                                                |
| Primary Fuel Type                   | Wind                                                                     | Wind                                                                     |
| Source                              | UK Renewable Energy Planning Database                                    | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data | https://www.gov.uk/government/collections/renewable-energy-planning-data |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     Value |
|:--------------------|-------:|----------:|
| Annual Output (MWh) |   2016 | 308673.02 |
| Annual Output (MWh) |   2017 | 380460.76 |
| Annual Output (MWh) |   2018 | 333805.70 |
| Annual Output (MWh) |   2019 | 299792.32 |
| Annual Output (MWh) |   2020 | 367136.53 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | CRYRW-2   | CRYRW-3   |
|:------------|:----------|:----------|
| Fuel Type   | WIND      | WIND      |

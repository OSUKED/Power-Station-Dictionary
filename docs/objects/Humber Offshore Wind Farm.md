### Identifiers

| Relationship   | ID Type             | ID(s)                              |
|:---------------|:--------------------|:-----------------------------------|
| root           | osuked_id           | 10214                              |
| element-of     | sett_bmu_id         | T_HMGTO-1, T_HMGTO-2               |
| element-of     | ngc_bmu_id          | HMGTO-1, HMGTO-2                   |
| same-as        | gppd_idnr           | GBR0002544                         |
| same-as        | esail_id            | HMGTO                              |
| same-as        | name                | Humber Offshore Wind Farm          |
| same-as        | 4c_offshore_id      | humber-gateway-united-kingdom-uk10 |
| same-as        | windpowernet_id     | windfarm_en_12070_humber-gateway   |
| same-as        | wikidata_id         | Q15226770                          |
| same-as        | wikipedia_id        | Humber_Gateway_Wind_Farm           |
| same-as        | power_technology_id | humber-gateway-offshore-wind-farm  |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    0.29 |
| Latitude    |   53.64 |

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

| Attribute                           | Value                                                                    |
|:------------------------------------|:-------------------------------------------------------------------------|
| Installed Capacity (MW)             | 219.0                                                                    |
| Longitude                           | 0.5006                                                                   |
| Latitude                            | 53.3875                                                                  |
| Primary Fuel Type                   | Wind                                                                     |
| Owner                               | E.ON  Humber Wind Ltd/ Balfour Beatty Investments and Equitix.           |
| Source                              | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    |
| PLATTS-WEPP ID                      | 1070246.0                                                                |
| Estimated Annual Generation in 2017 | 552.08                                                                   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     Value |
|:--------------------|-------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |
| Annual Output (MWh) |   2017 |      0.00 |
| Annual Output (MWh) |   2018 | 369522.74 |
| Annual Output (MWh) |   2019 | 418021.72 |
| Annual Output (MWh) |   2020 | 461932.97 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | HMGTO-1   | HMGTO-2   |
|:------------|:----------|:----------|
| Fuel Type   | WIND      | WIND      |

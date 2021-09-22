### Identifiers

| Relationship   | ID Type             | ID(s)                                                                                                                                                                                                                |
|:---------------|:--------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| root           | osuked_id           | 10201                                                                                                                                                                                                                |
| element-of     | sett_bmu_id         | T_GRGBW-1, T_GRGBW-2, T_GRGBW-3                                                                                                                                                                                      |
| element-of     | ngc_bmu_id          | GRGBW-1, GRGBW-2, GRGBW-3                                                                                                                                                                                            |
| element-of     | windpowernet_id     | [windfarm_en_1615_greater-gabbard-1](https://www.thewindpower.net/windfarm_en_1615_greater-gabbard-1.php), [windfarm_en_7107_greater-gabbard-2](https://www.thewindpower.net/windfarm_en_7107_greater-gabbard-2.php) |
| same-as        | gppd_idnr           | GBR0002510                                                                                                                                                                                                           |
| same-as        | esail_id            | GRGBW                                                                                                                                                                                                                |
| same-as        | name                | Greater Gabbard Offshore Windfarm                                                                                                                                                                                    |
| same-as        | 4c_offshore_id      | greater-gabbard-united-kingdom-uk05                                                                                                                                                                                  |
| same-as        | wikidata_id         | Q820613                                                                                                                                                                                                              |
| same-as        | wikipedia_id        | Greater_Gabbard_wind_farm                                                                                                                                                                                            |
| same-as        | power_technology_id | greatergabbardoffsho                                                                                                                                                                                                 |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    1.71 |
| Latitude    |   52.07 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 79.5     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                    |
|:------------------------------------|:-------------------------------------------------------------------------|
| Installed Capacity (MW)             | 504.0                                                                    |
| Longitude                           | 1.9284                                                                   |
| Latitude                            | 51.9176                                                                  |
| Primary Fuel Type                   | Wind                                                                     |
| Owner                               | Airtricity / Fluor Ltd                                                   |
| Source                              | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    |
| PLATTS-WEPP ID                      | 1061829.0                                                                |
| Estimated Annual Generation in 2017 | 1270.56                                                                  |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   GRGBW-1 |   GRGBW-2 |   GRGBW-3 |
|:--------------------|-------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 | 572836.86 | 621071.27 | 590806.58 |
| Annual Output (MWh) |   2017 | 609198.18 | 642323.33 | 607380.74 |
| Annual Output (MWh) |   2018 | 533116.47 | 564928.18 | 556467.97 |
| Annual Output (MWh) |   2019 | 499996.53 | 372637.43 | 567777.30 |
| Annual Output (MWh) |   2020 | 632324.84 | 671951.74 | 623308.87 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | GRGBW-1   | GRGBW-2   | GRGBW-3   |
|:------------|:----------|:----------|:----------|
| Fuel Type   | WIND      | WIND      | WIND      |

### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                             |
|:---------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10214                                                                                                                             |
| Related        | Settlement BMU ID    | T_HMGTO-1, T_HMGTO-2                                                                                                              |
| Related        | National Grid BMU ID | HMGTO-1, HMGTO-2                                                                                                                  |
| Equivalent     | GPPD ID              | GBR0002544                                                                                                                        |
| Equivalent     | ESAIL ID             | HMGTO                                                                                                                             |
| Equivalent     | Common Name          | Humber Offshore Wind Farm                                                                                                         |
| Equivalent     | 4C-Offshore ID       | [humber-gateway-united-kingdom-uk10](https://www.4coffshore.com/windfarms/united-kingdom/humber-gateway-united-kingdom-uk10.html) |
| Equivalent     | WindPowerNet ID      | [windfarm_en_12070_humber-gateway](https://www.thewindpower.net/windfarm_en_12070_humber-gateway.php)                             |
| Equivalent     | Wikidata ID          | [Q15226770](https://www.wikidata.org/wiki/Q15226770)                                                                              |
| Equivalent     | Wikipedia ID         | [Humber_Gateway_Wind_Farm](https://en.wikipedia.org/wiki/Humber_Gateway_Wind_Farm)                                                |
| Equivalent     | Power-Technology ID  | [humber-gateway-offshore-wind-farm](https://www.power-technology.com/projects/humber-gateway-offshore-wind-farm)                  |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | HMGTO-1   | HMGTO-2   |
|:------------|:----------|:----------|
| Fuel Type   | WIND      | WIND      |

<br><br>
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
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2018 |   56.10 |
| Capture Price (£/MWh) |   2019 |   40.34 |
| Capture Price (£/MWh) |   2020 |   31.16 |

### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                                                                                                                                                                                            |
|:---------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10239                                                                                                                                                                                                                                                                                            |
| Related        | Settlement BMU ID    | E_SHRSW-1, T_SHRSW-1, E_SHRSW-2, T_SHRSW-2                                                                                                                                                                                                                                                       |
| Related        | National Grid BMU ID | SHRSW-1, SHRSO-1, SHRSW-2, SHRSO-2                                                                                                                                                                                                                                                               |
| Related        | 4C-Offshore ID       | [sheringham-shoal-united-kingdom-uk27](https://www.4coffshore.com/windfarms/united-kingdom/sheringham-shoal-united-kingdom-uk27.html), [sheringham-shoal-extension-united-kingdom-uk4h](https://www.4coffshore.com/windfarms/united-kingdom/sheringham-shoal-extension-united-kingdom-uk4h.html) |
| Related        | WindPowerNet ID      | [windfarm_en_7394_sheringham-shoal](https://www.thewindpower.net/windfarm_en_7394_sheringham-shoal.php), [windfarm_en_30017_sheringham-shoal-extension](https://www.thewindpower.net/windfarm_en_30017_sheringham-shoal-extension.php)                                                           |
| Related        | EIC ID               | 48W00000SHRSO-1Y, 48W00000SHRSO-2W                                                                                                                                                                                                                                                               |
| Equivalent     | GPPD ID              | GBR0002512                                                                                                                                                                                                                                                                                       |
| Equivalent     | ESAIL ID             | SHRSW                                                                                                                                                                                                                                                                                            |
| Equivalent     | Common Name          | Sheringham Shoals Windfarm  1                                                                                                                                                                                                                                                                    |
| Equivalent     | Wikidata ID          | [Q7495028](https://www.wikidata.org/wiki/Q7495028)                                                                                                                                                                                                                                               |
| Equivalent     | Wikipedia ID         | [Sheringham_Shoal_Offshore_Wind_Farm](https://en.wikipedia.org/wiki/Sheringham_Shoal_Offshore_Wind_Farm)                                                                                                                                                                                         |
| Equivalent     | Power-Technology ID  | [sheringham-shoal](https://www.power-technology.com/projects/sheringham-shoal)                                                                                                                                                                                                                   |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | SHRSO-1   | SHRSO-2   |
|:------------|:----------|:----------|
| Fuel Type   | WIND      | WIND      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    1.15 |
| Latitude    |   53.13 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 132.0    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                    |
|:------------------------------------|:-------------------------------------------------------------------------|
| Installed Capacity (MW)             | 316.0                                                                    |
| Longitude                           | 1.1479                                                                   |
| Latitude                            | 53.1353                                                                  |
| Primary Fuel Type                   | Wind                                                                     |
| Owner                               | Vattenfall                                                               |
| Source                              | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    |
| Estimated Annual Generation in 2017 | 796.62                                                                   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   SHRSO-1 |   SHRSO-2 |
|:--------------------|-------:|----------:|----------:|
| Annual Output (MWh) |   2016 | 525299.36 | 515755.11 |
| Annual Output (MWh) |   2017 | 583486.91 | 555401.23 |
| Annual Output (MWh) |   2018 | 525391.77 | 529068.46 |
| Annual Output (MWh) |   2019 | 540017.89 | 532502.49 |
| Annual Output (MWh) |   2020 | 588697.74 | 575378.54 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   SHRSO-1 |   SHRSO-2 |
|:----------------------|-------:|----------:|----------:|
| Capture Price (£/MWh) |   2016 |     36.12 |     36.22 |
| Capture Price (£/MWh) |   2017 |     44.15 |     44.32 |
| Capture Price (£/MWh) |   2018 |     56.09 |     56.05 |
| Capture Price (£/MWh) |   2019 |     40.21 |     40.31 |
| Capture Price (£/MWh) |   2020 |     31.08 |     31.11 |

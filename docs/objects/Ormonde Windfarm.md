### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                               |
|:---------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10229                                                                                                               |
| Related        | Settlement BMU ID    | E_OMNDW-1, T_OMNDW-1, E_OMNDD-1                                                                                     |
| Related        | National Grid BMU ID | OMNDW-1, OMNDO-1, OMNDD-1                                                                                           |
| Equivalent     | GPPD ID              | GBR0002509                                                                                                          |
| Equivalent     | ESAIL ID             | OMNDW                                                                                                               |
| Equivalent     | Common Name          | Ormonde Windfarm                                                                                                    |
| Equivalent     | 4C-Offshore ID       | [ormonde-united-kingdom-uk17](https://www.4coffshore.com/windfarms/united-kingdom/ormonde-united-kingdom-uk17.html) |
| Equivalent     | WindPowerNet ID      | [windfarm_en_1629_ormonde](https://www.thewindpower.net/windfarm_en_1629_ormonde.php)                               |
| Equivalent     | Wikidata ID          | [Q763941](https://www.wikidata.org/wiki/Q763941)                                                                    |
| Equivalent     | Wikipedia ID         | [Ormonde_Wind_Farm](https://en.wikipedia.org/wiki/Ormonde_Wind_Farm)                                                |
| Equivalent     | Power-Technology ID  | [ormonde-offshore-wind-farm](https://www.power-technology.com/projects/ormonde-offshore-wind-farm)                  |
| Equivalent     | EIC ID               | 48W00000OMNDO-1J                                                                                                    |

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
| Longitude   |   -3.40 |
| Latitude    |   54.10 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 100.0    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                    |
|:------------------------------------|:-------------------------------------------------------------------------|
| Installed Capacity (MW)             | 150.0                                                                    |
| Longitude                           | -3.4386                                                                  |
| Latitude                            | 54.0889                                                                  |
| Primary Fuel Type                   | Wind                                                                     |
| Owner                               | Vattenfall                                                               |
| Source                              | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    |
| PLATTS-WEPP ID                      | 1078074.0                                                                |
| Estimated Annual Generation in 2017 | 378.14                                                                   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     Value |
|:--------------------|-------:|----------:|
| Annual Output (MWh) |   2016 | 474337.58 |
| Annual Output (MWh) |   2017 | 397657.20 |
| Annual Output (MWh) |   2018 | 445361.75 |
| Annual Output (MWh) |   2019 | 463310.91 |
| Annual Output (MWh) |   2020 | 522667.45 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   35.56 |
| Capture Price (£/MWh) |   2017 |   44.57 |
| Capture Price (£/MWh) |   2018 |   56.73 |
| Capture Price (£/MWh) |   2019 |   40.14 |
| Capture Price (£/MWh) |   2020 |   30.63 |

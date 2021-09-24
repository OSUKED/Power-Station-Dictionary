### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                             |
|:---------------|:---------------------|:------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10156                                                                                                             |
| Related        | Settlement BMU ID    | T_BOWLW-1                                                                                                         |
| Related        | National Grid BMU ID | BOWLW-1                                                                                                           |
| Equivalent     | GPPD ID              | GBR0002546                                                                                                        |
| Equivalent     | ESAIL ID             | BOWLW                                                                                                             |
| Equivalent     | Common Name          | Barrow Offshore Windfarm                                                                                          |
| Equivalent     | 4C-Offshore ID       | [barrow-united-kingdom-uk01](https://www.4coffshore.com/windfarms/united-kingdom/barrow-united-kingdom-uk01.html) |
| Equivalent     | WindPowerNet ID      | [windfarm_en_1503_barrow](https://www.thewindpower.net/windfarm_en_1503_barrow.php)                               |
| Equivalent     | Wikidata ID          | [Q2016017](https://www.wikidata.org/wiki/Q2016017)                                                                |
| Equivalent     | Wikipedia ID         | [Barrow_Offshore_Wind_Farm](https://en.wikipedia.org/wiki/Barrow_Offshore_Wind_Farm)                              |
| Equivalent     | EIC ID               | 48W00000BOWLW-1K                                                                                                  |

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
| Longitude   |   -3.28 |
| Latitude    |   53.98 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 75.0     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                    |
|:------------------------------------|:-------------------------------------------------------------------------|
| Installed Capacity (MW)             | 90.0                                                                     |
| Longitude                           | -3.2983                                                                  |
| Latitude                            | 53.9915                                                                  |
| Primary Fuel Type                   | Wind                                                                     |
| Owner                               | Orsted (formerly Dong Energy)                                            |
| Source                              | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    |
| Estimated Annual Generation in 2017 | 226.88                                                                   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     Value |
|:--------------------|-------:|----------:|
| Annual Output (MWh) |   2016 | 274316.86 |
| Annual Output (MWh) |   2017 | 296954.75 |
| Annual Output (MWh) |   2018 | 274151.77 |
| Annual Output (MWh) |   2019 | 283391.21 |
| Annual Output (MWh) |   2020 | 251538.81 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   36.21 |
| Capture Price (£/MWh) |   2017 |   43.94 |
| Capture Price (£/MWh) |   2018 |   55.96 |
| Capture Price (£/MWh) |   2019 |   39.58 |
| Capture Price (£/MWh) |   2020 |   30.44 |

### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                           |
|:---------------|:---------------------|:----------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10219                                                                                                           |
| Related        | Settlement BMU ID    | T_LNCSW-1, T_LNCSW-2, T_LNCSW-3                                                                                 |
| Related        | National Grid BMU ID | LNCSO-1, LNCSO-2, LNCSW-3                                                                                       |
| Related        | EIC ID               | 48W00000LNCSO-1R, 48W00000LNCSO-2P                                                                              |
| Equivalent     | GPPD ID              | GBR0002513                                                                                                      |
| Equivalent     | ESAIL ID             | LNCSW                                                                                                           |
| Equivalent     | Common Name          | Lincs Offshore Wind Farm                                                                                        |
| Equivalent     | 4C-Offshore ID       | [lincs-united-kingdom-uk13](https://www.4coffshore.com/windfarms/united-kingdom/lincs-united-kingdom-uk13.html) |
| Equivalent     | WindPowerNet ID      | [windfarm_en_10526_lincs](https://www.thewindpower.net/windfarm_en_10526_lincs.php)                             |
| Equivalent     | Wikidata ID          | [Q6551320](https://www.wikidata.org/wiki/Q6551320)                                                              |
| Equivalent     | Wikipedia ID         | [Lincs_Wind_Farm](https://en.wikipedia.org/wiki/Lincs_Wind_Farm)                                                |
| Equivalent     | Power-Technology ID  | [centricalincs](https://www.power-technology.com/projects/centricalincs)                                        |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | LNCSO-1   | LNCSO-2   |
|:------------|:----------|:----------|
| Fuel Type   | WIND      | WIND      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    0.53 |
| Latitude    |   53.27 |

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
| Installed Capacity (MW)             | 270.0                                                                    |
| Longitude                           | 0.4981                                                                   |
| Latitude                            | 53.1842                                                                  |
| Primary Fuel Type                   | Wind                                                                     |
| Owner                               | GIB                                                                      |
| Source                              | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    |
| Estimated Annual Generation in 2017 | 680.65                                                                   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   LNCSO-1 |   LNCSO-2 |
|:--------------------|-------:|----------:|----------:|
| Annual Output (MWh) |   2016 | 456783.34 | 498833.44 |
| Annual Output (MWh) |   2017 | 485943.16 | 538447.75 |
| Annual Output (MWh) |   2018 | 445459.89 | 492080.06 |
| Annual Output (MWh) |   2019 | 471039.73 | 515900.69 |
| Annual Output (MWh) |   2020 | 522144.55 | 573325.51 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   LNCSO-1 |   LNCSO-2 |
|:----------------------|-------:|----------:|----------:|
| Capture Price (£/MWh) |   2016 |     36.48 |     36.69 |
| Capture Price (£/MWh) |   2017 |     43.83 |     43.87 |
| Capture Price (£/MWh) |   2018 |     56.20 |     56.32 |
| Capture Price (£/MWh) |   2019 |     40.23 |     40.38 |
| Capture Price (£/MWh) |   2020 |     30.72 |     30.84 |

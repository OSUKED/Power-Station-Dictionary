### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                         |
|:---------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10221                                                                                                                         |
| Related        | Settlement BMU ID    | T_LARYW-1, T_LARYW-2, T_LARYW-3, T_LARYW-4                                                                                    |
| Related        | National Grid BMU ID | LARYO-1, LARYO-2, LARYO-3, LARYO-4                                                                                            |
| Related        | EIC ID               | 48W00000LARYO-1Z, 48W00000LARYO-2X, 48W00000LARYO-3V, 48W00000LARYO-4T                                                        |
| Equivalent     | GPPD ID              | GBR0002511                                                                                                                    |
| Equivalent     | ESAIL ID             | LARYW                                                                                                                         |
| Equivalent     | Common Name          | London Array Windfarm                                                                                                         |
| Equivalent     | 4C-Offshore ID       | [london-array-united-kingdom-uk14](https://www.4coffshore.com/windfarms/united-kingdom/london-array-united-kingdom-uk14.html) |
| Equivalent     | WindPowerNet ID      | [windfarm_en_1574_london-array](https://www.thewindpower.net/windfarm_en_1574_london-array.php)                               |
| Equivalent     | Wikidata ID          | [Q914264](https://www.wikidata.org/wiki/Q914264)                                                                              |
| Equivalent     | Wikipedia ID         | [London_Array](https://en.wikipedia.org/wiki/London_Array)                                                                    |
| Equivalent     | Power-Technology ID  | [london-array](https://www.power-technology.com/projects/london-array)                                                        |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | LARYO-1   | LARYO-2   | LARYO-3   | LARYO-4   |
|:------------|:----------|:----------|:----------|:----------|
| Fuel Type   | WIND      | WIND      | WIND      | WIND      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    1.36 |
| Latitude    |   51.65 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 87.0     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                    |
|:------------------------------------|:-------------------------------------------------------------------------|
| Installed Capacity (MW)             | 630.0                                                                    |
| Longitude                           | 1.4958                                                                   |
| Latitude                            | 51.6217                                                                  |
| Primary Fuel Type                   | Wind                                                                     |
| Owner                               | Siemens Gamesa Renewable Energy                                          |
| Source                              | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    |
| Estimated Annual Generation in 2017 | 1588.2                                                                   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   LARYO-1 |   LARYO-2 |   LARYO-3 |   LARYO-4 |
|:--------------------|-------:|----------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 | 551153.80 | 582802.56 | 551014.27 | 556309.16 |
| Annual Output (MWh) |   2017 | 554880.41 | 529613.13 | 561006.54 | 558952.02 |
| Annual Output (MWh) |   2018 | 487442.36 | 479026.91 | 440800.47 | 580230.39 |
| Annual Output (MWh) |   2019 | 474597.84 | 378873.93 | 578701.82 | 547497.09 |
| Annual Output (MWh) |   2020 | 641209.79 | 654520.60 | 648465.83 | 647593.43 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   LARYO-1 |   LARYO-2 |   LARYO-3 |   LARYO-4 |
|:----------------------|-------:|----------:|----------:|----------:|----------:|
| Capture Price (£/MWh) |   2016 |     36.84 |     37.04 |     36.85 |     37.19 |
| Capture Price (£/MWh) |   2017 |     44.56 |     44.22 |     44.44 |     44.53 |
| Capture Price (£/MWh) |   2018 |     55.58 |     56.73 |     55.38 |     56.56 |
| Capture Price (£/MWh) |   2019 |     41.82 |     38.58 |     40.68 |     40.59 |
| Capture Price (£/MWh) |   2020 |     31.07 |     31.10 |     30.92 |     30.88 |

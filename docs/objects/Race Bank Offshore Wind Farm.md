### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                                                                                                                                                                |
|:---------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10233                                                                                                                                                                                                                                                                |
| Related        | Settlement BMU ID    | T_RCBKO-1, T_RCBKO-2                                                                                                                                                                                                                                                 |
| Related        | National Grid BMU ID | RCBKO-1, RCBKO-2                                                                                                                                                                                                                                                     |
| Related        | 4C-Offshore ID       | [race-bank-united-kingdom-uk18](https://www.4coffshore.com/windfarms/united-kingdom/race-bank-united-kingdom-uk18.html), [race-bank-extension-united-kingdom-uk4f](https://www.4coffshore.com/windfarms/united-kingdom/race-bank-extension-united-kingdom-uk4f.html) |
| Related        | WindPowerNet ID      | [windfarm_en_12071_race-bank](https://www.thewindpower.net/windfarm_en_12071_race-bank.php), [windfarm_en_30016_race-bank-extension](https://www.thewindpower.net/windfarm_en_30016_race-bank-extension.php)                                                         |
| Related        | EIC ID               | 48W00000RCBKO-1S, 48W00000RCBKO-2Q                                                                                                                                                                                                                                   |
| Equivalent     | GPPD ID              | GBR0002515                                                                                                                                                                                                                                                           |
| Equivalent     | ESAIL ID             | RCBKO                                                                                                                                                                                                                                                                |
| Equivalent     | Common Name          | Race Bank Offshore Wind Farm                                                                                                                                                                                                                                         |
| Equivalent     | Wikidata ID          | [Q3364824](https://www.wikidata.org/wiki/Q3364824)                                                                                                                                                                                                                   |
| Equivalent     | Wikipedia ID         | [Race_Bank_wind_farm](https://en.wikipedia.org/wiki/Race_Bank_wind_farm)                                                                                                                                                                                             |
| Equivalent     | Power-Technology ID  | [race-bank-wind-farm](https://www.power-technology.com/projects/race-bank-wind-farm)                                                                                                                                                                                 |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | RCBKO-1   | RCBKO-2   |
|:------------|:----------|:----------|
| Fuel Type   | WIND      | WIND      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    0.84 |
| Latitude    |   53.28 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 90.0     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                    |
|:------------------------------------|:-------------------------------------------------------------------------|
| Installed Capacity (MW)             | 286.5                                                                    |
| Longitude                           | 0.5892                                                                   |
| Latitude                            | 53.136                                                                   |
| Primary Fuel Type                   | Wind                                                                     |
| Owner                               | Orsted (formerly Dong Energy)/ Macquarie Group                           |
| Source                              | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    |
| Estimated Annual Generation in 2017 | 722.25                                                                   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    RCBKO-1 |    RCBKO-2 |
|:--------------------|-------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 |       0.00 |       0.00 |
| Annual Output (MWh) |   2017 |  253709.63 |  445349.03 |
| Annual Output (MWh) |   2018 |  985582.74 |  989011.14 |
| Annual Output (MWh) |   2019 | 1045484.57 | 1086769.34 |
| Annual Output (MWh) |   2020 | 1190008.20 | 1199973.40 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   RCBKO-1 |   RCBKO-2 |
|:----------------------|-------:|----------:|----------:|
| Capture Price (£/MWh) |   2017 |     49.45 |     47.10 |
| Capture Price (£/MWh) |   2018 |     56.54 |     56.46 |
| Capture Price (£/MWh) |   2019 |     40.01 |     40.31 |
| Capture Price (£/MWh) |   2020 |     31.11 |     31.21 |

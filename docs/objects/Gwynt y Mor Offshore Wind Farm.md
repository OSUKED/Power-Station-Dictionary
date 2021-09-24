### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                              |
|:---------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10206                                                                                                                              |
| Related        | Settlement BMU ID    | T_GYMRW-1, T_GYMRW-2, T_GYMR-15, T_GYMR-17, T_GYMR-26, T_GYMR-28                                                                   |
| Related        | National Grid BMU ID | GYMRW-1, GYMRW-2, GYMRO-15, GYMRO-17, GYMRO-26, GYMRO-28                                                                           |
| Related        | EIC ID               | 48W00000GYMRW-1E, 48W00000GYMRW-2C, 48W0000GYMRO-15O, 48W0000GYMRO-17K, 48W0000GYMRO-26J, 48W0000GYMRO-28F                         |
| Equivalent     | GPPD ID              | GBR0002543                                                                                                                         |
| Equivalent     | ESAIL ID             | GYMR                                                                                                                               |
| Equivalent     | Common Name          | Gwynt y Mor Offshore Wind Farm                                                                                                     |
| Equivalent     | 4C-Offshore ID       | [gwynt-y-môr-united-kingdom-uk09](https://www.4coffshore.com/windfarms/united-kingdom/gwynt-y-môr-united-kingdom-uk09.html)        |
| Equivalent     | WindPowerNet ID      | [windfarm_en_7389_gwynt-y-mor](https://www.thewindpower.net/windfarm_en_7389_gwynt-y-mor.php)                                      |
| Equivalent     | Wikidata ID          | [Q455472](https://www.wikidata.org/wiki/Q455472)                                                                                   |
| Equivalent     | Wikipedia ID         | [Gwynt_y_Mor](https://en.wikipedia.org/wiki/Gwynt_y_Mor)                                                                           |
| Equivalent     | Power-Technology ID  | [gwynt-y-mor-offshore-wind-farm-north-wales](https://www.power-technology.com/projects/gwynt-y-mor-offshore-wind-farm-north-wales) |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | GYMRO-15   | GYMRO-17   | GYMRO-26   | GYMRO-28   |
|:------------|:-----------|:-----------|:-----------|:-----------|
| Fuel Type   | WIND       | WIND       | WIND       | WIND       |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.58 |
| Latitude    |   53.46 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 98.0     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                    |
|:------------------------------------|:-------------------------------------------------------------------------|
| Installed Capacity (MW)             | 576.0                                                                    |
| Longitude                           | -3.6266                                                                  |
| Latitude                            | 53.454                                                                   |
| Primary Fuel Type                   | Wind                                                                     |
| Owner                               | RWE                                                                      |
| Source                              | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    |
| Estimated Annual Generation in 2017 | 1452.07                                                                  |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   GYMRO-15 |   GYMRO-17 |   GYMRO-26 |   GYMRO-28 |
|:--------------------|-------:|-----------:|-----------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 |  408364.89 |  406814.26 |  313351.76 |  459572.75 |
| Annual Output (MWh) |   2017 |  467193.33 |  472611.62 |  503849.85 |  510219.49 |
| Annual Output (MWh) |   2018 |  418797.51 |  424367.33 |  437280.87 |  446317.47 |
| Annual Output (MWh) |   2019 |  434458.82 |  422045.76 |  458049.31 |  432103.22 |
| Annual Output (MWh) |   2020 |  533674.62 |  369437.61 |  507664.42 |  493621.71 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   GYMRO-15 |   GYMRO-17 |   GYMRO-26 |   GYMRO-28 |
|:----------------------|-------:|-----------:|-----------:|-----------:|-----------:|
| Capture Price (£/MWh) |   2016 |      36.06 |      36.05 |      37.24 |      35.94 |
| Capture Price (£/MWh) |   2017 |      44.09 |      43.99 |      44.05 |      43.96 |
| Capture Price (£/MWh) |   2018 |      56.47 |      56.39 |      56.46 |      56.29 |
| Capture Price (£/MWh) |   2019 |      39.71 |      39.67 |      39.63 |      40.22 |
| Capture Price (£/MWh) |   2020 |      31.99 |      27.82 |      31.17 |      31.72 |

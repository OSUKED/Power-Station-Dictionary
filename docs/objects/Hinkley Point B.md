### Identifiers

| Relationship   | ID Type              | ID(s)                              |
|:---------------|:---------------------|:-----------------------------------|
| Root           | OSUKED ID            | 10133                              |
| Related        | Settlement BMU ID    | T_HINB-7, T_HINB-8                 |
| Related        | National Grid BMU ID | HINB-7, HINB-8                     |
| Related        | EIC ID               | 48W000000HINB-77, 48W000000HINB-85 |
| Equivalent     | GPPD ID              | GBR1000056                         |
| Equivalent     | ESAIL ID             | HINB                               |
| Equivalent     | Common Name          | Hinkley Point B                    |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | HINB-7   | HINB-8   |
|:------------|:---------|:---------|
| Fuel Type   | NUCLEAR  | NUCLEAR  |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.32 |
| Latitude    |   51.14 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 955.0                                                                          |
| Longitude                           | -3.1334                                                                        |
| Latitude                            | 51.2085                                                                        |
| Primary Fuel Type                   | Nuclear                                                                        |
| Owner                               | British Energy (now part of EDF)                                               |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1024529.0                                                                      |
| Estimated Annual Generation in 2017 | 6310.68                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     HINB-7 |     HINB-8 |
|:--------------------|-------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 3343685.25 | 4139550.78 |
| Annual Output (MWh) |   2017 | 3922398.88 | 3607201.71 |
| Annual Output (MWh) |   2018 | 3845394.99 | 3296463.88 |
| Annual Output (MWh) |   2019 | 3069859.16 | 4095906.31 |
| Annual Output (MWh) |   2020 | 1358961.70 |  588252.28 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   HINB-7 |   HINB-8 |
|:----------------------|-------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    40.16 |    38.93 |
| Capture Price (£/MWh) |   2017 |    44.71 |    45.37 |
| Capture Price (£/MWh) |   2018 |    57.32 |    58.27 |
| Capture Price (£/MWh) |   2019 |    42.13 |    41.74 |
| Capture Price (£/MWh) |   2020 |    27.24 |    32.37 |

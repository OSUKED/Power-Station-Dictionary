### Identifiers

| Relationship   | ID Type              | ID(s)                                  |
|:---------------|:---------------------|:---------------------------------------|
| Root           | OSUKED ID            | 10136                                  |
| Related        | Settlement BMU ID    | T_SIZEA1, T_SIZEA2, T_SIZB-1, T_SIZB-2 |
| Related        | National Grid BMU ID | SIZB-1, SIZB-2                         |
| Related        | EIC ID               | 48W000000SIZB-1U, 48W000000SIZB-2S     |
| Equivalent     | GPPD ID              | GBR1000058                             |
| Equivalent     | ESAIL ID             | SIZ                                    |
| Equivalent     | Common Name          | Sizewell                               |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | SIZB-1   | SIZB-2   |
|:------------|:---------|:---------|
| Fuel Type   | NUCLEAR  | NUCLEAR  |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    1.62 |
| Latitude    |   52.22 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 1198.0                                                                         |
| Longitude                           | 1.6206                                                                         |
| Latitude                            | 52.2145                                                                        |
| Primary Fuel Type                   | Nuclear                                                                        |
| Owner                               | British Energy (now part of EDF)                                               |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1024533.0                                                                      |
| Annual Generation in 2015           | 7416.812                                                                       |
| Generation Source                   | JRC-PPDB-OPEN                                                                  |
| Estimated Annual Generation in 2017 | 7916.43                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     SIZB-1 |     SIZB-2 |
|:--------------------|-------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 4302033.49 | 4315374.01 |
| Annual Output (MWh) |   2017 | 4404928.63 | 4396461.33 |
| Annual Output (MWh) |   2018 | 4527418.77 | 4386923.29 |
| Annual Output (MWh) |   2019 | 4269543.83 | 4182403.15 |
| Annual Output (MWh) |   2020 | 4618171.89 | 3807720.69 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   SIZB-1 |   SIZB-2 |
|:----------------------|-------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    39.92 |    39.87 |
| Capture Price (£/MWh) |   2017 |    43.20 |    43.23 |
| Capture Price (£/MWh) |   2018 |    57.67 |    56.66 |
| Capture Price (£/MWh) |   2019 |    42.13 |    42.25 |
| Capture Price (£/MWh) |   2020 |    34.21 |    35.35 |

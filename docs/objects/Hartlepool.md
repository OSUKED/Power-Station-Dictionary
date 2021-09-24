### Identifiers

| Relationship   | ID Type              | ID(s)                              |
|:---------------|:---------------------|:-----------------------------------|
| Root           | OSUKED ID            | 10130                              |
| Related        | Settlement BMU ID    | T_HRTL-1, T_HRTL-2                 |
| Related        | National Grid BMU ID | HRTL-1, HRTL-2                     |
| Related        | EIC ID               | 48W000000HRTL-16, 48W000000HRTL-24 |
| Equivalent     | GPPD ID              | GBR1000053                         |
| Equivalent     | ESAIL ID             | HRTL                               |
| Equivalent     | Common Name          | Hartlepool                         |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | HRTL-1   | HRTL-2   |
|:------------|:---------|:---------|
| Fuel Type   | NUCLEAR  | NUCLEAR  |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -1.10 |
| Latitude    |   54.69 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 1180.0                                                                         |
| Longitude                           | -1.1801                                                                        |
| Latitude                            | 54.6341                                                                        |
| Primary Fuel Type                   | Nuclear                                                                        |
| Owner                               | British Energy (now part of EDF)                                               |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1024527.0                                                                      |
| Estimated Annual Generation in 2017 | 7797.48                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     HRTL-1 |     HRTL-2 |
|:--------------------|-------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 2844227.62 | 3789609.23 |
| Annual Output (MWh) |   2017 | 4687275.28 | 4657633.83 |
| Annual Output (MWh) |   2018 | 3340763.34 | 4395132.92 |
| Annual Output (MWh) |   2019 | 4366321.18 | 3292799.10 |
| Annual Output (MWh) |   2020 | 4594907.03 | 3945040.62 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   HRTL-1 |   HRTL-2 |
|:----------------------|-------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    39.89 |    40.10 |
| Capture Price (£/MWh) |   2017 |    44.73 |    44.10 |
| Capture Price (£/MWh) |   2018 |    57.91 |    56.20 |
| Capture Price (£/MWh) |   2019 |    41.46 |    44.37 |
| Capture Price (£/MWh) |   2020 |    34.10 |    33.28 |

### Identifiers

| Relationship   | ID Type              | ID(s)                                                                  |
|:---------------|:---------------------|:-----------------------------------------------------------------------|
| Root           | OSUKED ID            | 10125                                                                  |
| Related        | Settlement BMU ID    | M_SLOY-1, T_SLOY-2, T_SLOY-3, M_SLOY-4                                 |
| Related        | National Grid BMU ID | SLOY-1, SLOY-2, SLOY-3, SLOY-4                                         |
| Related        | EIC ID               | 48W000000SLOY-1C, 48W000000SLOY-2A, 48W000000SLOY-38, 48W000000SLOY-46 |
| Equivalent     | GPPD ID              | GBR1000404                                                             |
| Equivalent     | ESAIL ID             | SLOY                                                                   |
| Equivalent     | Common Name          | Sloy G                                                                 |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | SLOY-1   | SLOY-2   | SLOY-3   | SLOY-4   |
|:------------|:---------|:---------|:---------|:---------|
| Fuel Type   | NPSHYD   | NPSHYD   | NPSHYD   | NPSHYD   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -4.74 |
| Latitude    |   56.20 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 152.5                                                                          |
| Longitude                           | -4.7117                                                                        |
| Latitude                            | 56.2512                                                                        |
| Primary Fuel Type                   | Hydro                                                                          |
| Owner                               | Scottish and Southern: Hydro Schemes - Sloy/Awe                                |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1028346.0                                                                      |
| Estimated Annual Generation in 2013 | 436.89                                                                         |
| Estimated Annual Generation in 2014 | 288.23                                                                         |
| Estimated Annual Generation in 2015 | 562.34                                                                         |
| Estimated Annual Generation in 2016 | 347.17                                                                         |
| Estimated Annual Generation in 2017 | 351.45                                                                         |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   SLOY-1 |   SLOY-2 |   SLOY-3 |   SLOY-4 |
|:--------------------|-------:|---------:|---------:|---------:|---------:|
| Annual Output (MWh) |   2016 | 43059.75 | 43079.86 |  4313.43 | 31155.19 |
| Annual Output (MWh) |   2017 | 18951.86 | 69213.48 |  2314.96 | 53166.78 |
| Annual Output (MWh) |   2018 | 49170.32 | 14568.67 | 31056.31 | 37817.43 |
| Annual Output (MWh) |   2019 | 43686.32 | 41834.88 | 23601.27 | 15493.68 |
| Annual Output (MWh) |   2020 | 43014.26 | 45239.79 | 43840.69 | 19604.59 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   SLOY-1 |   SLOY-2 |   SLOY-3 |   SLOY-4 |
|:----------------------|-------:|---------:|---------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    61.09 |    61.79 |    74.74 |    62.91 |
| Capture Price (£/MWh) |   2017 |    62.08 |    56.03 |    68.53 |    55.85 |
| Capture Price (£/MWh) |   2018 |    72.41 |    80.49 |    72.72 |    72.67 |
| Capture Price (£/MWh) |   2019 |    52.06 |    51.92 |    46.75 |    58.51 |
| Capture Price (£/MWh) |   2020 |    47.37 |    47.60 |    47.57 |    52.64 |

### Identifiers

| Relationship   | ID Type              | ID(s)                                                                  |
|:---------------|:---------------------|:-----------------------------------------------------------------------|
| Root           | OSUKED ID            | 10131                                                                  |
| Related        | GPPD ID              | GBR1000054, GBR1000055                                                 |
| Related        | Settlement BMU ID    | T_HEYM11, T_HEYM12, T_HEYM27, T_HEYM28                                 |
| Related        | National Grid BMU ID | HEYM11, HEYM12, HEYM27, HEYM28                                         |
| Related        | EIC ID               | 48W000000HEYM11C, 48W000000HEYM12A, 48W000000HEYM27Y, 48W000000HEYM28W |
| Equivalent     | ESAIL ID             | HEYM                                                                   |
| Equivalent     | Common Name          | Heysham                                                                |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | HEYM11   | HEYM12   | HEYM27   | HEYM28   |
|:------------|:---------|:---------|:---------|:---------|
| Fuel Type   | NUCLEAR  | NUCLEAR  | NUCLEAR  | NUCLEAR  |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -2.92 |
| Latitude    |   54.03 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | GBR1000054                                                                     | GBR1000055                                                                     |
|:------------------------------------|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| Annual Generation in 2017           | NaN                                                                            | 10498.819                                                                      |
| Estimated Annual Generation in 2017 | 7632.28                                                                        | 8127.89                                                                        |
| Generation Source                   | None                                                                           | JRC-PPDB-OPEN                                                                  |
| Geolocation Source                  | GEODB                                                                          | GEODB                                                                          |
| Installed Capacity (MW)             | 1155.0                                                                         | 1230.0                                                                         |
| Latitude                            | 54.0285                                                                        | 54.0285                                                                        |
| Longitude                           | -2.916                                                                         | -2.916                                                                         |
| Owner                               | British Energy (now part of EDF)                                               | British Energy (now part of EDF)                                               |
| PLATTS-WEPP ID                      | 1024528.0                                                                      | 1043124.0                                                                      |
| Primary Fuel Type                   | Nuclear                                                                        | Nuclear                                                                        |
| Source                              | Department for Business Energy & Industrial Strategy                           | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     HEYM11 |     HEYM12 |     HEYM27 |     HEYM28 |
|:--------------------|-------:|-----------:|-----------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 3480423.32 | 4129181.00 | 5514342.67 | 4498838.44 |
| Annual Output (MWh) |   2017 | 3058936.44 | 3298364.99 | 5281604.15 | 5427790.74 |
| Annual Output (MWh) |   2018 | 3687412.07 | 3400931.94 | 3985949.81 | 5136322.86 |
| Annual Output (MWh) |   2019 | 3597733.01 | 3267867.54 | 5492781.37 | 5225327.81 |
| Annual Output (MWh) |   2020 | 2678400.76 | 3488480.84 | 5201481.44 | 4160665.54 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   HEYM11 |   HEYM12 |   HEYM27 |   HEYM28 |
|:----------------------|-------:|---------:|---------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    38.97 |    38.32 |    38.86 |    36.51 |
| Capture Price (£/MWh) |   2017 |    45.59 |    43.65 |    44.40 |    44.74 |
| Capture Price (£/MWh) |   2018 |    57.03 |    56.97 |    57.40 |    56.97 |
| Capture Price (£/MWh) |   2019 |    41.83 |    40.46 |    41.82 |    41.73 |
| Capture Price (£/MWh) |   2020 |    29.58 |    33.46 |    34.21 |    35.40 |

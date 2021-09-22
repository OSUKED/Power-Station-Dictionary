### Identifiers

| Relationship   | ID Type     | ID(s)                                                                                             |
|:---------------|:------------|:--------------------------------------------------------------------------------------------------|
| root           | osuked_id   | 10014                                                                                             |
| element-of     | gppd_idnr   | GBR1000143, GBR1000146, GBR1000141                                                                |
| element-of     | sett_bmu_id | T_WBUPS-1, T_WBUPS-2, T_WBUPS-3, T_WBUPS-4, T_WBUGT-1, T_WBUGT-4, T_WBURB-1, T_WBURB-2, T_WBURB-3 |
| element-of     | ngc_bmu_id  | WBUPS-1, WBUPS-2, WBUPS-3, WBUPS-4, WBUGT-1, WBUGT-4, WBURB-1, WBURB-2, WBURB-3                   |
| element-of     | eutl_id     | 97220, 97223                                                                                      |
| same-as        | esail_id    | WBU                                                                                               |
| same-as        | name        | West Burton                                                                                       |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.54 |
| Latitude    |   53.36 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | GBR1000141                                                                     | GBR1000143                                                                     | GBR1000146                                                                     |
|:------------------------------------|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| Estimated Annual Generation in 2017 | 6180.55                                                                        | 3056.2                                                                         | 185.6                                                                          |
| Geolocation Source                  | GEODB                                                                          | GEODB                                                                          | GEODB                                                                          |
| Installed Capacity (MW)             | 1332.0                                                                         | 2012.0                                                                         | 40.0                                                                           |
| Latitude                            | 53.3631                                                                        | 53.3604                                                                        | 53.3631                                                                        |
| Longitude                           | -0.7976                                                                        | -0.8102                                                                        | -0.7976                                                                        |
| Owner                               | EDF Energy                                                                     | EDF Energy                                                                     | EDF Energy                                                                     |
| PLATTS-WEPP ID                      | NaN                                                                            | 1013947.0                                                                      | NaN                                                                            |
| Primary Fuel Type                   | Gas                                                                            | Coal                                                                           | Gas                                                                            |
| Source                              | Department for Business Energy & Industrial Strategy                           | Department for Business Energy & Industrial Strategy                           | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |       97220 |      97223 |
|:-----------------------|-------:|------------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 |  8419658.00 |     nan    |
| CO2 Emissions (Tonnes) |   2006 |  8900616.00 |     nan    |
| CO2 Emissions (Tonnes) |   2007 |  9324306.00 |     nan    |
| CO2 Emissions (Tonnes) |   2008 |  9650932.00 |     nan    |
| CO2 Emissions (Tonnes) |   2009 |  7165862.00 |     nan    |
| CO2 Emissions (Tonnes) |   2010 |  5095438.00 |     nan    |
| CO2 Emissions (Tonnes) |   2011 |  6075254.00 |     nan    |
| CO2 Emissions (Tonnes) |   2012 | 10780107.00 |  187209.00 |
| CO2 Emissions (Tonnes) |   2013 | 10887300.00 | 1057877.00 |
| CO2 Emissions (Tonnes) |   2014 |  9208141.00 | 1842770.00 |
| CO2 Emissions (Tonnes) |   2015 |  7724207.00 | 2371371.00 |
| CO2 Emissions (Tonnes) |   2016 |  1165058.00 | 2029550.00 |
| CO2 Emissions (Tonnes) |   2017 |  1766100.00 | 2491134.00 |
| CO2 Emissions (Tonnes) |   2018 |  1679509.00 | 2573845.00 |
| CO2 Emissions (Tonnes) |   2019 |   790510.00 | 2380046.00 |
| CO2 Emissions (Tonnes) |   2020 |  1051651.00 | 1884207.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   WBUGT-1 |   WBUGT-4 |   WBUPS-1 |   WBUPS-2 |   WBUPS-3 |   WBUPS-4 |    WBURB-1 |    WBURB-2 |    WBURB-3 |
|:--------------------|-------:|----------:|----------:|----------:|----------:|----------:|----------:|-----------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 |    186.72 |    169.99 | 592424.56 | 354748.10 | 187014.18 | 129540.05 | 1706126.97 | 1642701.23 | 2021024.86 |
| Annual Output (MWh) |   2017 |     82.35 |    144.94 | 402301.49 | 711833.18 | 314437.84 | 349876.93 | 2392300.40 | 2242933.08 | 1964802.69 |
| Annual Output (MWh) |   2018 |    104.64 |     95.98 | 519811.99 | 541613.80 | 430122.78 | 357744.20 | 2124136.35 | 2181429.43 | 2254553.38 |
| Annual Output (MWh) |   2019 |     76.57 |     83.02 | 289630.32 | 244591.61 |  90731.24 | 198909.25 | 2089622.96 | 2254585.70 | 1865873.09 |
| Annual Output (MWh) |   2020 |    115.74 |    112.29 | 398596.37 | 338453.17 | 143891.61 | 355083.92 | 1660112.92 | 1325122.71 | 1892671.17 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | WBUGT-1   | WBUGT-4   | WBUPS-1   | WBUPS-2   | WBUPS-3   | WBUPS-4   | WBURB-1   | WBURB-2   | WBURB-3   |
|:------------|:----------|:----------|:----------|:----------|:----------|:----------|:----------|:----------|:----------|
| Fuel Type   | OCGT      | OCGT      | COAL      | COAL      | COAL      | COAL      | CCGT      | CCGT      | CCGT      |

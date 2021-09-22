### Identifiers

| Relationship   | ID Type     | ID(s)            |
|:---------------|:------------|:-----------------|
| root           | osuked_id   | 10091            |
| element-of     | sett_bmu_id | E_COWE1, E_COWE2 |
| element-of     | ngc_bmu_id  | COWE1, COWE2     |
| same-as        | gppd_idnr   | GBR1000376       |
| same-as        | esail_id    | COWE             |
| same-as        | name        | Cowes            |
| same-as        | eutl_id     | 97160            |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -1.29 |
| Latitude    |   50.75 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 140.0                                                                          |
| Longitude                           | -1.2862                                                                        |
| Latitude                            | 50.7469                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | RWE Npower Plc                                                                 |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1023587.0                                                                      |
| Estimated Annual Generation in 2017 | 649.6                                                                          |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |   Value |
|:-----------------------|-------:|--------:|
| CO2 Emissions (Tonnes) |   2005 | 4765.00 |
| CO2 Emissions (Tonnes) |   2006 | 7012.00 |
| CO2 Emissions (Tonnes) |   2007 | 3289.00 |
| CO2 Emissions (Tonnes) |   2008 | 6106.00 |
| CO2 Emissions (Tonnes) |   2009 | 4225.00 |
| CO2 Emissions (Tonnes) |   2010 | 1463.00 |
| CO2 Emissions (Tonnes) |   2011 | 2392.00 |
| CO2 Emissions (Tonnes) |   2012 | 2628.00 |
| CO2 Emissions (Tonnes) |   2013 | 1122.00 |
| CO2 Emissions (Tonnes) |   2014 | 1621.00 |
| CO2 Emissions (Tonnes) |   2015 | 2224.00 |
| CO2 Emissions (Tonnes) |   2016 | 6094.00 |
| CO2 Emissions (Tonnes) |   2017 | 4902.00 |
| CO2 Emissions (Tonnes) |   2018 | 4070.00 |
| CO2 Emissions (Tonnes) |   2019 |  651.00 |
| CO2 Emissions (Tonnes) |   2020 | 1158.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   COWE1 |   COWE2 |
|:--------------------|-------:|--------:|--------:|
| Annual Output (MWh) |   2016 | 2762.63 | 2678.79 |
| Annual Output (MWh) |   2017 | 2204.29 | 2194.66 |
| Annual Output (MWh) |   2018 | 1827.45 | 1841.93 |
| Annual Output (MWh) |   2019 |  262.12 |  324.32 |
| Annual Output (MWh) |   2020 |  282.78 |  300.40 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | COWE1   | COWE2   |
|:------------|:--------|:--------|
| Fuel Type   | OCGT    | OCGT    |

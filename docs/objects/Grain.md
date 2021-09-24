### Identifiers

| Relationship   | ID Type              | ID(s)                                                                |
|:---------------|:---------------------|:---------------------------------------------------------------------|
| Root           | OSUKED ID            | 10067                                                                |
| Related        | GPPD ID              | GBR1000495, GBR1000497                                               |
| Related        | Settlement BMU ID    | T_GRAI-6, T_GRAI-7, T_GRAI-8, T_GRAI-1, T_GRAI-2, T_GRAI-3, T_GRAI-4 |
| Related        | National Grid BMU ID | GRAI-6, GRAI-7, GRAI-8, GRAI-1, GRAI-2, GRAI-3, GRAI-4               |
| Related        | EIC ID               | 48W100000GRAI-6N, 48W000000GRAI-7Y, 48W000000GRAI-8W                 |
| Equivalent     | ESAIL ID             | GRAI                                                                 |
| Equivalent     | Common Name          | Grain                                                                |
| Equivalent     | EUTL ID              | 97061                                                                |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | GRAI-6   | GRAI-7   | GRAI-8   |
|:------------|:---------|:---------|:---------|
| Fuel Type   | CCGT     | CCGT     | CCGT     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    0.70 |
| Latitude    |   51.47 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | GBR1000495                                                                     | GBR1000497                                                                     |
|:------------------------------------|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| Estimated Annual Generation in 2017 | NaN                                                                            | 259.84                                                                         |
| Geolocation Source                  | GEODB                                                                          | GEODB                                                                          |
| Installed Capacity (MW)             | 1404.0                                                                         | 56.0                                                                           |
| Latitude                            | 51.4444                                                                        | 51.4444                                                                        |
| Longitude                           | 0.7114                                                                         | 0.7114                                                                         |
| Owner                               | Uniper UK Limited                                                              | Uniper UK Limited                                                              |
| PLATTS-WEPP ID                      | 1025719.0                                                                      | 1025719.0                                                                      |
| Primary Fuel Type                   | Cogeneration                                                                   | Gas                                                                            |
| Source                              | Department for Business Energy & Industrial Strategy                           | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2010 |  301362.00 |
| CO2 Emissions (Tonnes) |   2011 | 1879635.00 |
| CO2 Emissions (Tonnes) |   2012 | 2079280.00 |
| CO2 Emissions (Tonnes) |   2013 | 2064010.00 |
| CO2 Emissions (Tonnes) |   2014 | 2070438.00 |
| CO2 Emissions (Tonnes) |   2015 | 1605023.00 |
| CO2 Emissions (Tonnes) |   2016 | 2517282.00 |
| CO2 Emissions (Tonnes) |   2017 | 1829480.00 |
| CO2 Emissions (Tonnes) |   2018 | 1993264.00 |
| CO2 Emissions (Tonnes) |   2019 | 2438552.00 |
| CO2 Emissions (Tonnes) |   2020 | 2092636.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     GRAI-6 |     GRAI-7 |     GRAI-8 |
|:--------------------|-------:|-----------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 1861352.50 | 2530987.95 | 2612216.15 |
| Annual Output (MWh) |   2017 | 2227078.70 | 1835166.35 | 1000015.10 |
| Annual Output (MWh) |   2018 | 1658217.45 | 2040196.25 | 1664214.90 |
| Annual Output (MWh) |   2019 | 2486031.80 | 2158208.45 | 1992926.45 |
| Annual Output (MWh) |   2020 | 2355828.50 | 1784480.25 | 1577418.40 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   GRAI-6 |   GRAI-7 |   GRAI-8 |
|:----------------------|-------:|---------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    44.19 |    41.69 |    42.06 |
| Capture Price (£/MWh) |   2017 |    47.33 |    48.78 |    51.86 |
| Capture Price (£/MWh) |   2018 |    59.84 |    59.23 |    60.00 |
| Capture Price (£/MWh) |   2019 |    44.56 |    45.50 |    46.23 |
| Capture Price (£/MWh) |   2020 |    36.70 |    39.28 |    38.80 |

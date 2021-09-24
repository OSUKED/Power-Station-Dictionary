### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                      |
|:---------------|:---------------------|:-----------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10011                                                                                                      |
| Related        | Settlement BMU ID    | T_RATS-1, T_RATS-2, T_RATS-3, T_RATS-4, T_RATSGT-2, T_RATSGT-4                                             |
| Related        | National Grid BMU ID | RATS-1, RATS-2, RATS-3, RATS-4, RATSGT-2, RATSGT-4                                                         |
| Related        | EIC ID               | 48W000000RATS-1A, 48W000000RATS-28, 48W000000RATS-36, 48W000000RATS-44, 48W0000RATSGT-2V, 48W0000RATSGT-4R |
| Equivalent     | GPPD ID              | GBR1000496                                                                                                 |
| Equivalent     | ESAIL ID             | RATS                                                                                                       |
| Equivalent     | Common Name          | Ratcliffe on Soar                                                                                          |
| Equivalent     | EUTL ID              | 97052                                                                                                      |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | RATS-1   | RATS-2   | RATS-3   | RATS-4   | RATSGT-2   | RATSGT-4   |
|:------------|:---------|:---------|:---------|:---------|:-----------|:-----------|
| Fuel Type   | COAL     | COAL     | COAL     | COAL     | OCGT       | OCGT       |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -1.22 |
| Latitude    |   52.86 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 2000.0                                                                         |
| Longitude                           | -1.255                                                                         |
| Latitude                            | 52.8653                                                                        |
| Primary Fuel Type                   | Coal                                                                           |
| Owner                               | Uniper UK Limited                                                              |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1025731.0                                                                      |
| Estimated Annual Generation in 2017 | 3037.98                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |       Value |
|:-----------------------|-------:|------------:|
| CO2 Emissions (Tonnes) |   2005 |  8638887.00 |
| CO2 Emissions (Tonnes) |   2006 |  7812287.00 |
| CO2 Emissions (Tonnes) |   2007 |  9028906.00 |
| CO2 Emissions (Tonnes) |   2008 |  9901175.00 |
| CO2 Emissions (Tonnes) |   2009 |  7608926.00 |
| CO2 Emissions (Tonnes) |   2010 |  8363125.00 |
| CO2 Emissions (Tonnes) |   2011 |  7833954.00 |
| CO2 Emissions (Tonnes) |   2012 |  9998425.00 |
| CO2 Emissions (Tonnes) |   2013 | 11007539.00 |
| CO2 Emissions (Tonnes) |   2014 |  9222895.00 |
| CO2 Emissions (Tonnes) |   2015 |  4774148.00 |
| CO2 Emissions (Tonnes) |   2016 |  2672086.00 |
| CO2 Emissions (Tonnes) |   2017 |  2448591.00 |
| CO2 Emissions (Tonnes) |   2018 |  3333500.00 |
| CO2 Emissions (Tonnes) |   2019 |   728543.00 |
| CO2 Emissions (Tonnes) |   2020 |   439721.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    RATS-1 |    RATS-2 |     RATS-3 |    RATS-4 |   RATSGT-2 |   RATSGT-4 |
|:--------------------|-------:|----------:|----------:|-----------:|----------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 641566.26 | 871724.18 |  799338.82 | 451402.96 |     257.14 |     257.31 |
| Annual Output (MWh) |   2017 | 579054.32 | 579079.39 |  819821.58 | 585991.20 |     325.96 |     216.36 |
| Annual Output (MWh) |   2018 | 651460.58 | 810001.52 | 1222750.22 | 877622.67 |     181.07 |     213.65 |
| Annual Output (MWh) |   2019 | 220609.67 | 158445.22 |  141512.88 | 223333.13 |     102.47 |      89.94 |
| Annual Output (MWh) |   2020 | 147261.86 | 114266.93 |   82837.13 | 114534.07 |     351.82 |     322.07 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   RATS-1 |   RATS-2 |   RATS-3 |   RATS-4 |   RATSGT-2 |   RATSGT-4 |
|:----------------------|-------:|---------:|---------:|---------:|---------:|-----------:|-----------:|
| Capture Price (£/MWh) |   2016 |    52.96 |    50.15 |    51.69 |    59.71 |     215.92 |     213.23 |
| Capture Price (£/MWh) |   2017 |    53.74 |    52.42 |    52.60 |    56.58 |      91.09 |     122.62 |
| Capture Price (£/MWh) |   2018 |    69.38 |    66.83 |    65.05 |    65.96 |     107.08 |      97.77 |
| Capture Price (£/MWh) |   2019 |    63.43 |    66.24 |    67.78 |    62.46 |      51.42 |      71.28 |
| Capture Price (£/MWh) |   2020 |    68.29 |    72.94 |    62.64 |    70.35 |     154.79 |     149.44 |

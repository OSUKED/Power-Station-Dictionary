### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                                  |
|:---------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10001                                                                                                                                  |
| Related        | GPPD ID              | GBR1000377, GBR1000369                                                                                                                 |
| Related        | Settlement BMU ID    | T_DIDC1, T_DIDC2, T_DIDC4, T_DIDC3, T_DIDC1G, T_DIDC2G, T_DIDC3G, T_DIDC4G, E_DIDC1G, E_DIDC2G, E_DIDC3G, E_DIDC4G, T_DIDCB5, T_DIDCB6 |
| Related        | National Grid BMU ID | DIDC1, DIDC2, DIDC4, DIDC3, DIDC1G, DIDC2G, DIDC3G, DIDC4G, DIDC01G, DIDC02G, DIDC03G, DIDC04G, DIDCB5, DIDCB6                         |
| Related        | EIC ID               | 48W00000DIDC01G1, 48W00000DIDC02GZ, 48W00000DIDC03GW, 48W00000DIDC04GT, 48W000000DIDCB5C, 48W000000DIDCB6A                             |
| Equivalent     | ESAIL ID             | DIDC                                                                                                                                   |
| Equivalent     | Common Name          | Didcot                                                                                                                                 |
| Equivalent     | EUTL ID              | 97165                                                                                                                                  |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | DIDC01G   | DIDC02G   | DIDC03G   | DIDC04G   | DIDCB5   | DIDCB6   |
|:------------|:----------|:----------|:----------|:----------|:---------|:---------|
| Fuel Type   | OCGT      | OCGT      | OCGT      | OCGT      | CCGT     | CCGT     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -1.27 |
| Latitude    |   51.62 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | GBR1000369                                                                     | GBR1000377                                                                     |
|:------------------------------------|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| Estimated Annual Generation in 2017 | 6820.88                                                                        | 464.0                                                                          |
| Geolocation Source                  | GEODB                                                                          | GEODB                                                                          |
| Installed Capacity (MW)             | 1470.0                                                                         | 100.0                                                                          |
| Latitude                            | 51.6246                                                                        | 51.6246                                                                        |
| Longitude                           | -1.2683                                                                        | -1.2683                                                                        |
| Owner                               | RWE Npower Plc                                                                 | RWE Npower Plc                                                                 |
| PLATTS-WEPP ID                      | 1023591.0                                                                      | NaN                                                                            |
| Primary Fuel Type                   | Gas                                                                            | Gas                                                                            |
| Source                              | Department for Business Energy & Industrial Strategy                           | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 6342700.00 |
| CO2 Emissions (Tonnes) |   2006 | 7184281.00 |
| CO2 Emissions (Tonnes) |   2007 | 5231425.00 |
| CO2 Emissions (Tonnes) |   2008 | 5182660.00 |
| CO2 Emissions (Tonnes) |   2009 | 2435748.00 |
| CO2 Emissions (Tonnes) |   2010 | 1795512.00 |
| CO2 Emissions (Tonnes) |   2011 | 2181952.00 |
| CO2 Emissions (Tonnes) |   2012 | 6838317.00 |
| CO2 Emissions (Tonnes) |   2013 | 1737804.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   DIDC01G |   DIDC02G |   DIDC03G |   DIDC04G |     DIDCB5 |     DIDCB6 |
|:--------------------|-------:|----------:|----------:|----------:|----------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 |    805.51 |    895.90 |    906.59 |    904.72 | 3740564.95 | 2394716.10 |
| Annual Output (MWh) |   2017 |    587.93 |    703.78 |    576.75 |    542.08 | 3708766.45 | 2757882.40 |
| Annual Output (MWh) |   2018 |   1303.64 |   1265.48 |   1292.14 |   1286.47 | 3323661.45 | 2702690.75 |
| Annual Output (MWh) |   2019 |   1453.08 |   1499.91 |   1336.45 |   1440.01 | 4285470.60 | 2092243.40 |
| Annual Output (MWh) |   2020 |    807.00 |    624.05 |    773.35 |    803.66 | 2676611.45 | 1968618.25 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   DIDC01G |   DIDC02G |   DIDC03G |   DIDC04G |   DIDCB5 |   DIDCB6 |
|:----------------------|-------:|----------:|----------:|----------:|----------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |     56.46 |     71.32 |     72.23 |     72.16 |    41.98 |    41.93 |
| Capture Price (£/MWh) |   2017 |     98.86 |     91.04 |    100.68 |    103.89 |    47.52 |    47.94 |
| Capture Price (£/MWh) |   2018 |    102.70 |    103.01 |    102.71 |    102.30 |    60.27 |    61.00 |
| Capture Price (£/MWh) |   2019 |     71.04 |     70.73 |     71.19 |     70.56 |    44.50 |    46.14 |
| Capture Price (£/MWh) |   2020 |     66.35 |     71.81 |     67.77 |     66.32 |    41.10 |    41.88 |

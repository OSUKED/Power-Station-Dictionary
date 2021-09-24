### Identifiers

| Relationship   | ID Type              | ID(s)                              |
|:---------------|:---------------------|:-----------------------------------|
| Root           | OSUKED ID            | 10056                              |
| Related        | Settlement BMU ID    | T_SHBA-1, T_SHBA-2                 |
| Related        | National Grid BMU ID | SHBA-1, SHBA-2                     |
| Related        | EIC ID               | 48W000000SHBA-1C, 48W000000SHBA-2A |
| Equivalent     | GPPD ID              | GBR1000074                         |
| Equivalent     | ESAIL ID             | SHBA                               |
| Equivalent     | Common Name          | South Humber Bank                  |
| Equivalent     | EUTL ID              | 96979                              |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | SHBA-1   | SHBA-2   |
|:------------|:---------|:---------|
| Fuel Type   | CCGT     | CCGT     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.13 |
| Latitude    |   53.62 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 1310.0                                                                         |
| Longitude                           | -0.1446                                                                        |
| Latitude                            | 53.6008                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | Centrica                                                                       |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1018950.0                                                                      |
| Estimated Annual Generation in 2017 | 6078.47                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 2935989.00 |
| CO2 Emissions (Tonnes) |   2006 | 2303221.00 |
| CO2 Emissions (Tonnes) |   2007 | 3047981.00 |
| CO2 Emissions (Tonnes) |   2008 | 3044370.00 |
| CO2 Emissions (Tonnes) |   2009 | 3287536.00 |
| CO2 Emissions (Tonnes) |   2010 | 3443382.00 |
| CO2 Emissions (Tonnes) |   2011 | 1661335.00 |
| CO2 Emissions (Tonnes) |   2012 |  912777.00 |
| CO2 Emissions (Tonnes) |   2013 | 1094402.00 |
| CO2 Emissions (Tonnes) |   2014 | 1364050.00 |
| CO2 Emissions (Tonnes) |   2015 |  820991.00 |
| CO2 Emissions (Tonnes) |   2016 |  966065.00 |
| CO2 Emissions (Tonnes) |   2017 | 1117414.00 |
| CO2 Emissions (Tonnes) |   2018 | 1344908.00 |
| CO2 Emissions (Tonnes) |   2019 | 1992109.00 |
| CO2 Emissions (Tonnes) |   2020 | 2792113.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     SHBA-1 |     SHBA-2 |
|:--------------------|-------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 1351544.50 | 1145951.93 |
| Annual Output (MWh) |   2017 |  904306.94 | 1984081.22 |
| Annual Output (MWh) |   2018 | 1951090.73 | 1387370.54 |
| Annual Output (MWh) |   2019 | 2758954.68 | 2425564.20 |
| Annual Output (MWh) |   2020 | 4371847.57 | 2890134.29 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   SHBA-1 |   SHBA-2 |
|:----------------------|-------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    39.28 |    46.17 |
| Capture Price (£/MWh) |   2017 |    54.00 |    46.34 |
| Capture Price (£/MWh) |   2018 |    59.96 |    60.63 |
| Capture Price (£/MWh) |   2019 |    46.17 |    44.36 |
| Capture Price (£/MWh) |   2020 |    37.61 |    37.47 |

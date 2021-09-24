### Identifiers

| Relationship   | ID Type              | ID(s)                                                                  |
|:---------------|:---------------------|:-----------------------------------------------------------------------|
| Root           | OSUKED ID            | 10058                                                                  |
| Related        | Settlement BMU ID    | T_STAY-1, T_STAY-2, T_STAY-3, T_STAY-4                                 |
| Related        | National Grid BMU ID | STAY-1, STAY-2, STAY-3, STAY-4                                         |
| Related        | EIC ID               | 48W000000STAY-1Y, 48W000000STAY-2W, 48W000000STAY-3U, 48W000000STAY-4S |
| Equivalent     | GPPD ID              | GBR1000373                                                             |
| Equivalent     | ESAIL ID             | STAY                                                                   |
| Equivalent     | Common Name          | Staythorpe                                                             |
| Equivalent     | EUTL ID              | 97185                                                                  |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | STAY-1   | STAY-2   | STAY-3   | STAY-4   |
|:------------|:---------|:---------|:---------|:---------|
| Fuel Type   | CCGT     | CCGT     | CCGT     | CCGT     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.99 |
| Latitude    |   53.04 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 1772.0                                                                         |
| Longitude                           | -0.8585                                                                        |
| Latitude                            | 53.073                                                                         |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | RWE Npower Plc                                                                 |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1064569.0                                                                      |
| Estimated Annual Generation in 2017 | 8222.18                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2010 | 1389848.00 |
| CO2 Emissions (Tonnes) |   2011 | 3085875.00 |
| CO2 Emissions (Tonnes) |   2012 | 2939792.00 |
| CO2 Emissions (Tonnes) |   2013 | 2257412.00 |
| CO2 Emissions (Tonnes) |   2014 | 2694585.00 |
| CO2 Emissions (Tonnes) |   2015 | 3351616.00 |
| CO2 Emissions (Tonnes) |   2016 | 3648469.00 |
| CO2 Emissions (Tonnes) |   2017 | 2719755.00 |
| CO2 Emissions (Tonnes) |   2018 | 3004222.00 |
| CO2 Emissions (Tonnes) |   2019 | 3423908.00 |
| CO2 Emissions (Tonnes) |   2020 | 1882092.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     STAY-1 |     STAY-2 |     STAY-3 |     STAY-4 |
|:--------------------|-------:|-----------:|-----------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 2653380.60 | 2401438.20 | 2467320.95 | 2543956.50 |
| Annual Output (MWh) |   2017 | 2025452.70 | 1765678.55 | 2082050.55 | 1567359.90 |
| Annual Output (MWh) |   2018 | 1658011.45 | 2225584.00 | 2149710.35 | 1873607.35 |
| Annual Output (MWh) |   2019 | 2381620.95 | 2112564.25 | 2357037.00 | 2523223.15 |
| Annual Output (MWh) |   2020 | 1259669.20 | 1213780.50 | 1328482.75 | 1365182.45 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   STAY-1 |   STAY-2 |   STAY-3 |   STAY-4 |
|:----------------------|-------:|---------:|---------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    42.09 |    42.43 |    42.12 |    41.76 |
| Capture Price (£/MWh) |   2017 |    48.81 |    48.87 |    48.72 |    48.75 |
| Capture Price (£/MWh) |   2018 |    59.95 |    59.22 |    60.73 |    59.54 |
| Capture Price (£/MWh) |   2019 |    44.94 |    43.92 |    45.30 |    44.25 |
| Capture Price (£/MWh) |   2020 |    43.37 |    42.22 |    41.65 |    39.68 |

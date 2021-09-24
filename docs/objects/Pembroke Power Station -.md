### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                    |
|:---------------|:---------------------|:-----------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10047                                                                                    |
| Related        | Settlement BMU ID    | T_PEMB-11, T_PEMB-21, T_PEMB-31, T_PEMB-41, T_PEMB-51                                    |
| Related        | National Grid BMU ID | PEMB-11, PEMB-21, PEMB-31, PEMB-41, PEMB-51                                              |
| Related        | EIC ID               | 48W00000PEMB-11T, 48W00000PEMB-21Q, 48W00000PEMB-31N, 48W00000PEMB-41K, 48W00000PEMB-51H |
| Equivalent     | GPPD ID              | GBR1000372                                                                               |
| Equivalent     | ESAIL ID             | PEMB                                                                                     |
| Equivalent     | Common Name          | Pembroke Power Station -                                                                 |
| Equivalent     | EUTL ID              | 97190                                                                                    |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | PEMB-11   | PEMB-21   | PEMB-31   | PEMB-41   | PEMB-51   |
|:------------|:----------|:----------|:----------|:----------|:----------|
| Fuel Type   | CCGT      | CCGT      | CCGT      | CCGT      | CCGT      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -5.00 |
| Latitude    |   51.68 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 2180.0                                                                         |
| Longitude                           | -4.99                                                                          |
| Latitude                            | 51.685                                                                         |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | RWE Npower Plc                                                                 |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1023612.0                                                                      |
| Estimated Annual Generation in 2017 | 10115.32                                                                       |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2011 |    5618.00 |
| CO2 Emissions (Tonnes) |   2012 | 2858116.00 |
| CO2 Emissions (Tonnes) |   2013 | 3879335.00 |
| CO2 Emissions (Tonnes) |   2014 | 4313914.00 |
| CO2 Emissions (Tonnes) |   2015 | 3991210.00 |
| CO2 Emissions (Tonnes) |   2016 | 4912514.00 |
| CO2 Emissions (Tonnes) |   2017 | 4447649.00 |
| CO2 Emissions (Tonnes) |   2018 | 4568529.00 |
| CO2 Emissions (Tonnes) |   2019 | 4280280.00 |
| CO2 Emissions (Tonnes) |   2020 | 3753357.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    PEMB-11 |    PEMB-21 |    PEMB-31 |    PEMB-41 |    PEMB-51 |
|:--------------------|-------:|-----------:|-----------:|-----------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 2783249.65 | 2912821.45 | 3021636.95 | 2843192.05 | 2554706.30 |
| Annual Output (MWh) |   2017 | 2284091.35 | 2570000.20 | 2573527.55 | 2605875.30 | 2701804.70 |
| Annual Output (MWh) |   2018 | 2308706.00 | 2525643.55 | 2422640.20 | 2522703.70 | 2721002.90 |
| Annual Output (MWh) |   2019 | 2437444.75 | 2452962.40 | 2218824.35 | 2387369.90 | 2620250.00 |
| Annual Output (MWh) |   2020 | 2072749.35 | 2294991.90 | 2076274.90 | 2105766.15 | 2187708.35 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   PEMB-11 |   PEMB-21 |   PEMB-31 |   PEMB-41 |   PEMB-51 |
|:----------------------|-------:|----------:|----------:|----------:|----------:|----------:|
| Capture Price (£/MWh) |   2016 |     41.50 |     41.34 |     40.84 |     40.82 |     41.76 |
| Capture Price (£/MWh) |   2017 |     48.34 |     47.56 |     47.28 |     46.76 |     47.01 |
| Capture Price (£/MWh) |   2018 |     58.48 |     58.86 |     58.51 |     57.63 |     58.23 |
| Capture Price (£/MWh) |   2019 |     45.30 |     45.12 |     44.07 |     44.62 |     44.08 |
| Capture Price (£/MWh) |   2020 |     40.34 |     39.62 |     40.21 |     39.55 |     39.78 |

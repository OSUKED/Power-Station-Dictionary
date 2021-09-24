### Identifiers

| Relationship   | ID Type              | ID(s)                              |
|:---------------|:---------------------|:-----------------------------------|
| Root           | OSUKED ID            | 10054                              |
| Related        | Settlement BMU ID    | T_SVRP-10, T_SVRP-20               |
| Related        | National Grid BMU ID | SVRP-10, SVRP-20                   |
| Related        | EIC ID               | 48W00000SVRP-10A, 48W00000SVRP-207 |
| Equivalent     | GPPD ID              | GBR1000313                         |
| Equivalent     | ESAIL ID             | SVRP                               |
| Equivalent     | Common Name          | Severn Power                       |
| Equivalent     | EUTL ID              | 97635                              |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | SVRP-10   | SVRP-20   |
|:------------|:----------|:----------|
| Fuel Type   | CCGT      | CCGT      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.07 |
| Latitude    |   51.74 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 850.0                                                                          |
| Longitude                           | -2.975                                                                         |
| Latitude                            | 51.5475                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | MPF Operations Limited                                                         |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1063557.0                                                                      |
| Estimated Annual Generation in 2017 | 3944.04                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2010 |  482036.00 |
| CO2 Emissions (Tonnes) |   2011 | 1167005.00 |
| CO2 Emissions (Tonnes) |   2012 |  670971.00 |
| CO2 Emissions (Tonnes) |   2013 |  931074.00 |
| CO2 Emissions (Tonnes) |   2014 |  644874.00 |
| CO2 Emissions (Tonnes) |   2015 |  433278.00 |
| CO2 Emissions (Tonnes) |   2016 | 1428697.00 |
| CO2 Emissions (Tonnes) |   2017 | 1500909.00 |
| CO2 Emissions (Tonnes) |   2018 | 1179013.00 |
| CO2 Emissions (Tonnes) |   2019 |  716347.00 |
| CO2 Emissions (Tonnes) |   2020 |  431989.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    SVRP-10 |    SVRP-20 |
|:--------------------|-------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 1966638.80 | 1880999.80 |
| Annual Output (MWh) |   2017 | 2072655.20 | 1986155.85 |
| Annual Output (MWh) |   2018 | 1604429.55 | 1357534.95 |
| Annual Output (MWh) |   2019 | 1174701.90 |  674251.15 |
| Annual Output (MWh) |   2020 |  764775.25 |  368153.70 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   SVRP-10 |   SVRP-20 |
|:----------------------|-------:|----------:|----------:|
| Capture Price (£/MWh) |   2016 |     42.24 |     42.01 |
| Capture Price (£/MWh) |   2017 |     47.04 |     46.94 |
| Capture Price (£/MWh) |   2018 |     59.45 |     58.67 |
| Capture Price (£/MWh) |   2019 |     48.27 |     50.26 |
| Capture Price (£/MWh) |   2020 |     31.67 |     33.53 |

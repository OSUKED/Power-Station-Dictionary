### Identifiers

| Relationship   | ID Type              | ID(s)            |
|:---------------|:---------------------|:-----------------|
| Root           | OSUKED ID            | 10043            |
| Related        | Settlement BMU ID    | T_LAGA-1         |
| Related        | National Grid BMU ID | LAGA-1           |
| Equivalent     | GPPD ID              | GBR1000073       |
| Equivalent     | ESAIL ID             | LAGA             |
| Equivalent     | Common Name          | Langage          |
| Equivalent     | EUTL ID              | 97585            |
| Equivalent     | EIC ID               | 48W000000LAGA-14 |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | CCGT    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.97 |
| Latitude    |   50.49 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 905.0                                                                          |
| Longitude                           | -4.0118                                                                        |
| Latitude                            | 50.3882                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | Centrica                                                                       |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1050394.0                                                                      |
| Estimated Annual Generation in 2017 | 4199.25                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2009 |  131429.00 |
| CO2 Emissions (Tonnes) |   2010 | 1963818.00 |
| CO2 Emissions (Tonnes) |   2011 | 1866759.00 |
| CO2 Emissions (Tonnes) |   2012 | 1103998.00 |
| CO2 Emissions (Tonnes) |   2013 | 1192580.00 |
| CO2 Emissions (Tonnes) |   2014 | 1038702.00 |
| CO2 Emissions (Tonnes) |   2015 |  443926.00 |
| CO2 Emissions (Tonnes) |   2016 |  896488.00 |
| CO2 Emissions (Tonnes) |   2017 | 1238769.00 |
| CO2 Emissions (Tonnes) |   2018 |  968328.00 |
| CO2 Emissions (Tonnes) |   2019 |  744434.00 |
| CO2 Emissions (Tonnes) |   2020 |  799481.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |      Value |
|:--------------------|-------:|-----------:|
| Annual Output (MWh) |   2016 | 2367985.10 |
| Annual Output (MWh) |   2017 | 3326434.10 |
| Annual Output (MWh) |   2018 | 2416697.90 |
| Annual Output (MWh) |   2019 | 1936933.80 |
| Annual Output (MWh) |   2020 | 2073032.30 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   47.10 |
| Capture Price (£/MWh) |   2017 |   48.02 |
| Capture Price (£/MWh) |   2018 |   60.27 |
| Capture Price (£/MWh) |   2019 |   47.47 |
| Capture Price (£/MWh) |   2020 |   42.60 |

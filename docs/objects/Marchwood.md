### Identifiers

| Relationship   | ID Type              | ID(s)            |
|:---------------|:---------------------|:-----------------|
| Root           | OSUKED ID            | 10045            |
| Related        | Settlement BMU ID    | T_MRWD-1         |
| Related        | National Grid BMU ID | MRWD-1           |
| Equivalent     | GPPD ID              | GBR1000311       |
| Equivalent     | ESAIL ID             | MRWD             |
| Equivalent     | Common Name          | Marchwood        |
| Equivalent     | EUTL ID              | 97532            |
| Equivalent     | EIC ID               | 48W000000MRWD-1P |

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
| Longitude   |   -1.35 |
| Latitude    |   50.90 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 842.0                                                                          |
| Longitude                           | -1.4384                                                                        |
| Latitude                            | 50.8998                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | Marchwood Power Limited                                                        |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1052944.0                                                                      |
| Estimated Annual Generation in 2017 | 3906.92                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2009 |  761707.00 |
| CO2 Emissions (Tonnes) |   2010 | 2228297.00 |
| CO2 Emissions (Tonnes) |   2011 | 2159503.00 |
| CO2 Emissions (Tonnes) |   2012 | 1097847.00 |
| CO2 Emissions (Tonnes) |   2013 | 1255344.00 |
| CO2 Emissions (Tonnes) |   2014 | 1683941.00 |
| CO2 Emissions (Tonnes) |   2015 | 1328288.00 |
| CO2 Emissions (Tonnes) |   2016 | 1979491.00 |
| CO2 Emissions (Tonnes) |   2017 | 1964052.00 |
| CO2 Emissions (Tonnes) |   2018 | 1848833.00 |
| CO2 Emissions (Tonnes) |   2019 | 1560533.00 |
| CO2 Emissions (Tonnes) |   2020 | 1497168.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |      Value |
|:--------------------|-------:|-----------:|
| Annual Output (MWh) |   2016 | 5640833.30 |
| Annual Output (MWh) |   2017 | 5590636.80 |
| Annual Output (MWh) |   2018 | 5015982.10 |
| Annual Output (MWh) |   2019 | 4437811.70 |
| Annual Output (MWh) |   2020 | 4211782.60 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   41.03 |
| Capture Price (£/MWh) |   2017 |   46.79 |
| Capture Price (£/MWh) |   2018 |   57.95 |
| Capture Price (£/MWh) |   2019 |   45.33 |
| Capture Price (£/MWh) |   2020 |   37.70 |

### Identifiers

| Relationship   | ID Type              | ID(s)            |
|:---------------|:---------------------|:-----------------|
| Root           | OSUKED ID            | 10097            |
| Related        | Settlement BMU ID    | T_INDQ-1         |
| Related        | National Grid BMU ID | INDQ-1           |
| Equivalent     | GPPD ID              | GBR1000150       |
| Equivalent     | ESAIL ID             | INDQ             |
| Equivalent     | Common Name          | Indian Queens    |
| Equivalent     | EUTL ID              | 96869            |
| Equivalent     | EIC ID               | 48W000000INDQ-19 |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | OCGT    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -5.06 |
| Latitude    |   50.37 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 140.0                                                                          |
| Longitude                           | -4.8996                                                                        |
| Latitude                            | 50.3955                                                                        |
| Primary Fuel Type                   | Oil                                                                            |
| Owner                               | ENGIE                                                                          |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1013643.0                                                                      |
| Estimated Annual Generation in 2017 | 75.99                                                                          |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |    Value |
|:-----------------------|-------:|---------:|
| CO2 Emissions (Tonnes) |   2005 | 35449.00 |
| CO2 Emissions (Tonnes) |   2006 | 57291.00 |
| CO2 Emissions (Tonnes) |   2007 | 32686.00 |
| CO2 Emissions (Tonnes) |   2008 | 40833.00 |
| CO2 Emissions (Tonnes) |   2009 | 27791.00 |
| CO2 Emissions (Tonnes) |   2010 | 12252.00 |
| CO2 Emissions (Tonnes) |   2011 |  9668.00 |
| CO2 Emissions (Tonnes) |   2012 |  8863.00 |
| CO2 Emissions (Tonnes) |   2013 |  2125.00 |
| CO2 Emissions (Tonnes) |   2014 |  1265.00 |
| CO2 Emissions (Tonnes) |   2015 |  1369.00 |
| CO2 Emissions (Tonnes) |   2016 |   664.00 |
| CO2 Emissions (Tonnes) |   2017 |  1191.00 |
| CO2 Emissions (Tonnes) |   2018 |   531.00 |
| CO2 Emissions (Tonnes) |   2019 |  1885.00 |
| CO2 Emissions (Tonnes) |   2020 |   631.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   Value |
|:--------------------|-------:|--------:|
| Annual Output (MWh) |   2016 |  623.36 |
| Annual Output (MWh) |   2017 | 1170.44 |
| Annual Output (MWh) |   2018 |  502.30 |
| Annual Output (MWh) |   2019 | 1857.76 |
| Annual Output (MWh) |   2020 |  470.14 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   53.33 |
| Capture Price (£/MWh) |   2017 |   73.62 |
| Capture Price (£/MWh) |   2018 |   50.81 |
| Capture Price (£/MWh) |   2019 |   49.35 |
| Capture Price (£/MWh) |   2020 |   51.08 |

### Identifiers

| Relationship   | ID Type              | ID(s)                              |
|:---------------|:---------------------|:-----------------------------------|
| Root           | OSUKED ID            | 10044                              |
| Related        | Settlement BMU ID    | T_LBAR-1, T_LBAR-1G                |
| Related        | National Grid BMU ID | LBAR-1, LBAR-1G                    |
| Related        | EIC ID               | 48W000000LBAR-1Y, 48W00000LBAR-1G7 |
| Equivalent     | GPPD ID              | GBR1000371                         |
| Equivalent     | ESAIL ID             | LBAR                               |
| Equivalent     | Common Name          | Little Barford                     |
| Equivalent     | EUTL ID              | 97169                              |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | LBAR-1   | LBAR-1G   |
|:------------|:---------|:----------|
| Fuel Type   | CCGT     | OCGT      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.23 |
| Latitude    |   52.22 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 720.0                                                                          |
| Longitude                           | -0.2693                                                                        |
| Latitude                            | 52.2046                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | RWE Npower Plc                                                                 |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1023602.0                                                                      |
| Estimated Annual Generation in 2017 | 3340.84                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 1426809.00 |
| CO2 Emissions (Tonnes) |   2006 | 1106935.00 |
| CO2 Emissions (Tonnes) |   2007 | 1650201.00 |
| CO2 Emissions (Tonnes) |   2008 | 1534371.00 |
| CO2 Emissions (Tonnes) |   2009 | 1345795.00 |
| CO2 Emissions (Tonnes) |   2010 | 1749272.00 |
| CO2 Emissions (Tonnes) |   2011 |  701415.00 |
| CO2 Emissions (Tonnes) |   2012 |  108609.00 |
| CO2 Emissions (Tonnes) |   2013 |  687333.00 |
| CO2 Emissions (Tonnes) |   2014 | 1116502.00 |
| CO2 Emissions (Tonnes) |   2015 | 1073794.00 |
| CO2 Emissions (Tonnes) |   2016 | 1314656.00 |
| CO2 Emissions (Tonnes) |   2017 | 1484225.00 |
| CO2 Emissions (Tonnes) |   2018 | 1686546.00 |
| CO2 Emissions (Tonnes) |   2019 | 1079406.00 |
| CO2 Emissions (Tonnes) |   2020 |  824525.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     LBAR-1 |   LBAR-1G |
|:--------------------|-------:|-----------:|----------:|
| Annual Output (MWh) |   2016 | 3504736.73 |    137.17 |
| Annual Output (MWh) |   2017 | 3937267.69 |    120.06 |
| Annual Output (MWh) |   2018 | 4278575.07 |    180.52 |
| Annual Output (MWh) |   2019 | 2770502.33 |    189.58 |
| Annual Output (MWh) |   2020 | 2135193.93 |    185.29 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   LBAR-1 |   LBAR-1G |
|:----------------------|-------:|---------:|----------:|
| Capture Price (£/MWh) |   2016 |    43.63 |     33.89 |
| Capture Price (£/MWh) |   2017 |    47.49 |     53.14 |
| Capture Price (£/MWh) |   2018 |    57.19 |     99.02 |
| Capture Price (£/MWh) |   2019 |    47.13 |     42.28 |
| Capture Price (£/MWh) |   2020 |    41.17 |     50.41 |

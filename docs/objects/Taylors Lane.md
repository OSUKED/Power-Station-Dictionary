### Identifiers

| Relationship   | ID Type              | ID(s)                              |
|:---------------|:---------------------|:-----------------------------------|
| Root           | OSUKED ID            | 10104                              |
| Related        | Settlement BMU ID    | E_TAYL2G, E_TAYL3G                 |
| Related        | National Grid BMU ID | TAYL2G, TAYL3G                     |
| Related        | EIC ID               | 48W000000TAYL2GY, 48W000000TAYL3GV |
| Equivalent     | GPPD ID              | GBR1000499                         |
| Equivalent     | ESAIL ID             | TAYLG                              |
| Equivalent     | Common Name          | Taylors Lane                       |
| Equivalent     | EUTL ID              | 97048                              |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | TAYL2G   | TAYL3G   |
|:------------|:---------|:---------|
| Fuel Type   | OCGT     | OCGT     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.26 |
| Latitude    |   51.55 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 144.0                                                                          |
| Longitude                           | -0.2575                                                                        |
| Latitude                            | 51.5459                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | Uniper UK Limited                                                              |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| Estimated Annual Generation in 2017 | 668.16                                                                         |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |   Value |
|:-----------------------|-------:|--------:|
| CO2 Emissions (Tonnes) |   2005 | 5711.00 |
| CO2 Emissions (Tonnes) |   2006 | 9967.00 |
| CO2 Emissions (Tonnes) |   2007 | 6395.00 |
| CO2 Emissions (Tonnes) |   2008 | 3636.00 |
| CO2 Emissions (Tonnes) |   2009 | 4868.00 |
| CO2 Emissions (Tonnes) |   2010 | 3360.00 |
| CO2 Emissions (Tonnes) |   2011 |  962.00 |
| CO2 Emissions (Tonnes) |   2012 | 2578.00 |
| CO2 Emissions (Tonnes) |   2013 | 1245.00 |
| CO2 Emissions (Tonnes) |   2014 |  345.00 |
| CO2 Emissions (Tonnes) |   2015 | 1323.00 |
| CO2 Emissions (Tonnes) |   2016 | 7114.00 |
| CO2 Emissions (Tonnes) |   2017 | 8778.00 |
| CO2 Emissions (Tonnes) |   2018 | 8209.00 |
| CO2 Emissions (Tonnes) |   2019 |  927.00 |
| CO2 Emissions (Tonnes) |   2020 | 2398.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   TAYL2G |   TAYL3G |
|:--------------------|-------:|---------:|---------:|
| Annual Output (MWh) |   2016 |  3572.79 |  2869.73 |
| Annual Output (MWh) |   2017 |  4374.30 |  3527.71 |
| Annual Output (MWh) |   2018 |  4048.02 |  3393.58 |
| Annual Output (MWh) |   2019 |   529.07 |   294.57 |
| Annual Output (MWh) |   2020 |   845.55 |  1395.56 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   TAYL2G |   TAYL3G |
|:----------------------|-------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |   144.32 |   144.44 |
| Capture Price (£/MWh) |   2017 |    77.86 |    91.28 |
| Capture Price (£/MWh) |   2018 |   100.40 |    93.47 |
| Capture Price (£/MWh) |   2019 |    43.56 |    45.52 |
| Capture Price (£/MWh) |   2020 |   121.56 |   151.33 |

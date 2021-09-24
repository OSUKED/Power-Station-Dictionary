### Identifiers

| Relationship   | ID Type              | ID(s)                                                |
|:---------------|:---------------------|:-----------------------------------------------------|
| Root           | OSUKED ID            | 10040                                                |
| Related        | Settlement BMU ID    | T_KILNS-1, T_KILLPG-1, T_KILLPG-2                    |
| Related        | National Grid BMU ID | KILNS-1, KILLPG-1, KILLPG-2                          |
| Related        | EUTL ID              | 97057, 97443                                         |
| Related        | EIC ID               | 48W00000KILNS-1P, 48W0000KILLPG-1Q, 48W0000KILLPG-2O |
| Equivalent     | GPPD ID              | GBR1000500                                           |
| Equivalent     | ESAIL ID             | KIL                                                  |
| Equivalent     | Common Name          | Killingholme                                         |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | KILLPG-1   | KILLPG-2   | KILNS-1   |
|:------------|:-----------|:-----------|:----------|
| Fuel Type   | CCGT       | CCGT       | CCGT      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.26 |
| Latitude    |   53.66 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 600.0                                                                          |
| Longitude                           | -0.2556                                                                        |
| Latitude                            | 53.6535                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | Uniper UK Limited                                                              |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| Estimated Annual Generation in 2017 | 2784.03                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      97057 |      97443 |
|:-----------------------|-------:|-----------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 |  533528.00 | 1295903.00 |
| CO2 Emissions (Tonnes) |   2006 |  701199.00 |  556119.00 |
| CO2 Emissions (Tonnes) |   2007 | 1795380.00 |  770197.00 |
| CO2 Emissions (Tonnes) |   2008 | 2135992.00 | 1806442.00 |
| CO2 Emissions (Tonnes) |   2009 | 2186108.00 | 1274629.00 |
| CO2 Emissions (Tonnes) |   2010 | 1157296.00 |  404978.00 |
| CO2 Emissions (Tonnes) |   2011 |  253267.00 |  206528.00 |
| CO2 Emissions (Tonnes) |   2012 |  134510.00 |  276381.00 |
| CO2 Emissions (Tonnes) |   2013 |  108011.00 |  212818.00 |
| CO2 Emissions (Tonnes) |   2014 |  138695.00 |  269079.00 |
| CO2 Emissions (Tonnes) |   2015 |   26439.00 |   74661.00 |
| CO2 Emissions (Tonnes) |   2016 |    2742.00 |    1616.00 |
| CO2 Emissions (Tonnes) |   2017 |    7170.00 |     nan    |
| CO2 Emissions (Tonnes) |   2018 |   25051.00 |     nan    |
| CO2 Emissions (Tonnes) |   2019 |   44237.00 |     nan    |
| CO2 Emissions (Tonnes) |   2020 |   33542.00 |     nan    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   KILLPG-1 |   KILLPG-2 |   KILNS-1 |
|:--------------------|-------:|-----------:|-----------:|----------:|
| Annual Output (MWh) |   2016 |    1812.53 |    1977.15 |   2926.38 |
| Annual Output (MWh) |   2017 |    4670.68 |    5817.98 |      0.00 |
| Annual Output (MWh) |   2018 |   23090.19 |   14468.36 |      0.00 |
| Annual Output (MWh) |   2019 |   25677.64 |   41201.60 |      1.00 |
| Annual Output (MWh) |   2020 |   32400.30 |   19279.58 |      0.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   KILLPG-1 |   KILLPG-2 |   KILNS-1 |
|:----------------------|-------:|-----------:|-----------:|----------:|
| Capture Price (£/MWh) |   2016 |      44.08 |      45.11 |     25.39 |
| Capture Price (£/MWh) |   2017 |      65.60 |      65.44 |    nan    |
| Capture Price (£/MWh) |   2018 |     110.65 |     112.03 |    nan    |
| Capture Price (£/MWh) |   2019 |      65.84 |      54.55 |     31.63 |
| Capture Price (£/MWh) |   2020 |      84.37 |      99.07 |    nan    |

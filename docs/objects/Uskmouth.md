### Identifiers

| Relationship   | ID Type              | ID(s)                                                |
|:---------------|:---------------------|:-----------------------------------------------------|
| Root           | OSUKED ID            | 10013                                                |
| Related        | Settlement BMU ID    | T_USKM-13, T_USKM-14, T_USKM-15                      |
| Related        | National Grid BMU ID | USKM-13, USKM-14, USKM-15                            |
| Related        | EIC ID               | 48W00000USKM-13T, 48W00000USKM-14R, 48W00000USKM-15P |
| Equivalent     | GPPD ID              | GBR2000811                                           |
| Equivalent     | ESAIL ID             | USKM                                                 |
| Equivalent     | Common Name          | Uskmouth                                             |
| Equivalent     | EUTL ID              | 97413                                                |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | USKM-13   | USKM-14   | USKM-15   |
|:------------|:----------|:----------|:----------|
| Fuel Type   | BIOMASS   | BIOMASS   | BIOMASS   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.04 |
| Latitude    |   51.61 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value   |
|:------------------------------------|:--------|
| Installed Capacity (MW)             | 230.0   |
| Longitude                           | -2.9705 |
| Latitude                            | 51.5491 |
| Primary Fuel Type                   | Coal    |
| Geolocation Source                  | GEO     |
| Estimated Annual Generation in 2017 | 349.36  |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 |  993930.00 |
| CO2 Emissions (Tonnes) |   2006 |  866926.00 |
| CO2 Emissions (Tonnes) |   2007 |  650452.00 |
| CO2 Emissions (Tonnes) |   2008 | 1261290.00 |
| CO2 Emissions (Tonnes) |   2009 |  730966.00 |
| CO2 Emissions (Tonnes) |   2010 |  364196.00 |
| CO2 Emissions (Tonnes) |   2011 |  432476.00 |
| CO2 Emissions (Tonnes) |   2012 | 1102448.00 |
| CO2 Emissions (Tonnes) |   2013 | 1321477.00 |
| CO2 Emissions (Tonnes) |   2014 |  303643.00 |
| CO2 Emissions (Tonnes) |   2015 |  260169.00 |
| CO2 Emissions (Tonnes) |   2016 |  462434.00 |
| CO2 Emissions (Tonnes) |   2017 |   75503.00 |
| CO2 Emissions (Tonnes) |   2018 |    2448.00 |
| CO2 Emissions (Tonnes) |   2019 |     486.00 |
| CO2 Emissions (Tonnes) |   2020 |       4.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   USKM-13 |   USKM-14 |   USKM-15 |
|:--------------------|-------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 | 227497.20 | 179529.20 |      0.00 |
| Annual Output (MWh) |   2017 |  38307.80 |  25212.10 |      0.40 |
| Annual Output (MWh) |   2018 |      0.20 |      0.00 |      0.20 |
| Annual Output (MWh) |   2019 |      0.00 |      0.00 |    254.21 |
| Annual Output (MWh) |   2020 |      0.00 |      0.00 |      0.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   USKM-13 |   USKM-14 |   USKM-15 |
|:----------------------|-------:|----------:|----------:|----------:|
| Capture Price (£/MWh) |   2016 |     50.22 |     51.28 |    nan    |
| Capture Price (£/MWh) |   2017 |     59.23 |     60.66 |     45.39 |
| Capture Price (£/MWh) |   2018 |     45.16 |    nan    |     55.27 |
| Capture Price (£/MWh) |   2019 |    nan    |    nan    |     42.44 |

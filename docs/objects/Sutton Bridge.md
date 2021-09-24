### Identifiers

| Relationship   | ID Type              | ID(s)            |
|:---------------|:---------------------|:-----------------|
| Root           | OSUKED ID            | 10059            |
| Related        | Settlement BMU ID    | T_SUTB-1         |
| Related        | National Grid BMU ID | SUTB-1           |
| Equivalent     | GPPD ID              | GBR2000518       |
| Equivalent     | ESAIL ID             | SUTB             |
| Equivalent     | Common Name          | Sutton Bridge    |
| Equivalent     | EUTL ID              | 97236            |
| Equivalent     | EIC ID               | 48W000000SUTB-1P |

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
| Longitude   |    0.10 |
| Latitude    |   52.62 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value   |
|:------------------------------------|:--------|
| Installed Capacity (MW)             | 819.0   |
| Longitude                           | 0.1923  |
| Latitude                            | 52.7579 |
| Primary Fuel Type                   | Gas     |
| Geolocation Source                  | GEO     |
| Estimated Annual Generation in 2017 | 3800.2  |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 1871252.00 |
| CO2 Emissions (Tonnes) |   2006 | 1982395.00 |
| CO2 Emissions (Tonnes) |   2007 | 1960831.00 |
| CO2 Emissions (Tonnes) |   2008 | 2116571.00 |
| CO2 Emissions (Tonnes) |   2009 | 2047459.00 |
| CO2 Emissions (Tonnes) |   2010 | 1030167.00 |
| CO2 Emissions (Tonnes) |   2011 | 1962411.00 |
| CO2 Emissions (Tonnes) |   2012 |  562845.00 |
| CO2 Emissions (Tonnes) |   2013 |  470283.00 |
| CO2 Emissions (Tonnes) |   2014 |  430892.00 |
| CO2 Emissions (Tonnes) |   2015 |  245929.00 |
| CO2 Emissions (Tonnes) |   2016 |  836501.00 |
| CO2 Emissions (Tonnes) |   2017 |  945226.00 |
| CO2 Emissions (Tonnes) |   2018 |  667540.00 |
| CO2 Emissions (Tonnes) |   2019 |  776555.00 |
| CO2 Emissions (Tonnes) |   2020 |  259128.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |      Value |
|:--------------------|-------:|-----------:|
| Annual Output (MWh) |   2016 | 2198114.90 |
| Annual Output (MWh) |   2017 | 2511718.90 |
| Annual Output (MWh) |   2018 | 1623232.90 |
| Annual Output (MWh) |   2019 | 1980431.30 |
| Annual Output (MWh) |   2020 |  659072.40 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   43.15 |
| Capture Price (£/MWh) |   2017 |   50.48 |
| Capture Price (£/MWh) |   2018 |   56.48 |
| Capture Price (£/MWh) |   2019 |   45.94 |
| Capture Price (£/MWh) |   2020 |   34.12 |

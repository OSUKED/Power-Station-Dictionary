### Identifiers

| Relationship   | ID Type              | ID(s)            |
|:---------------|:---------------------|:-----------------|
| Root           | OSUKED ID            | 10034            |
| Related        | Settlement BMU ID    | T_DEEP-1         |
| Related        | National Grid BMU ID | DEEP-1           |
| Equivalent     | GPPD ID              | GBR2000262       |
| Equivalent     | ESAIL ID             | DEEP             |
| Equivalent     | Common Name          | Deeside          |
| Equivalent     | EUTL ID              | 97636            |
| Equivalent     | EIC ID               | 48W000000DEEP-1N |

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
| Longitude   |   -3.21 |
| Latitude    |   53.14 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value   |
|:------------------------------------|:--------|
| Installed Capacity (MW)             | 515.0   |
| Longitude                           | -3.0547 |
| Latitude                            | 53.2332 |
| Primary Fuel Type                   | Gas     |
| Geolocation Source                  | GEO     |
| Estimated Annual Generation in 2017 | 2389.62 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 |  978825.00 |
| CO2 Emissions (Tonnes) |   2006 |  640379.00 |
| CO2 Emissions (Tonnes) |   2007 |  882916.00 |
| CO2 Emissions (Tonnes) |   2008 | 1239522.00 |
| CO2 Emissions (Tonnes) |   2009 | 1158095.00 |
| CO2 Emissions (Tonnes) |   2010 | 1170704.00 |
| CO2 Emissions (Tonnes) |   2011 |  670401.00 |
| CO2 Emissions (Tonnes) |   2012 |  314779.00 |
| CO2 Emissions (Tonnes) |   2013 |  367723.00 |
| CO2 Emissions (Tonnes) |   2014 |  291518.00 |
| CO2 Emissions (Tonnes) |   2015 |  141965.00 |
| CO2 Emissions (Tonnes) |   2016 |  248853.00 |
| CO2 Emissions (Tonnes) |   2017 |  289810.00 |
| CO2 Emissions (Tonnes) |   2018 |  145298.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     Value |
|:--------------------|-------:|----------:|
| Annual Output (MWh) |   2016 | 600735.44 |
| Annual Output (MWh) |   2017 | 698242.08 |
| Annual Output (MWh) |   2018 | 352730.22 |
| Annual Output (MWh) |   2019 |      0.00 |
| Annual Output (MWh) |   2020 |      0.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   51.65 |
| Capture Price (£/MWh) |   2017 |   56.08 |
| Capture Price (£/MWh) |   2018 |   60.85 |

### Identifiers

| Relationship   | ID Type              | ID(s)            |
|:---------------|:---------------------|:-----------------|
| Root           | OSUKED ID            | 10026            |
| Related        | Settlement BMU ID    | E_BRGG-1         |
| Related        | National Grid BMU ID | BRGG-1           |
| Equivalent     | GPPD ID              | GBR2000126       |
| Equivalent     | ESAIL ID             | BRGG             |
| Equivalent     | Common Name          | Brigg            |
| Equivalent     | EUTL ID              | 97215            |
| Equivalent     | EIC ID               | 48W000000BRGG-1M |

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
| Longitude   |   -0.33 |
| Latitude    |   53.44 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value   |
|:------------------------------------|:--------|
| Installed Capacity (MW)             | 150.0   |
| Longitude                           | -0.5055 |
| Latitude                            | 53.5411 |
| Primary Fuel Type                   | Gas     |
| Geolocation Source                  | GEO     |
| Estimated Annual Generation in 2017 | 696.0   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |     Value |
|:-----------------------|-------:|----------:|
| CO2 Emissions (Tonnes) |   2005 | 279723.00 |
| CO2 Emissions (Tonnes) |   2006 | 193579.00 |
| CO2 Emissions (Tonnes) |   2007 | 319150.00 |
| CO2 Emissions (Tonnes) |   2008 | 413717.00 |
| CO2 Emissions (Tonnes) |   2009 | 466474.00 |
| CO2 Emissions (Tonnes) |   2010 | 161063.00 |
| CO2 Emissions (Tonnes) |   2011 |   7570.00 |
| CO2 Emissions (Tonnes) |   2012 |  12336.00 |
| CO2 Emissions (Tonnes) |   2013 |  10146.00 |
| CO2 Emissions (Tonnes) |   2014 |   9642.00 |
| CO2 Emissions (Tonnes) |   2015 |   7548.00 |
| CO2 Emissions (Tonnes) |   2016 |  14220.00 |
| CO2 Emissions (Tonnes) |   2017 |  14407.00 |
| CO2 Emissions (Tonnes) |   2018 |  17180.00 |
| CO2 Emissions (Tonnes) |   2019 |  20490.00 |
| CO2 Emissions (Tonnes) |   2020 |  26406.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    Value |
|:--------------------|-------:|---------:|
| Annual Output (MWh) |   2016 | 20917.36 |
| Annual Output (MWh) |   2017 | 20066.48 |
| Annual Output (MWh) |   2018 |  9773.99 |
| Annual Output (MWh) |   2019 |  6727.07 |
| Annual Output (MWh) |   2020 |  3109.12 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   94.38 |
| Capture Price (£/MWh) |   2017 |   78.49 |
| Capture Price (£/MWh) |   2018 |   80.55 |
| Capture Price (£/MWh) |   2019 |   72.85 |
| Capture Price (£/MWh) |   2020 |   88.17 |

### Identifiers

| Relationship   | ID Type              | ID(s)                                                |
|:---------------|:---------------------|:-----------------------------------------------------|
| Root           | OSUKED ID            | 10052                                                |
| Related        | Settlement BMU ID    | T_SCCL-1, T_SCCL-2, T_SCCL-3                         |
| Related        | National Grid BMU ID | SCCL-1, SCCL-2, SCCL-3                               |
| Related        | EIC ID               | 48W000000SCCL-1U, 48W000000SCCL-2S, 48W000000SCCL-3Q |
| Equivalent     | GPPD ID              | GBR2000263                                           |
| Equivalent     | ESAIL ID             | SCCL                                                 |
| Equivalent     | Common Name          | Saltend South                                        |
| Equivalent     | EUTL ID              | 96903                                                |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | SCCL-1   | SCCL-2   | SCCL-3   |
|:------------|:---------|:---------|:---------|
| Fuel Type   | CCGT     | CCGT     | CCGT     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.13 |
| Latitude    |   53.83 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value        |
|:------------------------------------|:-------------|
| Installed Capacity (MW)             | 1200.0       |
| Longitude                           | -0.2432      |
| Latitude                            | 53.735       |
| Primary Fuel Type                   | Gas          |
| Secondary Fuel Type                 | Cogeneration |
| Geolocation Source                  | WRI          |
| Estimated Annual Generation in 2017 | 5568.06      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 3553376.00 |
| CO2 Emissions (Tonnes) |   2006 | 3109891.00 |
| CO2 Emissions (Tonnes) |   2007 | 3610228.00 |
| CO2 Emissions (Tonnes) |   2008 | 3577320.00 |
| CO2 Emissions (Tonnes) |   2009 | 3417820.00 |
| CO2 Emissions (Tonnes) |   2010 | 3422020.00 |
| CO2 Emissions (Tonnes) |   2011 | 3459221.00 |
| CO2 Emissions (Tonnes) |   2012 | 3298487.00 |
| CO2 Emissions (Tonnes) |   2013 | 2879178.00 |
| CO2 Emissions (Tonnes) |   2014 | 2820501.00 |
| CO2 Emissions (Tonnes) |   2015 | 2239237.00 |
| CO2 Emissions (Tonnes) |   2016 | 2982161.00 |
| CO2 Emissions (Tonnes) |   2017 | 2811044.00 |
| CO2 Emissions (Tonnes) |   2018 | 2733240.00 |
| CO2 Emissions (Tonnes) |   2019 | 2772619.00 |
| CO2 Emissions (Tonnes) |   2020 | 2679112.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     SCCL-1 |     SCCL-2 |     SCCL-3 |
|:--------------------|-------:|-----------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 2549642.20 | 2426374.55 | 2473524.70 |
| Annual Output (MWh) |   2017 | 2667192.10 | 2191379.10 | 2176856.65 |
| Annual Output (MWh) |   2018 | 2093050.10 | 2219639.25 | 2269712.15 |
| Annual Output (MWh) |   2019 | 2463509.15 | 2127121.50 | 2462617.15 |
| Annual Output (MWh) |   2020 | 2071468.95 | 2577687.65 | 2142373.55 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   SCCL-1 |   SCCL-2 |   SCCL-3 |
|:----------------------|-------:|---------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    40.37 |    41.34 |    40.75 |
| Capture Price (£/MWh) |   2017 |    45.75 |    46.71 |    46.51 |
| Capture Price (£/MWh) |   2018 |    59.23 |    57.94 |    57.52 |
| Capture Price (£/MWh) |   2019 |    44.03 |    45.55 |    42.46 |
| Capture Price (£/MWh) |   2020 |    38.33 |    37.28 |    36.59 |

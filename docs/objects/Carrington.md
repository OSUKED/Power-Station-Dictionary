### Identifiers

| Relationship   | ID Type              | ID(s)                              |
|:---------------|:---------------------|:-----------------------------------|
| Root           | OSUKED ID            | 10027                              |
| Related        | Settlement BMU ID    | T_CARR-1, T_CARR-2                 |
| Related        | National Grid BMU ID | CARR-1, CARR-2                     |
| Related        | EIC ID               | 48W000000CARR-1I, 48W000000CARR-2G |
| Equivalent     | GPPD ID              | GBR2000124                         |
| Equivalent     | ESAIL ID             | CARR                               |
| Equivalent     | Common Name          | Carrington                         |
| Equivalent     | EUTL ID              | 112433                             |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | CARR-1   | CARR-2   |
|:------------|:---------|:---------|
| Fuel Type   | CCGT     | CCGT     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -2.50 |
| Latitude    |   53.46 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value   |
|:------------------------------------|:--------|
| Installed Capacity (MW)             | 900.0   |
| Longitude                           | -2.4077 |
| Latitude                            | 53.4366 |
| Primary Fuel Type                   | Gas     |
| Geolocation Source                  | WRI     |
| Estimated Annual Generation in 2017 | 4176.05 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2016 |  999505.00 |
| CO2 Emissions (Tonnes) |   2017 | 1706607.00 |
| CO2 Emissions (Tonnes) |   2018 | 1730337.00 |
| CO2 Emissions (Tonnes) |   2019 | 1488961.00 |
| CO2 Emissions (Tonnes) |   2020 |  879896.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     CARR-1 |     CARR-2 |
|:--------------------|-------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 1324700.50 | 1371785.00 |
| Annual Output (MWh) |   2017 | 2336355.90 | 2336500.70 |
| Annual Output (MWh) |   2018 | 2324901.60 | 2199250.50 |
| Annual Output (MWh) |   2019 | 1939525.00 | 2135729.80 |
| Annual Output (MWh) |   2020 | 1292381.80 | 1079629.40 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   CARR-1 |   CARR-2 |
|:----------------------|-------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    46.82 |    46.34 |
| Capture Price (£/MWh) |   2017 |    47.50 |    47.92 |
| Capture Price (£/MWh) |   2018 |    58.70 |    58.38 |
| Capture Price (£/MWh) |   2019 |    45.10 |    45.67 |
| Capture Price (£/MWh) |   2020 |    40.64 |    40.94 |

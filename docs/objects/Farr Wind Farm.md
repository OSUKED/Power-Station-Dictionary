### Identifiers

| Relationship   | ID Type              | ID(s)                              |
|:---------------|:---------------------|:-----------------------------------|
| Root           | OSUKED ID            | 10191                              |
| Related        | Settlement BMU ID    | T_FARR-1, T_FARR-2                 |
| Related        | National Grid BMU ID | FAARW-1, FAARW-2                   |
| Related        | EIC ID               | 48W00000FAARW-13, 48W00000FAARW-21 |
| Equivalent     | GPPD ID              | GBR0004676                         |
| Equivalent     | ESAIL ID             | FARR                               |
| Equivalent     | Common Name          | Farr Wind Farm                     |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | FAARW-1   | FAARW-2   |
|:------------|:----------|:----------|
| Fuel Type   | WIND      | WIND      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -4.09 |
| Latitude    |   57.33 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Plant Type  | onshore |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                    |
|:------------------------------------|:-------------------------------------------------------------------------|
| Installed Capacity (MW)             | 92.0                                                                     |
| Longitude                           | -4.103                                                                   |
| Latitude                            | 57.3339                                                                  |
| Primary Fuel Type                   | Wind                                                                     |
| Owner                               | Innogy (formerly RWE npower)                                             |
| Source                              | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    |
| PLATTS-WEPP ID                      | 1061620.0                                                                |
| Estimated Annual Generation in 2017 | 231.92                                                                   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   FAARW-1 |   FAARW-2 |
|:--------------------|-------:|----------:|----------:|
| Annual Output (MWh) |   2016 | 100606.48 |  94595.29 |
| Annual Output (MWh) |   2017 | 106058.36 | 104820.45 |
| Annual Output (MWh) |   2018 |  91780.99 | 105059.10 |
| Annual Output (MWh) |   2019 |  93931.56 |  90371.21 |
| Annual Output (MWh) |   2020 |  71577.35 |  82201.85 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   FAARW-1 |   FAARW-2 |
|:----------------------|-------:|----------:|----------:|
| Capture Price (£/MWh) |   2016 |     38.72 |     37.69 |
| Capture Price (£/MWh) |   2017 |     44.93 |     44.83 |
| Capture Price (£/MWh) |   2018 |     57.71 |     58.09 |
| Capture Price (£/MWh) |   2019 |     40.68 |     41.26 |
| Capture Price (£/MWh) |   2020 |     33.91 |     35.30 |

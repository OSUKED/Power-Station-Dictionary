### Identifiers

| Relationship   | ID Type              | ID(s)            |
|:---------------|:---------------------|:-----------------|
| Root           | OSUKED ID            | 10119            |
| Related        | Settlement BMU ID    | T_GLNDO-1        |
| Related        | National Grid BMU ID | GLNDO-1          |
| Equivalent     | GPPD ID              | GBR0000388       |
| Equivalent     | ESAIL ID             | GLNDO            |
| Equivalent     | Common Name          | Glendoe          |
| Equivalent     | EIC ID               | 48W00000GLNDO-1G |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | NPSHYD  |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -5.17 |
| Latitude    |   57.15 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                    |
|:------------------------------------|:-------------------------------------------------------------------------|
| Installed Capacity (MW)             | 100.0                                                                    |
| Longitude                           | -4.6592                                                                  |
| Latitude                            | 57.1437                                                                  |
| Primary Fuel Type                   | Hydro                                                                    |
| Owner                               | Scottish and Southern Energy (SSE)                                       |
| Source                              | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    |
| PLATTS-WEPP ID                      | 1059333.0                                                                |
| Estimated Annual Generation in 2013 | 303.9                                                                    |
| Estimated Annual Generation in 2014 | 237.62                                                                   |
| Estimated Annual Generation in 2015 | 435.46                                                                   |
| Estimated Annual Generation in 2016 | 278.62                                                                   |
| Estimated Annual Generation in 2017 | 277.86                                                                   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     Value |
|:--------------------|-------:|----------:|
| Annual Output (MWh) |   2016 | 141758.23 |
| Annual Output (MWh) |   2017 | 139016.47 |
| Annual Output (MWh) |   2018 | 149858.21 |
| Annual Output (MWh) |   2019 | 177515.84 |
| Annual Output (MWh) |   2020 | 231742.12 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   51.29 |
| Capture Price (£/MWh) |   2017 |   54.07 |
| Capture Price (£/MWh) |   2018 |   63.76 |
| Capture Price (£/MWh) |   2019 |   47.57 |
| Capture Price (£/MWh) |   2020 |   40.99 |
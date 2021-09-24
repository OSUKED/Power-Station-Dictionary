### Identifiers

| Relationship   | ID Type              | ID(s)            |
|:---------------|:---------------------|:-----------------|
| Root           | OSUKED ID            | 10109            |
| Related        | Settlement BMU ID    | M_CAS-CLU01      |
| Related        | National Grid BMU ID | CAS-CLU01        |
| Equivalent     | GPPD ID              | GBR1000405       |
| Equivalent     | ESAIL ID             | CASCLU           |
| Equivalent     | Common Name          | Clunie Cascade   |
| Equivalent     | EIC ID               | 48W000CAS-CLU01B |

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
| Longitude   |   -3.78 |
| Latitude    |   56.72 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 61.2                                                                           |
| Longitude                           | -2.6167                                                                        |
| Latitude                            | 57.55                                                                          |
| Primary Fuel Type                   | Hydro                                                                          |
| Owner                               | Scottish and Southern: Hydro Schemes - Tummel                                  |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | CARMA                                                                          |
| PLATTS-WEPP ID                      | 1028294.0                                                                      |
| Estimated Annual Generation in 2013 | 221.29                                                                         |
| Estimated Annual Generation in 2014 | 119.75                                                                         |
| Estimated Annual Generation in 2015 | 281.41                                                                         |
| Estimated Annual Generation in 2016 | 202.13                                                                         |
| Estimated Annual Generation in 2017 | 204.26                                                                         |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     Value |
|:--------------------|-------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |
| Annual Output (MWh) |   2017 |      0.00 |
| Annual Output (MWh) |   2018 |      0.00 |
| Annual Output (MWh) |   2019 | 234777.47 |
| Annual Output (MWh) |   2020 | 305671.35 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2019 |   41.23 |
| Capture Price (£/MWh) |   2020 |   36.05 |

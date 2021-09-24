### Identifiers

| Relationship   | ID Type              | ID(s)                                                      |
|:---------------|:---------------------|:-----------------------------------------------------------|
| Root           | OSUKED ID            | 10128                                                      |
| Related        | Settlement BMU ID    | T_DUNG-1, T_DUNG-2, T_DUNG-3, T_DUNG-4, T_DNGB21, T_DNGB22 |
| Related        | National Grid BMU ID | DNGB21, DNGB22                                             |
| Related        | EIC ID               | 48W000000DNGB216, 48W000000DNGB224                         |
| Equivalent     | GPPD ID              | GBR1000052                                                 |
| Equivalent     | ESAIL ID             | DUNG                                                       |
| Equivalent     | Common Name          | Dungeness B                                                |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | DNGB21   | DNGB22   |
|:------------|:---------|:---------|
| Fuel Type   | NUCLEAR  | NUCLEAR  |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    0.96 |
| Latitude    |   50.91 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 1050.0                                                                         |
| Longitude                           | 0.964                                                                          |
| Latitude                            | 50.9133                                                                        |
| Primary Fuel Type                   | Nuclear                                                                        |
| Owner                               | British Energy (now part of EDF)                                               |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1043125.0                                                                      |
| Estimated Annual Generation in 2017 | 6938.44                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     DNGB21 |     DNGB22 |
|:--------------------|-------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 4028569.62 | 3816796.17 |
| Annual Output (MWh) |   2017 | 2452885.25 | 3446814.02 |
| Annual Output (MWh) |   2018 | 2791474.56 | 2717332.65 |
| Annual Output (MWh) |   2019 |       0.00 |       0.00 |
| Annual Output (MWh) |   2020 |       0.00 |       0.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   DNGB21 |   DNGB22 |
|:----------------------|-------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    39.19 |    39.22 |
| Capture Price (£/MWh) |   2017 |    46.25 |    43.53 |
| Capture Price (£/MWh) |   2018 |    55.56 |    54.11 |

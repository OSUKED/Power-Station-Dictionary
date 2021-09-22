### Identifiers

| Relationship   | ID Type     | ID(s)                |
|:---------------|:------------|:---------------------|
| root           | osuked_id   | 10134                |
| element-of     | sett_bmu_id | T_HUNB-7, T_HUNB-8   |
| element-of     | ngc_bmu_id  | HUNB-7, HUNB-8       |
| same-as        | gppd_idnr   | GBR1000057           |
| same-as        | esail_id    | HUNB                 |
| same-as        | name        | Hunterston Generator |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -4.82 |
| Latitude    |   55.65 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 965.0                                                                          |
| Longitude                           | -4.8964                                                                        |
| Latitude                            | 55.7204                                                                        |
| Primary Fuel Type                   | Nuclear                                                                        |
| Owner                               | British Energy (now part of EDF)                                               |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1028357.0                                                                      |
| Estimated Annual Generation in 2017 | 6376.76                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     HUNB-7 |     HUNB-8 |
|:--------------------|-------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 3980995.38 | 4147373.73 |
| Annual Output (MWh) |   2017 | 3989068.99 | 3557532.81 |
| Annual Output (MWh) |   2018 |  711990.37 | 3092730.10 |
| Annual Output (MWh) |   2019 |       0.00 | 1239831.88 |
| Annual Output (MWh) |   2020 | 1386029.00 | 1119441.14 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | HUNB-7   | HUNB-8   |
|:------------|:---------|:---------|
| Fuel Type   | NUCLEAR  | NUCLEAR  |

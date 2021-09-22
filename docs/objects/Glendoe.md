### Identifiers

| Relationship   | ID Type     | ID(s)      |
|:---------------|:------------|:-----------|
| root           | osuked_id   | 10119      |
| element-of     | sett_bmu_id | T_GLNDO-1  |
| element-of     | ngc_bmu_id  | GLNDO-1    |
| same-as        | gppd_idnr   | GBR0000388 |
| same-as        | esail_id    | GLNDO      |
| same-as        | name        | Glendoe    |

<br>
### Datasets
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
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | NPSHYD  |

### Identifiers

| Relationship   | ID Type     | ID(s)              |
|:---------------|:------------|:-------------------|
| root           | osuked_id   | 10138              |
| element-of     | sett_bmu_id | T_TORN-1, T_TORN-2 |
| element-of     | ngc_bmu_id  | TORN-1, TORN-2     |
| same-as        | gppd_idnr   | GBR1000059         |
| same-as        | esail_id    | TORN               |
| same-as        | name        | Torness Generator  |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -2.05 |
| Latitude    |   55.81 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 1185.0                                                                         |
| Longitude                           | -2.4086                                                                        |
| Latitude                            | 55.9679                                                                        |
| Primary Fuel Type                   | Nuclear                                                                        |
| Owner                               | British Energy (now part of EDF)                                               |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1028358.0                                                                      |
| Estimated Annual Generation in 2017 | 7830.52                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     TORN-1 |     TORN-2 |
|:--------------------|-------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 5185089.12 | 5211225.59 |
| Annual Output (MWh) |   2017 | 4258394.86 | 5076008.83 |
| Annual Output (MWh) |   2018 | 4893869.72 | 3695363.89 |
| Annual Output (MWh) |   2019 | 5226702.87 | 5295549.42 |
| Annual Output (MWh) |   2020 | 5179209.53 | 5150741.45 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | TORN-1   | TORN-2   |
|:------------|:---------|:---------|
| Fuel Type   | NUCLEAR  | NUCLEAR  |

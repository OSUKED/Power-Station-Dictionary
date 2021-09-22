### Identifiers

| Relationship   | ID Type     | ID(s)                                  |
|:---------------|:------------|:---------------------------------------|
| root           | osuked_id   | 10145                                  |
| element-of     | sett_bmu_id | T_FFES-1, T_FFES-2, T_FFES-3, T_FFES-4 |
| element-of     | ngc_bmu_id  | FFES-1, FFES-2, FFES-3, FFES-4         |
| same-as        | gppd_idnr   | GBR1000152                             |
| same-as        | esail_id    | FFES                                   |
| same-as        | name        | Ffestiniog                             |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.98 |
| Latitude    |   53.01 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 360.0                                                                          |
| Longitude                           | -3.9686                                                                        |
| Latitude                            | 52.9807                                                                        |
| Primary Fuel Type                   | Hydro                                                                          |
| Owner                               | ENGIE                                                                          |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1017050.0                                                                      |
| Estimated Annual Generation in 2013 | 997.27                                                                         |
| Estimated Annual Generation in 2014 | 641.22                                                                         |
| Estimated Annual Generation in 2015 | 1120.05                                                                        |
| Estimated Annual Generation in 2016 | 795.4                                                                          |
| Estimated Annual Generation in 2017 | 793.22                                                                         |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   FFES-1 |   FFES-2 |   FFES-3 |   FFES-4 |
|:--------------------|-------:|---------:|---------:|---------:|---------:|
| Annual Output (MWh) |   2016 | 28963.61 | 51404.65 | 41315.67 | 50171.57 |
| Annual Output (MWh) |   2017 | 19595.43 | 51362.12 | 23657.77 | 51371.06 |
| Annual Output (MWh) |   2018 | 19327.44 | 42387.83 | 28273.54 | 17000.81 |
| Annual Output (MWh) |   2019 |  1888.52 |  4601.45 | 38549.66 | 23465.25 |
| Annual Output (MWh) |   2020 |     0.00 |     0.00 | 52053.77 | 59505.25 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | FFES-1   | FFES-2   | FFES-3   | FFES-4   |
|:------------|:---------|:---------|:---------|:---------|
| Fuel Type   | PS       | PS       | PS       | PS       |

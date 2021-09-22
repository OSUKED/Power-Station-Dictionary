### Identifiers

| Relationship   | ID Type     | ID(s)                                                      |
|:---------------|:------------|:-----------------------------------------------------------|
| root           | osuked_id   | 10144                                                      |
| element-of     | sett_bmu_id | T_DINO-1, T_DINO-2, T_DINO-3, T_DINO-4, T_DINO-5, T_DINO-6 |
| element-of     | ngc_bmu_id  | DINO-1, DINO-2, DINO-3, DINO-4, DINO-5, DINO-6             |
| same-as        | gppd_idnr   | GBR1000151                                                 |
| same-as        | esail_id    | DINO                                                       |
| same-as        | name        | Dinorwig                                                   |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.97 |
| Latitude    |   53.08 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 1800.0                                                                         |
| Longitude                           | -4.1032                                                                        |
| Latitude                            | 53.1181                                                                        |
| Primary Fuel Type                   | Hydro                                                                          |
| Owner                               | ENGIE                                                                          |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1017049.0                                                                      |
| Estimated Annual Generation in 2013 | 6890.49                                                                        |
| Estimated Annual Generation in 2014 | 3599.68                                                                        |
| Estimated Annual Generation in 2015 | 6509.32                                                                        |
| Estimated Annual Generation in 2016 | 4881.59                                                                        |
| Estimated Annual Generation in 2017 | 4969.86                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    DINO-1 |    DINO-2 |    DINO-3 |    DINO-4 |    DINO-5 |    DINO-6 |
|:--------------------|-------:|----------:|----------:|----------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 | 240348.65 | 592652.70 | 234400.10 | 255204.65 | 191703.10 | 781370.85 |
| Annual Output (MWh) |   2017 | 485190.80 | 530622.25 | 271695.40 | 167219.90 | 468465.45 | 224121.50 |
| Annual Output (MWh) |   2018 | 405522.80 | 189587.15 | 365114.35 | 108852.50 | 355582.85 | 439323.05 |
| Annual Output (MWh) |   2019 | 212005.00 | 188784.50 | 129424.90 | 141173.05 | 220690.90 | 375407.40 |
| Annual Output (MWh) |   2020 | 121686.80 | 163706.95 | 224881.10 | 203468.85 |  80617.75 | 220470.75 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | DINO-1   | DINO-2   | DINO-3   | DINO-4   | DINO-5   | DINO-6   |
|:------------|:---------|:---------|:---------|:---------|:---------|:---------|
| Fuel Type   | PS       | PS       | PS       | PS       | PS       | PS       |

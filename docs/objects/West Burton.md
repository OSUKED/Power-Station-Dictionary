### Identifiers

| Relationship   | ID Type     | ID(s)                                                                                             |
|:---------------|:------------|:--------------------------------------------------------------------------------------------------|
| root           | osuked_id   | 10014                                                                                             |
| element-of     | gppd_idnr   | GBR1000143, GBR1000146, GBR1000141                                                                |
| element-of     | sett_bmu_id | T_WBUPS-1, T_WBUPS-2, T_WBUPS-3, T_WBUPS-4, T_WBUGT-1, T_WBUGT-4, T_WBURB-1, T_WBURB-2, T_WBURB-3 |
| element-of     | ngc_bmu_id  | WBUPS-1, WBUPS-2, WBUPS-3, WBUPS-4, WBUGT-1, WBUGT-4, WBURB-1, WBURB-2, WBURB-3                   |
| element-of     | eutl_id     | 97220, 97223                                                                                      |
| same-as        | esail_id    | WBU                                                                                               |
| same-as        | name        | West Burton                                                                                       |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |    Value |
|:------------|---------:|
| Longitude   | -0.53833 |
| Latitude    | 53.3637  |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | GBR1000141                                                                     | GBR1000143                                                                     | GBR1000146                                                                     |
|:------------------------------------|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| Estimated Annual Generation in 2017 | 6180.55                                                                        | 3056.2                                                                         | 185.6                                                                          |
| Geolocation Source                  | GEODB                                                                          | GEODB                                                                          | GEODB                                                                          |
| Installed Capacity (MW)             | 1332.0                                                                         | 2012.0                                                                         | 40.0                                                                           |
| Latitude                            | 53.3631                                                                        | 53.3604                                                                        | 53.3631                                                                        |
| Longitude                           | -0.7976                                                                        | -0.8102                                                                        | -0.7976                                                                        |
| Owner                               | EDF Energy                                                                     | EDF Energy                                                                     | EDF Energy                                                                     |
| PLATTS-WEPP ID                      | NaN                                                                            | 1013947.0                                                                      | NaN                                                                            |
| Primary Fuel Type                   | Gas                                                                            | Coal                                                                           | Gas                                                                            |
| Source                              | Department for Business Energy & Industrial Strategy                           | Department for Business Energy & Industrial Strategy                           | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/eutl/datapackage.json">Eutl</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute       |    97220 |   97223 |
|:----------------|---------:|--------:|
| Tonnes CO2 2005 |  8419658 |         |
| Tonnes CO2 2006 |  8900616 |         |
| Tonnes CO2 2007 |  9324306 |         |
| Tonnes CO2 2008 |  9650932 |       0 |
| Tonnes CO2 2009 |  7165862 |       0 |
| Tonnes CO2 2010 |  5095438 |       0 |
| Tonnes CO2 2011 |  6075254 |       0 |
| Tonnes CO2 2012 | 10780107 |  187209 |
| Tonnes CO2 2013 | 10887300 | 1057877 |
| Tonnes CO2 2014 |  9208141 | 1842770 |
| Tonnes CO2 2015 |  7724207 | 2371371 |
| Tonnes CO2 2016 |  1165058 | 2029550 |
| Tonnes CO2 2017 |  1766100 | 2491134 |
| Tonnes CO2 2018 |  1679509 | 2573845 |
| Tonnes CO2 2019 |   790510 | 2380046 |
| Tonnes CO2 2020 |  1051651 | 1884207 |

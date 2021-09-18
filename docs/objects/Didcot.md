### Identifiers

| Relationship   | ID Type     | ID(s)                                                                                                                                  |
|:---------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| root           | osuked_id   | 10001                                                                                                                                  |
| element-of     | gppd_idnr   | GBR1000377, GBR1000369                                                                                                                 |
| element-of     | sett_bmu_id | T_DIDC1, T_DIDC2, T_DIDC4, T_DIDC3, T_DIDC1G, T_DIDC2G, T_DIDC3G, T_DIDC4G, E_DIDC1G, E_DIDC2G, E_DIDC3G, E_DIDC4G, T_DIDCB5, T_DIDCB6 |
| element-of     | ngc_bmu_id  | DIDC1, DIDC2, DIDC4, DIDC3, DIDC1G, DIDC2G, DIDC3G, DIDC4G, DIDC01G, DIDC02G, DIDC03G, DIDC04G, DIDCB5, DIDCB6                         |
| same-as        | esail_id    | DIDC                                                                                                                                   |
| same-as        | name        | Didcot                                                                                                                                 |
| same-as        | eutl_id     | 97165                                                                                                                                  |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |    Value |
|:------------|---------:|
| Longitude   | -1.26757 |
| Latitude    | 51.6236  |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | GBR1000369                                                                     | GBR1000377                                                                     |
|:------------------------------------|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| Estimated Annual Generation in 2017 | 6820.88                                                                        | 464.0                                                                          |
| Geolocation Source                  | GEODB                                                                          | GEODB                                                                          |
| Installed Capacity (MW)             | 1470.0                                                                         | 100.0                                                                          |
| Latitude                            | 51.6246                                                                        | 51.6246                                                                        |
| Longitude                           | -1.2683                                                                        | -1.2683                                                                        |
| Owner                               | RWE Npower Plc                                                                 | RWE Npower Plc                                                                 |
| PLATTS-WEPP ID                      | 1023591.0                                                                      | NaN                                                                            |
| Primary Fuel Type                   | Gas                                                                            | Gas                                                                            |
| Source                              | Department for Business Energy & Industrial Strategy                           | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/eutl/datapackage.json">Eutl</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute       |   Value |
|:----------------|--------:|
| Tonnes CO2 2005 | 6342700 |
| Tonnes CO2 2006 | 7184281 |
| Tonnes CO2 2007 | 5231425 |
| Tonnes CO2 2008 | 5182660 |
| Tonnes CO2 2009 | 2435748 |
| Tonnes CO2 2010 | 1795512 |
| Tonnes CO2 2011 | 2181952 |
| Tonnes CO2 2012 | 6838317 |
| Tonnes CO2 2013 | 1737804 |
| Tonnes CO2 2014 |       0 |
| Tonnes CO2 2015 |       0 |

### Identifiers

| Relationship   | ID Type     | ID(s)                                                   |
|:---------------|:------------|:--------------------------------------------------------|
| root           | osuked_id   | 10002                                                   |
| element-of     | gppd_idnr   | GBR1000374, GBR1000375                                  |
| element-of     | sett_bmu_id | T_ABTH7, T_ABTH8, T_ABTH9, T_ABTH7G, T_ABTH8G, T_ABTH9G |
| element-of     | ngc_bmu_id  | ABTH7, ABTH8, ABTH9, ABTH7G, ABTH8G, ABTH9G             |
| same-as        | esail_id    | ABTH                                                    |
| same-as        | name        | Aberthaw B                                              |
| same-as        | eutl_id     | 97175                                                   |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.40 |
| Latitude    |   51.39 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | GBR1000374                                                                     | GBR1000375                                                                     |
|:------------------------------------|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| Estimated Annual Generation in 2017 | 2409.11                                                                        | 236.64                                                                         |
| Geolocation Source                  | GEODB                                                                          | CARMA                                                                          |
| Installed Capacity (MW)             | 1586.0                                                                         | 51.0                                                                           |
| Latitude                            | 51.3873                                                                        | 51.3875                                                                        |
| Longitude                           | -3.4049                                                                        | -3.4068                                                                        |
| Owner                               | RWE Npower Plc                                                                 | RWE Npower Plc                                                                 |
| PLATTS-WEPP ID                      | 1023577.0                                                                      | NaN                                                                            |
| Primary Fuel Type                   | Coal                                                                           | Gas                                                                            |
| Source                              | Department for Business Energy & Industrial Strategy                           | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 5264973.00 |
| CO2 Emissions (Tonnes) |   2006 | 7340340.00 |
| CO2 Emissions (Tonnes) |   2007 | 4186423.00 |
| CO2 Emissions (Tonnes) |   2008 | 7027839.00 |
| CO2 Emissions (Tonnes) |   2009 | 5002555.00 |
| CO2 Emissions (Tonnes) |   2010 | 4739140.00 |
| CO2 Emissions (Tonnes) |   2011 | 4829978.00 |
| CO2 Emissions (Tonnes) |   2012 | 8229115.00 |
| CO2 Emissions (Tonnes) |   2013 | 8504964.00 |
| CO2 Emissions (Tonnes) |   2014 | 6038198.00 |
| CO2 Emissions (Tonnes) |   2015 | 6682528.00 |
| CO2 Emissions (Tonnes) |   2016 | 5910278.00 |
| CO2 Emissions (Tonnes) |   2017 | 2296592.00 |
| CO2 Emissions (Tonnes) |   2018 |  495388.00 |
| CO2 Emissions (Tonnes) |   2019 |  660075.00 |
| CO2 Emissions (Tonnes) |   2020 |     235.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |      ABTH7 |   ABTH7G |      ABTH8 |   ABTH8G |      ABTH9 |   ABTH9G |
|:--------------------|-------:|-----------:|---------:|-----------:|---------:|-----------:|---------:|
| Annual Output (MWh) |   2016 | 2386727.61 |    30.49 | 2036344.12 |    27.31 | 2476881.29 |    30.24 |
| Annual Output (MWh) |   2017 |  890904.03 |     0.00 |  935056.72 |     5.31 |  877525.08 |    24.54 |
| Annual Output (MWh) |   2018 |  173340.22 |   125.46 |  177871.12 |    77.42 |  179066.76 |    81.57 |
| Annual Output (MWh) |   2019 |  148814.22 |    54.46 |  133844.60 |    51.56 |  435824.00 |    62.01 |
| Annual Output (MWh) |   2020 |       0.00 |    24.71 |       0.00 |    18.63 |       0.00 |    26.41 |

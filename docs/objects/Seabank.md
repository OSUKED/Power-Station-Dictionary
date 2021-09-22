### Identifiers

| Relationship   | ID Type     | ID(s)              |
|:---------------|:------------|:-------------------|
| root           | osuked_id   | 10053              |
| element-of     | sett_bmu_id | T_SEAB-1, T_SEAB-2 |
| element-of     | ngc_bmu_id  | SEAB-1, SEAB-2     |
| same-as        | gppd_idnr   | GBR1000480         |
| same-as        | esail_id    | SEAB               |
| same-as        | name        | Seabank            |
| same-as        | eutl_id     | 96899              |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -2.61 |
| Latitude    |   51.48 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 410.0                                                                          |
| Longitude                           | -2.67                                                                          |
| Latitude                            | 51.5392                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | Seabank Power Limited                                                          |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1028387.0                                                                      |
| Estimated Annual Generation in 2017 | 1902.42                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 1420032.00 |
| CO2 Emissions (Tonnes) |   2006 | 1960340.00 |
| CO2 Emissions (Tonnes) |   2007 | 2261133.00 |
| CO2 Emissions (Tonnes) |   2008 | 2384033.00 |
| CO2 Emissions (Tonnes) |   2009 | 2796747.00 |
| CO2 Emissions (Tonnes) |   2010 | 2722964.00 |
| CO2 Emissions (Tonnes) |   2011 | 1756875.00 |
| CO2 Emissions (Tonnes) |   2012 |  558154.00 |
| CO2 Emissions (Tonnes) |   2013 |  724808.00 |
| CO2 Emissions (Tonnes) |   2014 |  977917.00 |
| CO2 Emissions (Tonnes) |   2015 |  726450.00 |
| CO2 Emissions (Tonnes) |   2016 | 1633611.00 |
| CO2 Emissions (Tonnes) |   2017 | 2106161.00 |
| CO2 Emissions (Tonnes) |   2018 | 1308953.00 |
| CO2 Emissions (Tonnes) |   2019 | 1125229.00 |
| CO2 Emissions (Tonnes) |   2020 |  961367.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     SEAB-1 |     SEAB-2 |
|:--------------------|-------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 3750212.46 |  707328.44 |
| Annual Output (MWh) |   2017 | 4426354.56 | 1347746.34 |
| Annual Output (MWh) |   2018 | 2222597.68 | 1026782.77 |
| Annual Output (MWh) |   2019 | 2086463.83 |  919074.61 |
| Annual Output (MWh) |   2020 | 1875384.85 |  665433.33 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | SEAB-1   | SEAB-2   |
|:------------|:---------|:---------|
| Fuel Type   | CCGT     | CCGT     |

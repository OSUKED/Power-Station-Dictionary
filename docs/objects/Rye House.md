### Identifiers

| Relationship   | ID Type     | ID(s)      |
|:---------------|:------------|:-----------|
| root           | osuked_id   | 10051      |
| element-of     | sett_bmu_id | T_RYHPS-1  |
| element-of     | ngc_bmu_id  | RYHPS-1    |
| same-as        | gppd_idnr   | GBR1000466 |
| same-as        | esail_id    | RYHPS      |
| same-as        | name        | Rye House  |
| same-as        | eutl_id     | 96908      |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.29 |
| Latitude    |   51.82 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 715.0                                                                          |
| Longitude                           | 0.0094                                                                         |
| Latitude                            | 51.7626                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | Scottish Power: Thermal                                                        |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1025737.0                                                                      |
| Estimated Annual Generation in 2017 | 3317.64                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 1372095.00 |
| CO2 Emissions (Tonnes) |   2006 |  726226.00 |
| CO2 Emissions (Tonnes) |   2007 | 1223877.00 |
| CO2 Emissions (Tonnes) |   2008 | 1694516.00 |
| CO2 Emissions (Tonnes) |   2009 | 1575331.00 |
| CO2 Emissions (Tonnes) |   2010 | 1308016.00 |
| CO2 Emissions (Tonnes) |   2011 |  568074.00 |
| CO2 Emissions (Tonnes) |   2012 |  341234.00 |
| CO2 Emissions (Tonnes) |   2013 |  243176.00 |
| CO2 Emissions (Tonnes) |   2014 |  177365.00 |
| CO2 Emissions (Tonnes) |   2015 |   76018.00 |
| CO2 Emissions (Tonnes) |   2016 |  509656.00 |
| CO2 Emissions (Tonnes) |   2017 |  351574.00 |
| CO2 Emissions (Tonnes) |   2018 |  183916.00 |
| CO2 Emissions (Tonnes) |   2019 |  261688.00 |
| CO2 Emissions (Tonnes) |   2020 |  185816.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |      Value |
|:--------------------|-------:|-----------:|
| Annual Output (MWh) |   2016 | 1140005.01 |
| Annual Output (MWh) |   2017 |  607796.29 |
| Annual Output (MWh) |   2018 |  405364.15 |
| Annual Output (MWh) |   2019 |  582315.55 |
| Annual Output (MWh) |   2020 |  430420.14 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | CCGT    |

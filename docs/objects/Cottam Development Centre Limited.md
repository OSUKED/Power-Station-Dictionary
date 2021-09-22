### Identifiers

| Relationship   | ID Type     | ID(s)                             |
|:---------------|:------------|:----------------------------------|
| root           | osuked_id   | 10032                             |
| element-of     | sett_bmu_id | T_CDCL-1                          |
| element-of     | ngc_bmu_id  | CDCL-1                            |
| same-as        | gppd_idnr   | GBR1000493                        |
| same-as        | esail_id    | CDCL                              |
| same-as        | name        | Cottam Development Centre Limited |
| same-as        | eutl_id     | 97059                             |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.87 |
| Latitude    |   53.22 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 395.0                                                                          |
| Longitude                           | -0.7858                                                                        |
| Latitude                            | 53.3051                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | Uniper UK Limited                                                              |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1064726.0                                                                      |
| Estimated Annual Generation in 2017 | 1832.82                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 |  534303.00 |
| CO2 Emissions (Tonnes) |   2006 |  609504.00 |
| CO2 Emissions (Tonnes) |   2007 |  777490.00 |
| CO2 Emissions (Tonnes) |   2008 |  912995.00 |
| CO2 Emissions (Tonnes) |   2009 | 1022877.00 |
| CO2 Emissions (Tonnes) |   2010 |  867789.00 |
| CO2 Emissions (Tonnes) |   2011 |  662863.00 |
| CO2 Emissions (Tonnes) |   2012 |  105815.00 |
| CO2 Emissions (Tonnes) |   2013 |  280213.00 |
| CO2 Emissions (Tonnes) |   2014 |  357058.00 |
| CO2 Emissions (Tonnes) |   2015 |  239994.00 |
| CO2 Emissions (Tonnes) |   2016 |  758011.00 |
| CO2 Emissions (Tonnes) |   2017 |  695591.00 |
| CO2 Emissions (Tonnes) |   2018 | 1061719.00 |
| CO2 Emissions (Tonnes) |   2019 |  903829.00 |
| CO2 Emissions (Tonnes) |   2020 |  732716.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |      Value |
|:--------------------|-------:|-----------:|
| Annual Output (MWh) |   2016 | 2038860.99 |
| Annual Output (MWh) |   2017 | 1859874.21 |
| Annual Output (MWh) |   2018 | 2835308.25 |
| Annual Output (MWh) |   2019 | 2451134.16 |
| Annual Output (MWh) |   2020 | 1924425.90 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | CCGT    |

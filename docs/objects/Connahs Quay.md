### Identifiers

| Relationship   | ID Type     | ID(s)                                      |
|:---------------|:------------|:-------------------------------------------|
| root           | osuked_id   | 10029                                      |
| element-of     | sett_bmu_id | T_CNQPS-1, T_CNQPS-2, T_CNQPS-3, T_CNQPS-4 |
| element-of     | ngc_bmu_id  | CNQPS-1, CNQPS-2, CNQPS-3, CNQPS-4         |
| same-as        | gppd_idnr   | GBR1000492                                 |
| same-as        | esail_id    | CNQPS                                      |
| same-as        | name        | Connahs Quay                               |
| same-as        | eutl_id     | 97054                                      |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.08 |
| Latitude    |   53.23 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 1380.0                                                                         |
| Longitude                           | -3.0815                                                                        |
| Latitude                            | 53.2317                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | Uniper UK Limited                                                              |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1025709.0                                                                      |
| Estimated Annual Generation in 2017 | 6403.27                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 3434321.00 |
| CO2 Emissions (Tonnes) |   2006 | 3158476.00 |
| CO2 Emissions (Tonnes) |   2007 | 3370721.00 |
| CO2 Emissions (Tonnes) |   2008 | 3303359.00 |
| CO2 Emissions (Tonnes) |   2009 | 3212444.00 |
| CO2 Emissions (Tonnes) |   2010 | 2974382.00 |
| CO2 Emissions (Tonnes) |   2011 | 1836582.00 |
| CO2 Emissions (Tonnes) |   2012 |  905062.00 |
| CO2 Emissions (Tonnes) |   2013 |  779233.00 |
| CO2 Emissions (Tonnes) |   2014 |  771177.00 |
| CO2 Emissions (Tonnes) |   2015 | 1104678.00 |
| CO2 Emissions (Tonnes) |   2016 | 1978392.00 |
| CO2 Emissions (Tonnes) |   2017 | 1032450.00 |
| CO2 Emissions (Tonnes) |   2018 |  805523.00 |
| CO2 Emissions (Tonnes) |   2019 |  886409.00 |
| CO2 Emissions (Tonnes) |   2020 |  836748.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   CNQPS-1 |    CNQPS-2 |    CNQPS-3 |    CNQPS-4 |
|:--------------------|-------:|----------:|-----------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 999887.43 | 1613115.25 | 1047778.77 | 1084023.55 |
| Annual Output (MWh) |   2017 | 579713.34 |  900435.63 |  588513.11 |  427931.85 |
| Annual Output (MWh) |   2018 | 556062.82 |  463354.04 |  481653.52 |  404696.44 |
| Annual Output (MWh) |   2019 | 808350.10 |  275342.45 |  430069.06 |  693619.92 |
| Annual Output (MWh) |   2020 | 695340.07 |  400037.97 |  228272.75 |  636543.18 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | CNQPS-1   | CNQPS-2   | CNQPS-3   | CNQPS-4   |
|:------------|:----------|:----------|:----------|:----------|
| Fuel Type   | CCGT      | CCGT      | CCGT      | CCGT      |

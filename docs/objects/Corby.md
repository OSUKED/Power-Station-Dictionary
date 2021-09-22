### Identifiers

| Relationship   | ID Type     | ID(s)      |
|:---------------|:------------|:-----------|
| root           | osuked_id   | 10030      |
| element-of     | sett_bmu_id | E_CORB-1   |
| element-of     | ngc_bmu_id  | CORB-1     |
| same-as        | gppd_idnr   | GBR1000077 |
| same-as        | esail_id    | CORB       |
| same-as        | name        | Corby      |
| same-as        | eutl_id     | 97634      |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.87 |
| Latitude    |   52.25 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 401.0                                                                          |
| Longitude                           | -0.6814                                                                        |
| Latitude                            | 52.5104                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | Corby Power Ltd                                                                |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1013306.0                                                                      |
| Estimated Annual Generation in 2017 | 1860.66                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |     Value |
|:-----------------------|-------:|----------:|
| CO2 Emissions (Tonnes) |   2005 | 294519.00 |
| CO2 Emissions (Tonnes) |   2006 | 340108.00 |
| CO2 Emissions (Tonnes) |   2007 | 562212.00 |
| CO2 Emissions (Tonnes) |   2008 | 637026.00 |
| CO2 Emissions (Tonnes) |   2009 | 728752.00 |
| CO2 Emissions (Tonnes) |   2010 | 374201.00 |
| CO2 Emissions (Tonnes) |   2011 | 121892.00 |
| CO2 Emissions (Tonnes) |   2012 |  33532.00 |
| CO2 Emissions (Tonnes) |   2013 | 115686.00 |
| CO2 Emissions (Tonnes) |   2014 | 154331.00 |
| CO2 Emissions (Tonnes) |   2015 | 126270.00 |
| CO2 Emissions (Tonnes) |   2016 |   2256.00 |
| CO2 Emissions (Tonnes) |   2017 |  17488.00 |
| CO2 Emissions (Tonnes) |   2018 |  36500.00 |
| CO2 Emissions (Tonnes) |   2019 |  18639.00 |
| CO2 Emissions (Tonnes) |   2020 |   6647.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    Value |
|:--------------------|-------:|---------:|
| Annual Output (MWh) |   2016 |  3485.65 |
| Annual Output (MWh) |   2017 | 35015.55 |
| Annual Output (MWh) |   2018 | 64012.91 |
| Annual Output (MWh) |   2019 | 37054.11 |
| Annual Output (MWh) |   2020 | 11245.85 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | CCGT    |

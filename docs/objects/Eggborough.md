### Identifiers

| Relationship   | ID Type     | ID(s)                                      |
|:---------------|:------------|:-------------------------------------------|
| root           | osuked_id   | 10005                                      |
| element-of     | sett_bmu_id | T_EGGPS-1, T_EGGPS-2, T_EGGPS-3, T_EGGPS-4 |
| element-of     | ngc_bmu_id  | EGGPS-1, EGGPS-2, EGGPS-3, EGGPS-4         |
| same-as        | gppd_idnr   | GBR1000147                                 |
| same-as        | esail_id    | EGGPS                                      |
| same-as        | name        | Eggborough                                 |
| same-as        | eutl_id     | 97445                                      |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.83 |
| Latitude    |   53.71 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 1960.0                                                                         |
| Longitude                           | -1.1269                                                                        |
| Latitude                            | 53.7116                                                                        |
| Primary Fuel Type                   | Coal                                                                           |
| Owner                               | Eggborough Power Ltd                                                           |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1023595.0                                                                      |
| Estimated Annual Generation in 2017 | 2977.22                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |       Value |
|:-----------------------|-------:|------------:|
| CO2 Emissions (Tonnes) |   2005 |  7215160.00 |
| CO2 Emissions (Tonnes) |   2006 |  7649883.00 |
| CO2 Emissions (Tonnes) |   2007 |  7819665.00 |
| CO2 Emissions (Tonnes) |   2008 |  8114954.00 |
| CO2 Emissions (Tonnes) |   2009 |  5493019.00 |
| CO2 Emissions (Tonnes) |   2010 |  4581301.00 |
| CO2 Emissions (Tonnes) |   2011 |  5094741.00 |
| CO2 Emissions (Tonnes) |   2012 | 10222778.00 |
| CO2 Emissions (Tonnes) |   2013 | 11495905.00 |
| CO2 Emissions (Tonnes) |   2014 |  7799832.00 |
| CO2 Emissions (Tonnes) |   2015 |  4748504.00 |
| CO2 Emissions (Tonnes) |   2016 |  2098992.00 |
| CO2 Emissions (Tonnes) |   2017 |  1014334.00 |
| CO2 Emissions (Tonnes) |   2018 |   540497.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   EGGPS-1 |   EGGPS-2 |   EGGPS-3 |   EGGPS-4 |
|:--------------------|-------:|----------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 | 436598.37 | 267020.77 | 586067.98 | 953048.31 |
| Annual Output (MWh) |   2017 |  62280.33 |  25789.49 | 452437.08 | 488897.67 |
| Annual Output (MWh) |   2018 |  30842.92 |  17390.11 | 260354.27 | 230801.76 |
| Annual Output (MWh) |   2019 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2020 |      0.00 |      0.00 |      0.00 |      0.00 |

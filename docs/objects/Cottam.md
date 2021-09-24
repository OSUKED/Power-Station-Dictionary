### Identifiers

| Relationship   | ID Type              | ID(s)                                                                  |
|:---------------|:---------------------|:-----------------------------------------------------------------------|
| Root           | OSUKED ID            | 10003                                                                  |
| Related        | Settlement BMU ID    | T_COTPS-1, T_COTPS-2, T_COTPS-3, T_COTPS-4                             |
| Related        | National Grid BMU ID | COTPS-1, COTPS-2, COTPS-3, COTPS-4                                     |
| Related        | EIC ID               | 48W00000COTPS-1Q, 48W00000COTPS-2O, 48W00000COTPS-3M, 48W00000COTPS-4K |
| Equivalent     | GPPD ID              | GBR1000142                                                             |
| Equivalent     | ESAIL ID             | COTPS                                                                  |
| Equivalent     | Common Name          | Cottam                                                                 |
| Equivalent     | EUTL ID              | 97778                                                                  |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.65 |
| Latitude    |   53.25 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 2008.0                                                                         |
| Longitude                           | -0.7815                                                                        |
| Latitude                            | 53.304                                                                         |
| Primary Fuel Type                   | Coal                                                                           |
| Owner                               | EDF Energy                                                                     |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1025710.0                                                                      |
| Estimated Annual Generation in 2017 | 3050.13                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |       Value |
|:-----------------------|-------:|------------:|
| CO2 Emissions (Tonnes) |   2005 |  8068565.00 |
| CO2 Emissions (Tonnes) |   2006 | 10029024.00 |
| CO2 Emissions (Tonnes) |   2007 | 10240663.00 |
| CO2 Emissions (Tonnes) |   2008 | 10157213.00 |
| CO2 Emissions (Tonnes) |   2009 |  8426332.00 |
| CO2 Emissions (Tonnes) |   2010 |  8715015.00 |
| CO2 Emissions (Tonnes) |   2011 |  8863488.00 |
| CO2 Emissions (Tonnes) |   2012 |  9889284.00 |
| CO2 Emissions (Tonnes) |   2013 | 10171477.00 |
| CO2 Emissions (Tonnes) |   2014 |  8846877.00 |
| CO2 Emissions (Tonnes) |   2015 |  6756444.00 |
| CO2 Emissions (Tonnes) |   2016 |  1565134.00 |
| CO2 Emissions (Tonnes) |   2017 |  2907114.00 |
| CO2 Emissions (Tonnes) |   2018 |  2900716.00 |
| CO2 Emissions (Tonnes) |   2019 |  1378192.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   COTPS-1 |    COTPS-2 |   COTPS-3 |   COTPS-4 |
|:--------------------|-------:|----------:|-----------:|----------:|----------:|
| Annual Output (MWh) |   2016 | 462987.97 |  426297.23 | 557408.09 | 193660.58 |
| Annual Output (MWh) |   2017 | 747476.45 | 1049205.65 | 782286.29 | 596559.60 |
| Annual Output (MWh) |   2018 | 735835.82 |  860044.00 | 656608.25 | 569976.73 |
| Annual Output (MWh) |   2019 | 546867.90 |  620486.22 | 378151.60 | 201143.12 |
| Annual Output (MWh) |   2020 |      0.00 |       0.00 |      0.00 |      0.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   COTPS-1 |   COTPS-2 |   COTPS-3 |   COTPS-4 |
|:----------------------|-------:|----------:|----------:|----------:|----------:|
| Capture Price (£/MWh) |   2016 |     61.44 |     60.33 |     61.75 |     57.83 |
| Capture Price (£/MWh) |   2017 |     56.51 |     53.75 |     55.58 |     56.68 |
| Capture Price (£/MWh) |   2018 |     66.14 |     64.48 |     61.44 |     69.53 |
| Capture Price (£/MWh) |   2019 |     51.03 |     52.76 |     49.39 |     59.93 |

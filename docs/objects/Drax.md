### Identifiers

| Relationship   | ID Type     | ID(s)                                                                                                  |
|:---------------|:------------|:-------------------------------------------------------------------------------------------------------|
| root           | osuked_id   | 10004                                                                                                  |
| element-of     | gppd_idnr   | GBR0000174, GBR1000112                                                                                 |
| element-of     | sett_bmu_id | T_DRAXX-1, T_DRAXX-2, T_DRAXX-3, T_DRAXX-4, T_DRAXX-5, T_DRAXX-6, T_DRAXX-10G, T_DRAXX-12G, T_DRAXX-9G |
| element-of     | ngc_bmu_id  | DRAXX-1, DRAXX-2, DRAXX-3, DRAXX-4, DRAXX-5, DRAXX-6, DRAXX-10G, DRAXX-12G, DRAXX-9G                   |
| same-as        | esail_id    | DRAXX                                                                                                  |
| same-as        | name        | Drax                                                                                                   |
| same-as        | eutl_id     | 96842                                                                                                  |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.63 |
| Latitude    |   53.75 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | GBR0000174                                                               | GBR1000112                                                                     |
|:------------------------------------|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| Estimated Annual Generation in 2017 | 3007.6                                                                   | 348.0                                                                          |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    | CARMA                                                                          |
| Installed Capacity (MW)             | 1980.0                                                                   | 75.0                                                                           |
| Latitude                            | 53.7356                                                                  | 53.7364                                                                        |
| Longitude                           | -0.9911                                                                  | -0.9981                                                                        |
| Owner                               | Drax Power                                                               | Drax Power Ltd                                                                 |
| PLATTS-WEPP ID                      | 1023594.0                                                                | NaN                                                                            |
| Primary Fuel Type                   | Coal                                                                     | Gas                                                                            |
| Secondary Fuel Type                 | Biomass                                                                  | None                                                                           |
| Source                              | UK Renewable Energy Planning Database                                    | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |       Value |
|:-----------------------|-------:|------------:|
| CO2 Emissions (Tonnes) |   2005 | 20771624.00 |
| CO2 Emissions (Tonnes) |   2006 | 22764847.00 |
| CO2 Emissions (Tonnes) |   2007 | 22160413.00 |
| CO2 Emissions (Tonnes) |   2008 | 22299778.00 |
| CO2 Emissions (Tonnes) |   2009 | 19851702.00 |
| CO2 Emissions (Tonnes) |   2010 | 22392487.00 |
| CO2 Emissions (Tonnes) |   2011 | 21465607.00 |
| CO2 Emissions (Tonnes) |   2012 | 22694684.00 |
| CO2 Emissions (Tonnes) |   2013 | 20317580.00 |
| CO2 Emissions (Tonnes) |   2014 | 16581565.00 |
| CO2 Emissions (Tonnes) |   2015 | 13173987.00 |
| CO2 Emissions (Tonnes) |   2016 |  6171178.00 |
| CO2 Emissions (Tonnes) |   2017 |  6215220.00 |
| CO2 Emissions (Tonnes) |   2018 |  4138782.00 |
| CO2 Emissions (Tonnes) |   2019 |   725751.00 |
| CO2 Emissions (Tonnes) |   2020 |  1527003.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    DRAXX-1 |   DRAXX-10G |   DRAXX-12G |    DRAXX-2 |    DRAXX-3 |    DRAXX-4 |    DRAXX-5 |    DRAXX-6 |   DRAXX-9G |
|:--------------------|-------:|-----------:|------------:|------------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 5014662.68 |       42.71 |       23.04 | 4591242.68 | 3270868.97 | 2832039.08 | 2138424.28 | 2088242.12 |      27.69 |
| Annual Output (MWh) |   2017 | 4036655.43 |      135.21 |       81.50 | 4165307.98 | 4754720.16 | 2515965.61 | 3020489.48 | 1814090.70 |     134.02 |
| Annual Output (MWh) |   2018 | 5272782.11 |      194.75 |      200.66 | 3775143.04 | 3765275.16 | 1827026.43 | 1671123.54 | 1979873.84 |     123.50 |
| Annual Output (MWh) |   2019 | 4759282.28 |      178.77 |      139.35 | 2833499.66 | 3585051.60 | 2607930.56 |  416402.33 |  297244.18 |      44.04 |
| Annual Output (MWh) |   2020 | 5016991.29 |      218.85 |      242.96 | 3925674.33 | 2675650.95 | 2844261.94 |  838405.28 |  839832.47 |      59.72 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | DRAXX-1   | DRAXX-10G   | DRAXX-12G   | DRAXX-2   | DRAXX-3   | DRAXX-4   | DRAXX-5   | DRAXX-6   | DRAXX-9G   |
|:------------|:----------|:------------|:------------|:----------|:----------|:----------|:----------|:----------|:-----------|
| Fuel Type   | BIOMASS   | OCGT        | OCGT        | BIOMASS   | BIOMASS   | BIOMASS   | COAL      | COAL      | OCGT       |

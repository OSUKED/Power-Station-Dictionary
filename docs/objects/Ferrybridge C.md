### Identifiers

| Relationship   | ID Type     | ID(s)                                                        |
|:---------------|:------------|:-------------------------------------------------------------|
| root           | osuked_id   | 10006                                                        |
| element-of     | sett_bmu_id | T_FERR-3, T_FERR-4, T_FERR-1, T_FERR-2, T_FERR-5G, T_FERR-8G |
| element-of     | ngc_bmu_id  | FERR-3, FERR-4, FERR-1, FERR-2, FERR-5G, FERR-8G             |
| same-as        | gppd_idnr   | GBR0000116                                                   |
| same-as        | esail_id    | FERR                                                         |
| same-as        | name        | Ferrybridge C                                                |
| same-as        | eutl_id     | 98253                                                        |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -1.03 |
| Latitude    |   53.74 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute               | Value                                                                    |
|:------------------------|:-------------------------------------------------------------------------|
| Installed Capacity (MW) | 79.0                                                                     |
| Longitude               | -1.2819                                                                  |
| Latitude                | 53.7164                                                                  |
| Primary Fuel Type       | Biomass                                                                  |
| Owner                   | Scottish and Southern Energy (SSE)                                       |
| Source                  | UK Renewable Energy Planning Database                                    |
| URL                     | https://www.gov.uk/government/collections/renewable-energy-planning-data |
| Geolocation Source      | UK Renewable Energy Planning Database                                    |
| PLATTS-WEPP ID          | 1076625.0                                                                |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 8413055.00 |
| CO2 Emissions (Tonnes) |   2006 | 8865656.00 |
| CO2 Emissions (Tonnes) |   2007 | 8287912.00 |
| CO2 Emissions (Tonnes) |   2008 | 3728402.00 |
| CO2 Emissions (Tonnes) |   2009 | 4052365.00 |
| CO2 Emissions (Tonnes) |   2010 | 4830312.00 |
| CO2 Emissions (Tonnes) |   2011 | 7123621.00 |
| CO2 Emissions (Tonnes) |   2012 | 9010659.00 |
| CO2 Emissions (Tonnes) |   2013 | 8311632.00 |
| CO2 Emissions (Tonnes) |   2014 | 3053338.00 |
| CO2 Emissions (Tonnes) |   2015 | 2328454.00 |
| CO2 Emissions (Tonnes) |   2016 |  742098.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   FERR-1 |   FERR-2 |    FERR-3 |   FERR-5G |
|:--------------------|-------:|---------:|---------:|----------:|----------:|
| Annual Output (MWh) |   2016 |     0.04 |     0.03 | 798832.27 |      0.00 |
| Annual Output (MWh) |   2017 |     0.00 |     0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2018 |     0.00 |     0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2019 |     0.00 |     0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2020 |     0.00 |     0.00 |      0.00 |      0.00 |

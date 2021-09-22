### Identifiers

| Relationship   | ID Type     | ID(s)                                    |
|:---------------|:------------|:-----------------------------------------|
| root           | osuked_id   | 10101                                    |
| element-of     | sett_bmu_id | T_PEHE-1, T_PEHE-2, T_PEHE-3G, T_PEHE-4G |
| element-of     | ngc_bmu_id  | PEHE-1, PEHE-2, PEHE-3, PEHE-4           |
| same-as        | gppd_idnr   | GBR2000723                               |
| same-as        | esail_id    | PEHE                                     |
| same-as        | name        | Peterhead                                |
| same-as        | eutl_id     | 97910                                    |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -1.87 |
| Latitude    |   57.53 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value   |
|:------------------------------------|:--------|
| Installed Capacity (MW)             | 1180.0  |
| Longitude                           | -1.7889 |
| Latitude                            | 57.4772 |
| Primary Fuel Type                   | Gas     |
| Geolocation Source                  | WRI     |
| Estimated Annual Generation in 2017 | 5475.26 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 2549691.00 |
| CO2 Emissions (Tonnes) |   2006 | 3448929.00 |
| CO2 Emissions (Tonnes) |   2007 | 3236835.00 |
| CO2 Emissions (Tonnes) |   2008 | 3663680.00 |
| CO2 Emissions (Tonnes) |   2009 | 2755572.00 |
| CO2 Emissions (Tonnes) |   2010 | 2482116.00 |
| CO2 Emissions (Tonnes) |   2011 | 2322849.00 |
| CO2 Emissions (Tonnes) |   2012 | 1412931.00 |
| CO2 Emissions (Tonnes) |   2013 | 1316371.00 |
| CO2 Emissions (Tonnes) |   2014 |  330961.00 |
| CO2 Emissions (Tonnes) |   2015 |   54696.00 |
| CO2 Emissions (Tonnes) |   2016 |  601641.00 |
| CO2 Emissions (Tonnes) |   2017 |  950298.00 |
| CO2 Emissions (Tonnes) |   2018 | 1911466.00 |
| CO2 Emissions (Tonnes) |   2019 | 1578522.00 |
| CO2 Emissions (Tonnes) |   2020 | 1293967.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |      Value |
|:--------------------|-------:|-----------:|
| Annual Output (MWh) |   2016 | 1490503.60 |
| Annual Output (MWh) |   2017 | 2468365.63 |
| Annual Output (MWh) |   2018 | 4794831.14 |
| Annual Output (MWh) |   2019 | 4207197.31 |
| Annual Output (MWh) |   2020 | 3438142.04 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | CCGT    |

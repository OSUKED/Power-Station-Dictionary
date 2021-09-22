### Identifiers

| Relationship   | ID Type     | ID(s)      |
|:---------------|:------------|:-----------|
| root           | osuked_id   | 10055      |
| element-of     | sett_bmu_id | E_SHOS-1   |
| element-of     | ngc_bmu_id  | SHOS-1     |
| same-as        | gppd_idnr   | GBR2000769 |
| same-as        | esail_id    | SHOS       |
| same-as        | name        | Shoreham   |
| same-as        | eutl_id     | 96911      |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.25 |
| Latitude    |   50.88 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value   |
|:------------------------------------|:--------|
| Installed Capacity (MW)             | 420.0   |
| Longitude                           | -0.2311 |
| Latitude                            | 50.8292 |
| Primary Fuel Type                   | Gas     |
| Geolocation Source                  | GEO     |
| Estimated Annual Generation in 2017 | 1948.82 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 |  942612.00 |
| CO2 Emissions (Tonnes) |   2006 |  788144.00 |
| CO2 Emissions (Tonnes) |   2007 |  296186.00 |
| CO2 Emissions (Tonnes) |   2008 | 1044619.00 |
| CO2 Emissions (Tonnes) |   2009 |  960770.00 |
| CO2 Emissions (Tonnes) |   2010 |  956535.00 |
| CO2 Emissions (Tonnes) |   2011 |  984985.00 |
| CO2 Emissions (Tonnes) |   2012 |  139866.00 |
| CO2 Emissions (Tonnes) |   2013 |  192303.00 |
| CO2 Emissions (Tonnes) |   2014 |  143622.00 |
| CO2 Emissions (Tonnes) |   2015 |  562081.00 |
| CO2 Emissions (Tonnes) |   2016 |  827671.00 |
| CO2 Emissions (Tonnes) |   2017 |  940204.00 |
| CO2 Emissions (Tonnes) |   2018 |  346999.00 |
| CO2 Emissions (Tonnes) |   2019 |   68211.00 |
| CO2 Emissions (Tonnes) |   2020 |  288460.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |      Value |
|:--------------------|-------:|-----------:|
| Annual Output (MWh) |   2016 | 2155750.67 |
| Annual Output (MWh) |   2017 | 2465171.00 |
| Annual Output (MWh) |   2018 |  921114.37 |
| Annual Output (MWh) |   2019 |  184489.40 |
| Annual Output (MWh) |   2020 |  740140.04 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | CCGT    |

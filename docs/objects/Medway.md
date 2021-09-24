### Identifiers

| Relationship   | ID Type              | ID(s)            |
|:---------------|:---------------------|:-----------------|
| Root           | OSUKED ID            | 10046            |
| Related        | Settlement BMU ID    | T_MEDP-1         |
| Related        | National Grid BMU ID | MEDP-1           |
| Equivalent     | GPPD ID              | GBR1000437       |
| Equivalent     | ESAIL ID             | MEDP             |
| Equivalent     | Common Name          | Medway           |
| Equivalent     | EUTL ID              | 98257            |
| Equivalent     | EIC ID               | 48W000000MEDP-12 |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | CCGT    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    0.89 |
| Latitude    |   51.38 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 700.0                                                                          |
| Longitude                           | 0.6894                                                                         |
| Latitude                            | 51.4396                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | Scottish and Southern: Thermal                                                 |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| PLATTS-WEPP ID                      | 1022461.0                                                                      |
| Estimated Annual Generation in 2017 | 3248.04                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 1548481.00 |
| CO2 Emissions (Tonnes) |   2006 | 1329097.00 |
| CO2 Emissions (Tonnes) |   2007 | 1705103.00 |
| CO2 Emissions (Tonnes) |   2008 |  727064.00 |
| CO2 Emissions (Tonnes) |   2009 |  888589.00 |
| CO2 Emissions (Tonnes) |   2010 | 1474299.00 |
| CO2 Emissions (Tonnes) |   2011 | 1403577.00 |
| CO2 Emissions (Tonnes) |   2012 |   20998.00 |
| CO2 Emissions (Tonnes) |   2013 |  274013.00 |
| CO2 Emissions (Tonnes) |   2014 |  570229.00 |
| CO2 Emissions (Tonnes) |   2015 |  591014.00 |
| CO2 Emissions (Tonnes) |   2016 |  927881.00 |
| CO2 Emissions (Tonnes) |   2017 |  951590.00 |
| CO2 Emissions (Tonnes) |   2018 |  619337.00 |
| CO2 Emissions (Tonnes) |   2019 |  680587.00 |
| CO2 Emissions (Tonnes) |   2020 |  809312.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |      Value |
|:--------------------|-------:|-----------:|
| Annual Output (MWh) |   2016 | 2393667.56 |
| Annual Output (MWh) |   2017 | 2381409.96 |
| Annual Output (MWh) |   2018 | 1457296.64 |
| Annual Output (MWh) |   2019 | 1698224.21 |
| Annual Output (MWh) |   2020 | 2001115.21 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   40.87 |
| Capture Price (£/MWh) |   2017 |   49.08 |
| Capture Price (£/MWh) |   2018 |   62.03 |
| Capture Price (£/MWh) |   2019 |   47.06 |
| Capture Price (£/MWh) |   2020 |   36.82 |

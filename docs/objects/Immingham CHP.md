### Identifiers

| Relationship   | ID Type              | ID(s)            |
|:---------------|:---------------------|:-----------------|
| Root           | OSUKED ID            | 10070            |
| Related        | Settlement BMU ID    | T_HUMR-1         |
| Related        | National Grid BMU ID | HUMR-1           |
| Equivalent     | GPPD ID              | GBR1000517       |
| Equivalent     | ESAIL ID             | HUMR             |
| Equivalent     | Common Name          | Immingham CHP    |
| Equivalent     | EUTL ID              | 96880            |
| Equivalent     | EIC ID               | 48W100000HUMR-1N |

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
| Longitude   |    0.00 |
| Latitude    |   53.69 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute               | Value                                                                          |
|:------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW) | 1240.0                                                                         |
| Longitude               | -0.2395                                                                        |
| Latitude                | 53.6366                                                                        |
| Primary Fuel Type       | Cogeneration                                                                   |
| Owner                   | VPI Immingham LLP                                                              |
| Source                  | Department for Business Energy & Industrial Strategy                           |
| URL                     | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source      | CARMA                                                                          |
| PLATTS-WEPP ID          | 1052905.0                                                                      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 2030737.00 |
| CO2 Emissions (Tonnes) |   2006 | 2143213.00 |
| CO2 Emissions (Tonnes) |   2007 | 2146205.00 |
| CO2 Emissions (Tonnes) |   2008 | 2073563.00 |
| CO2 Emissions (Tonnes) |   2009 | 2928585.00 |
| CO2 Emissions (Tonnes) |   2010 | 3136936.00 |
| CO2 Emissions (Tonnes) |   2011 | 3238329.00 |
| CO2 Emissions (Tonnes) |   2012 | 2709905.00 |
| CO2 Emissions (Tonnes) |   2013 | 2199240.00 |
| CO2 Emissions (Tonnes) |   2014 | 2544552.00 |
| CO2 Emissions (Tonnes) |   2015 | 2989934.00 |
| CO2 Emissions (Tonnes) |   2016 | 3435305.00 |
| CO2 Emissions (Tonnes) |   2017 | 3110900.00 |
| CO2 Emissions (Tonnes) |   2018 | 3371537.00 |
| CO2 Emissions (Tonnes) |   2019 | 3361712.00 |
| CO2 Emissions (Tonnes) |   2020 | 3237057.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |      Value |
|:--------------------|-------:|-----------:|
| Annual Output (MWh) |   2016 | 7721634.80 |
| Annual Output (MWh) |   2017 | 6761155.15 |
| Annual Output (MWh) |   2018 | 7288425.48 |
| Annual Output (MWh) |   2019 | 7627097.97 |
| Annual Output (MWh) |   2020 | 7237835.54 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   40.70 |
| Capture Price (£/MWh) |   2017 |   46.96 |
| Capture Price (£/MWh) |   2018 |   58.52 |
| Capture Price (£/MWh) |   2019 |   43.85 |
| Capture Price (£/MWh) |   2020 |   36.89 |

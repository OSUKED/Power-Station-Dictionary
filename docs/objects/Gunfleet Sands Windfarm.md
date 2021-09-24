### Identifiers

| Relationship   | ID Type              | ID(s)                                                                  |
|:---------------|:---------------------|:-----------------------------------------------------------------------|
| Root           | OSUKED ID            | 10204                                                                  |
| Related        | GPPD ID              | GBR0002490, GBR0002489, GBR0002488                                     |
| Related        | Settlement BMU ID    | E_GNFSW-1, T_GNFSW-1, E_GNFSW-2, T_GNFSW-2, E_GNFSW-3                  |
| Related        | National Grid BMU ID | GNFSW-1, GNFSW-1, GNFSW-2, GNFSW-2                                     |
| Related        | EIC ID               | 48W00000GNFSW-1H, 48W00000GNFSW-1H, 48W00000GNFSW-2F, 48W00000GNFSW-2F |
| Equivalent     | ESAIL ID             | GNFSW                                                                  |
| Equivalent     | Common Name          | Gunfleet Sands Windfarm                                                |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | GNFSW-1   | GNFSW-2   |
|:------------|:----------|:----------|
| Fuel Type   | WIND      | WIND      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    1.17 |
| Latitude    |   51.74 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 80.0     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | GBR0002488                                                               | GBR0002489                                                               | GBR0002490                                                               |
|:------------------------------------|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------|
| Estimated Annual Generation in 2017 | 30.25                                                                    | 163.86                                                                   | 272.26                                                                   |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    | UK Renewable Energy Planning Database                                    | UK Renewable Energy Planning Database                                    |
| Installed Capacity (MW)             | 12.0                                                                     | 65.0                                                                     | 108.0                                                                    |
| Latitude                            | 51.703                                                                   | 51.7272                                                                  | 51.7308                                                                  |
| Longitude                           | 1.1919                                                                   | 1.2459                                                                   | 1.218                                                                    |
| Owner                               | Orsted (formerly Dong Energy)                                            | Orsted (formerly Dong Energy)                                            | Orsted (formerly Dong Energy)                                            |
| PLATTS-WEPP ID                      | 1038553.0                                                                | NaN                                                                      | 1038553.0                                                                |
| Primary Fuel Type                   | Wind                                                                     | Wind                                                                     | Wind                                                                     |
| Source                              | UK Renewable Energy Planning Database                                    | UK Renewable Energy Planning Database                                    | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data | https://www.gov.uk/government/collections/renewable-energy-planning-data | https://www.gov.uk/government/collections/renewable-energy-planning-data |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   GNFSW-1 |   GNFSW-2 |
|:--------------------|-------:|----------:|----------:|
| Annual Output (MWh) |   2016 |  96991.69 |  63185.03 |
| Annual Output (MWh) |   2017 | 324190.03 | 202595.15 |
| Annual Output (MWh) |   2018 | 316336.28 | 205092.98 |
| Annual Output (MWh) |   2019 | 314996.21 | 200895.06 |
| Annual Output (MWh) |   2020 | 366748.71 | 230090.53 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   GNFSW-1 |   GNFSW-2 |
|:----------------------|-------:|----------:|----------:|
| Capture Price (£/MWh) |   2016 |     45.47 |     45.86 |
| Capture Price (£/MWh) |   2017 |     44.28 |     44.30 |
| Capture Price (£/MWh) |   2018 |     56.58 |     56.42 |
| Capture Price (£/MWh) |   2019 |     40.78 |     40.86 |
| Capture Price (£/MWh) |   2020 |     30.78 |     30.80 |

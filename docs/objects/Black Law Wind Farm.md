### Identifiers

| Relationship   | ID Type     | ID(s)                  |
|:---------------|:------------|:-----------------------|
| root           | osuked_id   | 10163                  |
| element-of     | gppd_idnr   | GBR0003116, GBR0004253 |
| element-of     | sett_bmu_id | T_BLLA-1, T_BLLA-2     |
| element-of     | ngc_bmu_id  | BLLA-1, BLLA-2         |
| same-as        | esail_id    | BLLA                   |
| same-as        | name        | Black Law Wind Farm    |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.48 |
| Latitude    |   55.59 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Plant Type  | onshore |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | GBR0003116                                                               | GBR0004253                                                               |
|:------------------------------------|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------|
| Estimated Annual Generation in 2017 | 313.1                                                                    | 139.71                                                                   |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    | UK Renewable Energy Planning Database                                    |
| Installed Capacity (MW)             | 124.2                                                                    | 55.42                                                                    |
| Latitude                            | 55.7622                                                                  | 55.7622                                                                  |
| Longitude                           | -3.7626                                                                  | -3.7626                                                                  |
| Owner                               | Scottish Power Renewables                                                | Scottish Power Renewables                                                |
| PLATTS-WEPP ID                      | 1051674.0                                                                | 1051674.0                                                                |
| Primary Fuel Type                   | Wind                                                                     | Wind                                                                     |
| Source                              | UK Renewable Energy Planning Database                                    | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data | https://www.gov.uk/government/collections/renewable-energy-planning-data |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    BLLA-1 |    BLLA-2 |
|:--------------------|-------:|----------:|----------:|
| Annual Output (MWh) |   2016 | 157880.01 |      0.00 |
| Annual Output (MWh) |   2017 | 144279.07 |      0.00 |
| Annual Output (MWh) |   2018 | 144087.87 |      0.00 |
| Annual Output (MWh) |   2019 | 177925.36 | 112989.04 |
| Annual Output (MWh) |   2020 | 156338.88 | 113895.20 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | BLLA-1   | BLLA-2   |
|:------------|:---------|:---------|
| Fuel Type   | WIND     | WIND     |

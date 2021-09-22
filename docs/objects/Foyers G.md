### Identifiers

| Relationship   | ID Type     | ID(s)              |
|:---------------|:------------|:-------------------|
| root           | osuked_id   | 10146              |
| element-of     | sett_bmu_id | T_FOYE-1, T_FOYE-2 |
| element-of     | ngc_bmu_id  | FOYE-1, FOYE-2     |
| same-as        | gppd_idnr   | GBR2000657         |
| same-as        | esail_id    | FOYE               |
| same-as        | name        | Foyers G           |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -4.36 |
| Latitude    |   57.24 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value   |
|:------------------------------------|:--------|
| Installed Capacity (MW)             | 300.0   |
| Longitude                           | -4.4835 |
| Latitude                            | 57.2618 |
| Primary Fuel Type                   | Hydro   |
| Geolocation Source                  | GEO     |
| Estimated Annual Generation in 2013 | 641.53  |
| Estimated Annual Generation in 2014 | 533.18  |
| Estimated Annual Generation in 2015 | 1099.11 |
| Estimated Annual Generation in 2016 | 538.5   |
| Estimated Annual Generation in 2017 | 659.86  |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    FOYE-1 |    FOYE-2 |
|:--------------------|-------:|----------:|----------:|
| Annual Output (MWh) |   2016 | 117047.20 | 113004.75 |
| Annual Output (MWh) |   2017 | 145254.50 | 122335.15 |
| Annual Output (MWh) |   2018 | 126654.35 | 101084.00 |
| Annual Output (MWh) |   2019 | 122683.25 |  80375.95 |
| Annual Output (MWh) |   2020 |  61029.35 | 104882.20 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | FOYE-1   | FOYE-2   |
|:------------|:---------|:---------|
| Fuel Type   | PS       | PS       |

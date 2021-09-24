### Identifiers

| Relationship   | ID Type              | ID(s)                              |
|:---------------|:---------------------|:-----------------------------------|
| Root           | OSUKED ID            | 10146                              |
| Related        | Settlement BMU ID    | T_FOYE-1, T_FOYE-2                 |
| Related        | National Grid BMU ID | FOYE-1, FOYE-2                     |
| Related        | EIC ID               | 48W000000FOYE-14, 48W000000FOYE-22 |
| Equivalent     | GPPD ID              | GBR2000657                         |
| Equivalent     | ESAIL ID             | FOYE                               |
| Equivalent     | Common Name          | Foyers G                           |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | FOYE-1   | FOYE-2   |
|:------------|:---------|:---------|
| Fuel Type   | PS       | PS       |

<br><br>
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
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   FOYE-1 |   FOYE-2 |
|:----------------------|-------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    60.54 |    61.38 |
| Capture Price (£/MWh) |   2017 |    58.93 |    59.28 |
| Capture Price (£/MWh) |   2018 |    70.77 |    69.87 |
| Capture Price (£/MWh) |   2019 |    50.59 |    52.88 |
| Capture Price (£/MWh) |   2020 |    56.65 |    46.74 |

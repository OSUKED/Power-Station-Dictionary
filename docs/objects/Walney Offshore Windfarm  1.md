### Identifiers

| Relationship   | ID Type              | ID(s)                                                                  |
|:---------------|:---------------------|:-----------------------------------------------------------------------|
| Root           | OSUKED ID            | 10246                                                                  |
| Related        | GPPD ID              | GBR0002500, GBR0002506                                                 |
| Related        | Settlement BMU ID    | T_WLNYW-1, E_WLNYW-2, T_WLNYO-3, T_WLNYO-4, T_WLNYO-2                  |
| Related        | National Grid BMU ID | WLNYW-1, WLNYW-2, WLNYO-3, WLNYO-4, WLNYO-2                            |
| Related        | EIC ID               | 48W00000WLNYW-1A, 48W00000WLNYO-31, 48W00000WLNYO-4-, 48W00000WLNYO-23 |
| Related        | CfD ID               | INV-WAL-001, INV-WAL-002                                               |
| Equivalent     | ESAIL ID             | WLNYW1                                                                 |
| Equivalent     | Common Name          | Walney Offshore Windfarm  1                                            |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | WLNYO-2   | WLNYO-3   | WLNYO-4   | WLNYW-1   |
|:------------|:----------|:----------|:----------|:----------|
| Fuel Type   | WIND      | WIND      | WIND      | WIND      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.52 |
| Latitude    |   54.04 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 88.0     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | GBR0002500                                                               | GBR0002506                                                               |
|:------------------------------------|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------|
| Estimated Annual Generation in 2017 | 463.85                                                                   | 463.85                                                                   |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    | UK Renewable Energy Planning Database                                    |
| Installed Capacity (MW)             | 184.0                                                                    | 184.0                                                                    |
| Latitude                            | 54.0394                                                                  | 54.0807                                                                  |
| Longitude                           | -3.5158                                                                  | -3.609                                                                   |
| Owner                               | Orsted (formerly Dong Energy)                                            | Orsted (formerly Dong Energy)                                            |
| Primary Fuel Type                   | Wind                                                                     | Wind                                                                     |
| Source                              | UK Renewable Energy Planning Database                                    | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data | https://www.gov.uk/government/collections/renewable-energy-planning-data |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   WLNYO-2 |    WLNYO-3 |    WLNYO-4 |   WLNYW-1 |
|:--------------------|-------:|----------:|-----------:|-----------:|----------:|
| Annual Output (MWh) |   2016 | 510281.75 |       0.00 |       0.00 | 606021.37 |
| Annual Output (MWh) |   2017 | 799073.79 |  161692.17 |       0.03 | 700749.33 |
| Annual Output (MWh) |   2018 | 719934.15 | 1243740.00 |  893251.37 | 608583.25 |
| Annual Output (MWh) |   2019 | 762832.71 | 1394601.69 | 1312203.78 | 623769.78 |
| Annual Output (MWh) |   2020 | 754188.00 | 1427744.22 | 1090859.32 | 664786.54 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   WLNYO-2 |   WLNYO-3 |   WLNYO-4 |   WLNYW-1 |
|:----------------------|-------:|----------:|----------:|----------:|----------:|
| Capture Price (£/MWh) |   2016 |     38.52 |    nan    |    nan    |     36.05 |
| Capture Price (£/MWh) |   2017 |     43.90 |     51.80 |     53.94 |     43.68 |
| Capture Price (£/MWh) |   2018 |     56.39 |     56.30 |     56.45 |     55.94 |
| Capture Price (£/MWh) |   2019 |     39.70 |     39.91 |     39.48 |     39.38 |
| Capture Price (£/MWh) |   2020 |     31.03 |     31.73 |     30.77 |     30.64 |

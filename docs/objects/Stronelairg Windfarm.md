### Identifiers

| Relationship   | ID Type              | ID(s)                                                |
|:---------------|:---------------------|:-----------------------------------------------------|
| Root           | OSUKED ID            | 10284                                                |
| Related        | Settlement BMU ID    | T_STLGW-1, T_STLGW-2, T_STLGW-3                      |
| Related        | National Grid BMU ID | STLGW-1, STLGW-2, STLGW-3                            |
| Related        | EIC ID               | 48W00000STLGW-1E, 48W00000STLGW-2C, 48W00000STLGW-3A |
| Equivalent     | ESAIL ID             | STLGW                                                |
| Equivalent     | Common Name          | Stronelairg Windfarm                                 |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | STLGW-1   | STLGW-2   | STLGW-3   |
|:------------|:----------|:----------|:----------|
| Fuel Type   | WIND      | WIND      | WIND      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -4.46 |
| Latitude    |   57.10 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Plant Type  | onshore |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   STLGW-1 |   STLGW-2 |   STLGW-3 |
|:--------------------|-------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2017 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2018 | 102275.17 | 133101.72 |  56571.37 |
| Annual Output (MWh) |   2019 | 183012.61 | 214292.86 | 191655.30 |
| Annual Output (MWh) |   2020 | 139656.07 | 158080.54 | 138744.35 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   STLGW-1 |   STLGW-2 |   STLGW-3 |
|:----------------------|-------:|----------:|----------:|----------:|
| Capture Price (£/MWh) |   2018 |     58.17 |     59.95 |     59.83 |
| Capture Price (£/MWh) |   2019 |     42.38 |     42.44 |     42.34 |
| Capture Price (£/MWh) |   2020 |     33.01 |     33.60 |     33.17 |

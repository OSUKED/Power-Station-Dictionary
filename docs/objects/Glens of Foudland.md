### Identifiers

| Relationship   | ID Type              | ID(s)             |
|:---------------|:---------------------|:------------------|
| Root           | OSUKED ID            | 10197             |
| Related        | Settlement BMU ID    | E_GLOFW-1         |
| Related        | National Grid BMU ID | GLOFW-1           |
| Equivalent     | ESAIL ID             | GLOFW             |
| Equivalent     | Common Name          | Glens of Foudland |
| Equivalent     | EIC ID               | 48W00000GLOFW-15  |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | WIND    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -2.88 |
| Latitude    |   57.22 |

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

| Attribute           |   Year |    Value |
|:--------------------|-------:|---------:|
| Annual Output (MWh) |   2016 | 48232.29 |
| Annual Output (MWh) |   2017 | 55740.15 |
| Annual Output (MWh) |   2018 | 52664.20 |
| Annual Output (MWh) |   2019 | 52532.15 |
| Annual Output (MWh) |   2020 | 54318.17 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   36.09 |
| Capture Price (£/MWh) |   2017 |   44.22 |
| Capture Price (£/MWh) |   2018 |   55.92 |
| Capture Price (£/MWh) |   2019 |   40.09 |
| Capture Price (£/MWh) |   2020 |   31.98 |

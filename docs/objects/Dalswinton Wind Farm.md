### Identifiers

| Relationship   | ID Type              | ID(s)                |
|:---------------|:---------------------|:---------------------|
| Root           | OSUKED ID            | 10183                |
| Related        | Settlement BMU ID    | E_DALSW-1            |
| Related        | National Grid BMU ID | DALSW-1              |
| Equivalent     | ESAIL ID             | DALSW                |
| Equivalent     | Common Name          | Dalswinton Wind Farm |
| Equivalent     | EIC ID               | 48W00000DALSW-1M     |

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
| Longitude   |   -3.66 |
| Latitude    |   55.18 |

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
| Annual Output (MWh) |   2016 | 53997.00 |
| Annual Output (MWh) |   2017 | 58985.62 |
| Annual Output (MWh) |   2018 | 56702.33 |
| Annual Output (MWh) |   2019 | 57418.80 |
| Annual Output (MWh) |   2020 | 55791.40 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   36.22 |
| Capture Price (£/MWh) |   2017 |   42.99 |
| Capture Price (£/MWh) |   2018 |   57.17 |
| Capture Price (£/MWh) |   2019 |   39.54 |
| Capture Price (£/MWh) |   2020 |   31.26 |

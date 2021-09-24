### Identifiers

| Relationship   | ID Type              | ID(s)                   |
|:---------------|:---------------------|:------------------------|
| Root           | OSUKED ID            | 10198                   |
| Related        | Settlement BMU ID    | E_GFLDW-1               |
| Related        | National Grid BMU ID | GFLDW-1                 |
| Equivalent     | ESAIL ID             | GFLDW                   |
| Equivalent     | Common Name          | Goole Fields 1 Windfarm |
| Equivalent     | EIC ID               | 48W00000GFLDW-11        |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.87 |
| Latitude    |   53.67 |

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
| Annual Output (MWh) |   2016 | 80075.09 |
| Annual Output (MWh) |   2017 | 81619.86 |
| Annual Output (MWh) |   2018 | 80559.51 |
| Annual Output (MWh) |   2019 | 74774.50 |
| Annual Output (MWh) |   2020 | 85038.55 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   35.70 |
| Capture Price (£/MWh) |   2017 |   43.49 |
| Capture Price (£/MWh) |   2018 |   55.96 |
| Capture Price (£/MWh) |   2019 |   39.85 |
| Capture Price (£/MWh) |   2020 |   30.04 |

### Identifiers

| Relationship   | ID Type              | ID(s)                                                                  |
|:---------------|:---------------------|:-----------------------------------------------------------------------|
| Root           | OSUKED ID            | 10139                                                                  |
| Related        | Settlement BMU ID    | T_WYLF-1, T_WYLF-2, T_WYLF-3, T_WYLF-4                                 |
| Related        | National Grid BMU ID | WYLF-1, WYLF-2, WYLF-3, WYLF-4                                         |
| Related        | EIC ID               | 48W000000WYLF-1Y, 48W000000WYLF-2W, 48W000000WYLF-3U, 48W000000WYLF-4S |
| Equivalent     | ESAIL ID             | WYLF                                                                   |
| Equivalent     | Common Name          | Wylfa                                                                  |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -4.41 |
| Latitude    |   53.37 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   WYLF-1 |   WYLF-2 |   WYLF-3 |   WYLF-4 |
|:--------------------|-------:|---------:|---------:|---------:|---------:|
| Annual Output (MWh) |   2016 |     0.00 |     0.00 |     0.00 |     0.00 |
| Annual Output (MWh) |   2017 |     0.00 |     0.00 |     0.00 |     0.00 |
| Annual Output (MWh) |   2018 |     0.00 |     0.00 |     9.11 |    25.37 |
| Annual Output (MWh) |   2019 |    13.80 |    16.18 |     0.00 |     0.00 |
| Annual Output (MWh) |   2020 |     0.00 |     0.00 |     0.00 |     0.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   WYLF-1 |   WYLF-2 |   WYLF-3 |   WYLF-4 |
|:----------------------|-------:|---------:|---------:|---------:|---------:|
| Capture Price (£/MWh) |   2018 |   nan    |   nan    |    69.59 |    90.94 |
| Capture Price (£/MWh) |   2019 |    49.44 |    63.24 |   nan    |   nan    |

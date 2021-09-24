### Identifiers

| Relationship   | ID Type              | ID(s)            |
|:---------------|:---------------------|:-----------------|
| Root           | OSUKED ID            | 10083            |
| Related        | Settlement BMU ID    | E_FDUN-1         |
| Related        | National Grid BMU ID | FDUNT-1          |
| Equivalent     | ESAIL ID             | FDUN             |
| Equivalent     | Common Name          | Fort Dunlop      |
| Equivalent     | EIC ID               | 48W00000FDUNT-15 |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -1.35 |
| Latitude    |   50.83 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    Value |
|:--------------------|-------:|---------:|
| Annual Output (MWh) |   2016 | 19641.65 |
| Annual Output (MWh) |   2017 | 17489.06 |
| Annual Output (MWh) |   2018 | 10130.94 |
| Annual Output (MWh) |   2019 |  4418.40 |
| Annual Output (MWh) |   2020 | 18233.80 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   86.59 |
| Capture Price (£/MWh) |   2017 |   66.79 |
| Capture Price (£/MWh) |   2018 |   78.19 |
| Capture Price (£/MWh) |   2019 |   60.43 |
| Capture Price (£/MWh) |   2020 |   58.37 |

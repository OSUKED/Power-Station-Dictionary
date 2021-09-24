### Identifiers

| Relationship   | ID Type              | ID(s)            |
|:---------------|:---------------------|:-----------------|
| Root           | OSUKED ID            | 10117            |
| Related        | Settlement BMU ID    | T_FINL-1         |
| Related        | National Grid BMU ID | FINL-1           |
| Equivalent     | ESAIL ID             | FINL             |
| Equivalent     | Common Name          | Finlarig         |
| Equivalent     | EIC ID               | 48W000000FINL-1U |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | NPSHYD  |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.61 |
| Latitude    |   56.28 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    Value |
|:--------------------|-------:|---------:|
| Annual Output (MWh) |   2016 | 69561.09 |
| Annual Output (MWh) |   2017 | 72695.28 |
| Annual Output (MWh) |   2018 | 72531.88 |
| Annual Output (MWh) |   2019 | 73329.19 |
| Annual Output (MWh) |   2020 | 90026.80 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   42.90 |
| Capture Price (£/MWh) |   2017 |   48.27 |
| Capture Price (£/MWh) |   2018 |   60.54 |
| Capture Price (£/MWh) |   2019 |   43.58 |
| Capture Price (£/MWh) |   2020 |   36.92 |

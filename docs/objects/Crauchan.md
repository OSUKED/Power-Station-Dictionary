### Identifiers

| Relationship   | ID Type              | ID(s)                                                                  |
|:---------------|:---------------------|:-----------------------------------------------------------------------|
| Root           | OSUKED ID            | 10143                                                                  |
| Related        | Settlement BMU ID    | T_CRUA-1, T_CRUA-2, T_CRUA-3, T_CRUA-4                                 |
| Related        | National Grid BMU ID | CRUA-1, CRUA-2, CRUA-3, CRUA-4                                         |
| Related        | EIC ID               | 48W000000CRUA-16, 48W000000CRUA-24, 48W000000CRUA-32, 48W000000CRUA-40 |
| Equivalent     | ESAIL ID             | CRUA                                                                   |
| Equivalent     | Common Name          | Crauchan                                                               |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | CRUA-1   | CRUA-2   | CRUA-3   | CRUA-4   |
|:------------|:---------|:---------|:---------|:---------|
| Fuel Type   | PS       | PS       | PS       | PS       |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -5.22 |
| Latitude    |   56.37 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    CRUA-1 |    CRUA-2 |   CRUA-3 |   CRUA-4 |
|:--------------------|-------:|----------:|----------:|---------:|---------:|
| Annual Output (MWh) |   2016 |  94772.20 | 129230.96 | 22636.54 | 24691.62 |
| Annual Output (MWh) |   2017 |  95151.14 |  96342.94 | 30147.40 | 34270.94 |
| Annual Output (MWh) |   2018 | 114202.20 |  74677.38 |  9183.86 | 33938.50 |
| Annual Output (MWh) |   2019 |  94098.06 |  73404.10 | 25189.48 | 44980.04 |
| Annual Output (MWh) |   2020 | 114757.34 |  89555.32 | 21139.44 | 45380.08 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   CRUA-1 |   CRUA-2 |   CRUA-3 |   CRUA-4 |
|:----------------------|-------:|---------:|---------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    60.61 |    50.22 |    81.30 |    48.47 |
| Capture Price (£/MWh) |   2017 |    57.32 |    56.51 |    65.36 |    58.17 |
| Capture Price (£/MWh) |   2018 |    69.19 |    72.89 |    69.91 |    68.99 |
| Capture Price (£/MWh) |   2019 |    51.78 |    52.17 |    52.07 |    53.60 |
| Capture Price (£/MWh) |   2020 |    46.79 |    48.69 |    50.32 |    55.11 |

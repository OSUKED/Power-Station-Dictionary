### Identifiers

| Relationship   | ID Type              | ID(s)                                                |
|:---------------|:---------------------|:-----------------------------------------------------|
| Root           | OSUKED ID            | 10115                                                |
| Related        | Settlement BMU ID    | T_ERRO-1, T_ERRO-2, T_ERRO-3                         |
| Related        | National Grid BMU ID | ERRO-1, ERRO-2, ERRO-3                               |
| Related        | EIC ID               | 48W000000ERRO-1P, 48W000000ERRO-2N, 48W000000ERRO-3L |
| Equivalent     | ESAIL ID             | ERRO                                                 |
| Equivalent     | Common Name          | Errochty G                                           |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | ERRO-1   | ERRO-2   | ERRO-3   |
|:------------|:---------|:---------|:---------|
| Fuel Type   | NPSHYD   | NPSHYD   | NPSHYD   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.79 |
| Latitude    |   56.73 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   ERRO-1 |   ERRO-2 |   ERRO-3 |
|:--------------------|-------:|---------:|---------:|---------:|
| Annual Output (MWh) |   2016 | 32304.97 | 19178.85 | 41301.73 |
| Annual Output (MWh) |   2017 | 41242.56 |   881.61 | 39118.14 |
| Annual Output (MWh) |   2018 | 25336.81 | 16830.54 | 27133.03 |
| Annual Output (MWh) |   2019 | 32969.14 | 28239.16 | 34927.63 |
| Annual Output (MWh) |   2020 | 41495.31 | 41134.97 | 38918.45 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   ERRO-1 |   ERRO-2 |   ERRO-3 |
|:----------------------|-------:|---------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    54.71 |    51.69 |    52.04 |
| Capture Price (£/MWh) |   2017 |    54.60 |    68.45 |    54.10 |
| Capture Price (£/MWh) |   2018 |    70.34 |    73.97 |    70.33 |
| Capture Price (£/MWh) |   2019 |    48.90 |    48.38 |    48.23 |
| Capture Price (£/MWh) |   2020 |    44.37 |    45.06 |    45.68 |

### Identifiers

| Relationship   | ID Type              | ID(s)                |
|:---------------|:---------------------|:---------------------|
| Root           | OSUKED ID            | 10000                |
| Related        | Settlement BMU ID    | E_MARK-1, E_MARK-2   |
| Related        | National Grid BMU ID | MARK-1, MARK-2       |
| Equivalent     | ESAIL ID             | MARK                 |
| Equivalent     | Common Name          | Rothes Bio-Plant CHP |
| Equivalent     | EIC ID               | 48W000000MARK-1D     |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | BIOMASS |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.60 |
| Latitude    |   57.48 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     Value |
|:--------------------|-------:|----------:|
| Annual Output (MWh) |   2016 | 355704.93 |
| Annual Output (MWh) |   2017 | 387311.36 |
| Annual Output (MWh) |   2018 | 295847.59 |
| Annual Output (MWh) |   2019 | 389670.23 |
| Annual Output (MWh) |   2020 | 347661.62 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   39.60 |
| Capture Price (£/MWh) |   2017 |   45.39 |
| Capture Price (£/MWh) |   2018 |   56.83 |
| Capture Price (£/MWh) |   2019 |   42.17 |
| Capture Price (£/MWh) |   2020 |   34.83 |

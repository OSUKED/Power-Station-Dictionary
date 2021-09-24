### Identifiers

| Relationship   | ID Type              | ID(s)              |
|:---------------|:---------------------|:-------------------|
| Root           | OSUKED ID            | 10151              |
| Related        | Settlement BMU ID    | T_ANSUW-1          |
| Related        | National Grid BMU ID | ANSUW-1            |
| Equivalent     | ESAIL ID             | ANSUW              |
| Equivalent     | Common Name          | An Suidhe Windfarm |
| Equivalent     | EIC ID               | 48W00000ANSUW-1E   |

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
| Longitude   |   -5.45 |
| Latitude    |   56.07 |

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
| Annual Output (MWh) |   2016 | 31724.95 |
| Annual Output (MWh) |   2017 | 36265.97 |
| Annual Output (MWh) |   2018 | 45994.27 |
| Annual Output (MWh) |   2019 | 44266.80 |
| Annual Output (MWh) |   2020 | 51728.88 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   37.88 |
| Capture Price (£/MWh) |   2017 |   43.02 |
| Capture Price (£/MWh) |   2018 |   57.27 |
| Capture Price (£/MWh) |   2019 |   40.69 |
| Capture Price (£/MWh) |   2020 |   30.67 |

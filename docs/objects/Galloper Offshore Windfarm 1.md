### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                 |
|:---------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10194                                                                                                                 |
| Related        | Settlement BMU ID    | T_GANW-11, T_GANW-13, T_GANW-22, T_GANW-24                                                                            |
| Related        | National Grid BMU ID | GAOFO-1, GAOFO-3, GAOFO-2, GAOFO-4                                                                                    |
| Related        | EIC ID               | 48W00000GAOFO-13, 48W10000GAOFO-3N, 48W00000GAOFO-21, 48W00000GAOFO-4Y                                                |
| Equivalent     | ESAIL ID             | GANW                                                                                                                  |
| Equivalent     | Common Name          | Galloper Offshore Windfarm 1                                                                                          |
| Equivalent     | 4C-Offshore ID       | [galloper-united-kingdom-uk62](https://www.4coffshore.com/windfarms/united-kingdom/galloper-united-kingdom-uk62.html) |
| Equivalent     | WindPowerNet ID      | [windfarm_en_16770_galloper](https://www.thewindpower.net/windfarm_en_16770_galloper.php)                             |
| Equivalent     | Wikidata ID          | [Q56026054](https://www.wikidata.org/wiki/Q56026054)                                                                  |
| Equivalent     | Power-Technology ID  | [galloper-offshore-wind-farm](https://www.power-technology.com/projects/galloper-offshore-wind-farm)                  |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | GAOFO-1   | GAOFO-2   | GAOFO-3   | GAOFO-4   |
|:------------|:----------|:----------|:----------|:----------|
| Fuel Type   | WIND      | WIND      | WIND      | WIND      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    2.04 |
| Latitude    |   51.89 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 88.0     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   GAOFO-1 |   GAOFO-2 |   GAOFO-3 |   GAOFO-4 |
|:--------------------|-------:|----------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2017 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2018 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2019 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2020 | 124611.95 | 124803.32 | 123607.07 | 121803.71 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   GAOFO-1 |   GAOFO-2 |   GAOFO-3 |   GAOFO-4 |
|:----------------------|-------:|----------:|----------:|----------:|----------:|
| Capture Price (£/MWh) |   2020 |     41.10 |     41.24 |     41.43 |     41.56 |

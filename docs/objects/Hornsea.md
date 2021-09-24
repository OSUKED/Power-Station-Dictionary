### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:---------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10301                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Related        | Settlement BMU ID    | T_HOWAO-1, T_HOWAO-2, T_HOWAO-3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Related        | National Grid BMU ID | HOWAO-1, HOWAO-2, HOWAO-3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Related        | 4C-Offshore ID       | [hornsea-project-one-united-kingdom-uk81](https://www.4coffshore.com/windfarms/united-kingdom/hornsea-project-one-united-kingdom-uk81.html), [hornsea-project-two-united-kingdom-uk1u](https://www.4coffshore.com/windfarms/united-kingdom/hornsea-project-two-united-kingdom-uk1u.html), [hornsea-project-three-united-kingdom-uk1k](https://www.4coffshore.com/windfarms/united-kingdom/hornsea-project-three-united-kingdom-uk1k.html), [hornsea-project-four-united-kingdom-uk1j](https://www.4coffshore.com/windfarms/united-kingdom/hornsea-project-four-united-kingdom-uk1j.html) |
| Related        | WindPowerNet ID      | [windfarm_en_16677_hornsea-project-one-heron-wind](https://www.thewindpower.net/windfarm_en_16677_hornsea-project-one-heron-wind.php), [windfarm_en_16685_hornsea-project-three](https://www.thewindpower.net/windfarm_en_16685_hornsea-project-three.php)                                                                                                                                                                                                                                                                                                                               |
| Related        | EIC ID               | 48W00000HOWAO-1M, 48W00000HOWAO-2K, 48W00000HOWAO-3I                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Related        | CfD ID               | INV-HOR-001, INV-HOR-002, INV-HOR-003                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Equivalent     | Common Name          | Hornsea                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Equivalent     | Wikidata ID          | [Q23013079](https://www.wikidata.org/wiki/Q23013079)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Equivalent     | Wikipedia ID         | [Hornsea_Wind_Farm](https://en.wikipedia.org/wiki/Hornsea_Wind_Farm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Equivalent     | Power-Technology ID  | [hornsea-project-one-north-sea](https://www.power-technology.com/projects/hornsea-project-one-north-sea)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | HOWAO-1   | HOWAO-2   | HOWAO-3   |
|:------------|:----------|:----------|:----------|
| Fuel Type   | WIND      | WIND      | WIND      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    1.79 |
| Latitude    |   53.88 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 153.0    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    HOWAO-1 |    HOWAO-2 |    HOWAO-3 |
|:--------------------|-------:|-----------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 |       0.00 |       0.00 |       0.00 |
| Annual Output (MWh) |   2017 |       0.00 |       0.00 |       0.00 |
| Annual Output (MWh) |   2018 |       0.00 |       0.00 |       0.00 |
| Annual Output (MWh) |   2019 |  362072.33 | 1221985.93 |  747642.88 |
| Annual Output (MWh) |   2020 | 1752325.14 | 1808774.69 | 1562432.70 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   HOWAO-1 |   HOWAO-2 |   HOWAO-3 |
|:----------------------|-------:|----------:|----------:|----------:|
| Capture Price (£/MWh) |   2019 |     36.74 |     37.12 |     36.30 |
| Capture Price (£/MWh) |   2020 |     32.33 |     31.99 |     32.57 |

### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                               |
|:---------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10300                                                                                                                               |
| Related        | Settlement BMU ID    | T_EAAO-1, T_EAAO-2                                                                                                                  |
| Related        | National Grid BMU ID | EAAO-1, EAAO-2                                                                                                                      |
| Related        | EIC ID               | 48W000000EAAO-1R, 48W000000EAAO-2P                                                                                                  |
| Equivalent     | Common Name          | East Anglia One                                                                                                                     |
| Equivalent     | 4C-Offshore ID       | [east-anglia-one-united-kingdom-uk64](https://www.4coffshore.com/windfarms/united-kingdom/east-anglia-one-united-kingdom-uk64.html) |
| Equivalent     | WindPowerNet ID      | [windfarm_en_16790_east](https://www.thewindpower.net/windfarm_en_16790_east.php)                                                   |
| Equivalent     | Wikidata ID          | [Q19364853](https://www.wikidata.org/wiki/Q19364853)                                                                                |
| Equivalent     | Wikipedia ID         | [East_Anglia_Array](https://en.wikipedia.org/wiki/East_Anglia_Array)                                                                |
| Equivalent     | Power-Technology ID  | [east-anglia-one-offshore-wind-farm](https://www.power-technology.com/projects/east-anglia-one-offshore-wind-farm)                  |
| Equivalent     | CfD ID               | CAA-EAS-168                                                                                                                         |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | EAAO-1   | EAAO-2   |
|:------------|:---------|:---------|
| Fuel Type   | WIND     | WIND     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    2.50 |
| Latitude    |   52.23 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 120.0    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     EAAO-1 |    EAAO-2 |
|:--------------------|-------:|-----------:|----------:|
| Annual Output (MWh) |   2016 |       0.00 |      0.00 |
| Annual Output (MWh) |   2017 |       0.00 |      0.00 |
| Annual Output (MWh) |   2018 |       0.00 |      0.00 |
| Annual Output (MWh) |   2019 |  185800.09 |     31.62 |
| Annual Output (MWh) |   2020 | 1252092.42 | 949133.39 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   EAAO-1 |   EAAO-2 |
|:----------------------|-------:|---------:|---------:|
| Capture Price (£/MWh) |   2019 |    37.10 |    38.10 |
| Capture Price (£/MWh) |   2020 |    32.50 |    33.33 |

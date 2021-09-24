### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                               |
|:---------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10185                                                                                                               |
| Related        | Settlement BMU ID    | T_DDGNO-1, T_DDGNO-2, T_DDGNO-3, T_DDGNO-4                                                                          |
| Related        | National Grid BMU ID | DDGNO-1, DDGNO-2, DDGNO-3, DDGNO-4                                                                                  |
| Related        | EIC ID               | 48W00000DDGNO-1E, 48W00000DDGNO-2C, 48W00000DDGNO-3A, 48W00000DDGNO-48                                              |
| Related        | CfD ID               | INV-DUD-001, INV-DUD-002, INV-DUD-003                                                                               |
| Equivalent     | ESAIL ID             | DDGNO                                                                                                               |
| Equivalent     | Common Name          | Dudgeon Offshore Wind Farm Generator                                                                                |
| Equivalent     | 4C-Offshore ID       | [dudgeon-united-kingdom-uk04](https://www.4coffshore.com/windfarms/united-kingdom/dudgeon-united-kingdom-uk04.html) |
| Equivalent     | WindPowerNet ID      | [windfarm_en_12072_dudgeon](https://www.thewindpower.net/windfarm_en_12072_dudgeon.php)                             |
| Equivalent     | Wikidata ID          | [Q5311735](https://www.wikidata.org/wiki/Q5311735)                                                                  |
| Equivalent     | Wikipedia ID         | [Dudgeon_Offshore_Wind_Farm](https://en.wikipedia.org/wiki/Dudgeon_Offshore_Wind_Farm)                              |
| Equivalent     | Power-Technology ID  | [dudgeon-offshore-wind-farm](https://www.power-technology.com/projects/dudgeon-offshore-wind-farm)                  |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | DDGNO-1   | DDGNO-2   | DDGNO-3   | DDGNO-4   |
|:------------|:----------|:----------|:----------|:----------|
| Fuel Type   | WIND      | WIND      | WIND      | WIND      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |    1.39 |
| Latitude    |   53.25 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 110.0    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   DDGNO-1 |   DDGNO-2 |   DDGNO-3 |   DDGNO-4 |
|:--------------------|-------:|----------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2017 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2018 | 176743.81 | 172032.94 | 182301.18 | 185793.67 |
| Annual Output (MWh) |   2019 | 416007.83 | 366762.44 | 398173.59 | 417384.72 |
| Annual Output (MWh) |   2020 | 446123.36 | 398511.70 | 435760.64 | 442121.23 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   DDGNO-1 |   DDGNO-2 |   DDGNO-3 |   DDGNO-4 |
|:----------------------|-------:|----------:|----------:|----------:|----------:|
| Capture Price (£/MWh) |   2018 |     59.16 |     59.10 |     59.12 |     59.12 |
| Capture Price (£/MWh) |   2019 |     39.82 |     40.28 |     39.84 |     40.24 |
| Capture Price (£/MWh) |   2020 |     31.49 |     31.25 |     31.47 |     31.64 |

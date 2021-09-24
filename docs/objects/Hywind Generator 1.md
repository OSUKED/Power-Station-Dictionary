### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                                                     |
|:---------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10215                                                                                                                                                     |
| Related        | Settlement BMU ID    | E_HYWDW-1                                                                                                                                                 |
| Related        | National Grid BMU ID | HYWDW-1                                                                                                                                                   |
| Equivalent     | ESAIL ID             | HYWDW                                                                                                                                                     |
| Equivalent     | Common Name          | Hywind Generator 1                                                                                                                                        |
| Equivalent     | 4C-Offshore ID       | [hywind-scotland-pilot-park-united-kingdom-uk76](https://www.4coffshore.com/windfarms/united-kingdom/hywind-scotland-pilot-park-united-kingdom-uk76.html) |
| Equivalent     | WindPowerNet ID      | [windfarm_en_16758_hywind-scotland-pilot-park](https://www.thewindpower.net/windfarm_en_16758_hywind-scotland-pilot-park.php)                             |
| Equivalent     | Wikidata ID          | [Q6989526](https://www.wikidata.org/wiki/Q6989526)                                                                                                        |
| Equivalent     | Wikipedia ID         | [Hywind_Scotland](https://en.wikipedia.org/wiki/Hywind_Scotland)                                                                                          |
| Equivalent     | Power-Technology ID  | [hywind-pilot-park-aberdeenshire](https://www.power-technology.com/projects/hywind-pilot-park-aberdeenshire)                                              |
| Equivalent     | EIC ID               | 48W00000HYWDW-1G                                                                                                                                          |

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
| Longitude   |   -1.35 |
| Latitude    |   57.48 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 101.0    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     Value |
|:--------------------|-------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |
| Annual Output (MWh) |   2017 |      0.00 |
| Annual Output (MWh) |   2018 |  66547.45 |
| Annual Output (MWh) |   2019 | 145561.10 |
| Annual Output (MWh) |   2020 | 140133.59 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2018 |   60.03 |
| Capture Price (£/MWh) |   2019 |   40.53 |
| Capture Price (£/MWh) |   2020 |   33.18 |

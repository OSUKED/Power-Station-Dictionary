### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                                                                                                                                                                                                                                |
|:---------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10297                                                                                                                                                                                                                                                                                                                                |
| Related        | Settlement BMU ID    | T_BEATO-1, T_BEATO-2, T_BEATO-3, T_BEATO-4                                                                                                                                                                                                                                                                                           |
| Related        | National Grid BMU ID | BEATO-1, BEATO-2, BEATO-3, BEATO-4                                                                                                                                                                                                                                                                                                   |
| Related        | 4C-Offshore ID       | [united-kingdom/beatrice-demonstration-united-kingdom-uk46](https://www.4coffshore.com/windfarms/united-kingdom/united-kingdom/beatrice-demonstration-united-kingdom-uk46.html), [united-kingdom/beatrice-united-kingdom-uk53](https://www.4coffshore.com/windfarms/united-kingdom/united-kingdom/beatrice-united-kingdom-uk53.html) |
| Related        | WindPowerNet ID      | [windfarm_en_10664_beatrice-demonstration](https://www.thewindpower.net/windfarm_en_10664_beatrice-demonstration.php), [windfarm_en_12051_beatrice](https://www.thewindpower.net/windfarm_en_12051_beatrice.php)                                                                                                                     |
| Related        | EIC ID               | 48W00000BEATO-1T, 48W00000BEATO-2R, 48W00000BEATO-3P, 48W00000BEATO-4N                                                                                                                                                                                                                                                               |
| Related        | CfD ID               | INV-BEA-001, INV-BEA-002                                                                                                                                                                                                                                                                                                             |
| Equivalent     | Common Name          | Beatrice                                                                                                                                                                                                                                                                                                                             |
| Equivalent     | Wikidata ID          | [Q4877211](https://www.wikidata.org/wiki/Q4877211)                                                                                                                                                                                                                                                                                   |
| Equivalent     | Wikipedia ID         | [Beatrice_Wind_Farm](https://en.wikipedia.org/wiki/Beatrice_Wind_Farm)                                                                                                                                                                                                                                                               |
| Equivalent     | Power-Technology ID  | [beatrice-offshore-wind-farm](https://www.power-technology.com/projects/beatrice-offshore-wind-farm)                                                                                                                                                                                                                                 |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | BEATO-1   | BEATO-2   | BEATO-3   | BEATO-4   |
|:------------|:----------|:----------|:----------|:----------|
| Fuel Type   | WIND      | WIND      | WIND      | WIND      |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.07 |
| Latitude    |   58.13 |

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

| Attribute           |   Year |   BEATO-1 |   BEATO-2 |   BEATO-3 |   BEATO-4 |
|:--------------------|-------:|----------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2017 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2018 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2019 | 491797.60 | 499619.45 | 495000.97 | 582576.48 |
| Annual Output (MWh) |   2020 | 470829.79 | 522452.38 | 695097.69 | 676297.95 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   BEATO-1 |   BEATO-2 |   BEATO-3 |   BEATO-4 |
|:----------------------|-------:|----------:|----------:|----------:|----------:|
| Capture Price (£/MWh) |   2019 |     40.41 |     40.27 |     38.27 |     39.44 |
| Capture Price (£/MWh) |   2020 |     32.80 |     32.94 |     32.80 |     32.99 |

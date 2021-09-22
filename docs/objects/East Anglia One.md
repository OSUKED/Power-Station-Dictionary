### Identifiers

| Relationship   | ID Type             | ID(s)                               |
|:---------------|:--------------------|:------------------------------------|
| root           | osuked_id           | 10300                               |
| element-of     | sett_bmu_id         | T_EAAO-1, T_EAAO-2                  |
| element-of     | ngc_bmu_id          | EAAO-1, EAAO-2                      |
| same-as        | name                | East Anglia One                     |
| same-as        | 4c_offshore_id      | east-anglia-one-united-kingdom-uk64 |
| same-as        | windpowernet_id     | windfarm_en_16790_east              |
| same-as        | wikidata_id         | Q19364853                           |
| same-as        | wikipedia_id        | East_Anglia_Array                   |
| same-as        | power_technology_id | east-anglia-one-offshore-wind-farm  |

<br>
### Datasets
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
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | EAAO-1   | EAAO-2   |
|:------------|:---------|:---------|
| Fuel Type   | WIND     | WIND     |

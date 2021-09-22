### Identifiers

| Relationship   | ID Type     | ID(s)         |
|:---------------|:------------|:--------------|
| root           | osuked_id   | 10110         |
| element-of     | sett_bmu_id | M_CAS-CON01   |
| element-of     | ngc_bmu_id  | CAS-CON01     |
| same-as        | esail_id    | CASCON        |
| same-as        | name        | Conon Cascade |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -4.83 |
| Latitude    |   57.62 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     Value |
|:--------------------|-------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |
| Annual Output (MWh) |   2017 |      0.00 |
| Annual Output (MWh) |   2018 |      0.00 |
| Annual Output (MWh) |   2019 | 361446.54 |
| Annual Output (MWh) |   2020 | 436169.66 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | NPSHYD  |

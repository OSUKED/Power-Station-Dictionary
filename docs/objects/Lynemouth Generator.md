### Identifiers

| Relationship   | ID Type     | ID(s)                     |
|:---------------|:------------|:--------------------------|
| root           | osuked_id   | 10010                     |
| element-of     | sett_bmu_id | E_LYNE1, E_LYNE2, E_LYNE3 |
| element-of     | ngc_bmu_id  | LNMTH-1, LNMTH-2, LNMTH-3 |
| same-as        | esail_id    | LYNE                      |
| same-as        | name        | Lynemouth Generator       |
| same-as        | eutl_id     | 96827                     |

<br>
### Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -1.52 |
| Latitude    |   55.20 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 2685512.00 |
| CO2 Emissions (Tonnes) |   2006 | 2693932.00 |
| CO2 Emissions (Tonnes) |   2007 | 2695748.00 |
| CO2 Emissions (Tonnes) |   2008 | 2802040.00 |
| CO2 Emissions (Tonnes) |   2009 | 2543017.00 |
| CO2 Emissions (Tonnes) |   2010 | 2551364.00 |
| CO2 Emissions (Tonnes) |   2011 | 2612450.00 |
| CO2 Emissions (Tonnes) |   2012 | 2050363.00 |
| CO2 Emissions (Tonnes) |   2013 | 2284177.00 |
| CO2 Emissions (Tonnes) |   2014 | 2717964.00 |
| CO2 Emissions (Tonnes) |   2015 | 1287305.00 |
| CO2 Emissions (Tonnes) |   2016 |    1059.00 |
| CO2 Emissions (Tonnes) |   2017 |    2421.00 |
| CO2 Emissions (Tonnes) |   2018 |   44027.00 |
| CO2 Emissions (Tonnes) |   2019 |   13528.00 |
| CO2 Emissions (Tonnes) |   2020 |   10422.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   LNMTH-1 |   LNMTH-2 |   LNMTH-3 |
|:--------------------|-------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2017 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2018 | 515802.15 | 415919.47 | 343062.98 |
| Annual Output (MWh) |   2019 | 874149.46 | 778388.41 | 792208.59 |
| Annual Output (MWh) |   2020 | 905712.39 | 851145.27 | 868365.01 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | LNMTH-1   | LNMTH-2   | LNMTH-3   |
|:------------|:----------|:----------|:----------|
| Fuel Type   | BIOMASS   | BIOMASS   | BIOMASS   |

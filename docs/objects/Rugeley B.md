### Identifiers

| Relationship   | ID Type              | ID(s)                                                                  |
|:---------------|:---------------------|:-----------------------------------------------------------------------|
| Root           | OSUKED ID            | 10012                                                                  |
| Related        | Settlement BMU ID    | T_RUGPS-6, T_RUGPS-7, T_RUGGT-6, T_RUGGT-7                             |
| Related        | National Grid BMU ID | RUGPS-6, RUGPS-7, RUGGT-6, RUGGT-7                                     |
| Related        | EIC ID               | 48W00000RUGPS-66, 48W00000RUGPS-74, 48W00000RUGGT-6A, 48W00000RUGGT-78 |
| Equivalent     | ESAIL ID             | RUG                                                                    |
| Equivalent     | Common Name          | Rugeley B                                                              |
| Equivalent     | EUTL ID              | 97192                                                                  |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -1.94 |
| Latitude    |   52.73 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 4211713.00 |
| CO2 Emissions (Tonnes) |   2006 | 4063802.00 |
| CO2 Emissions (Tonnes) |   2007 | 4893162.00 |
| CO2 Emissions (Tonnes) |   2008 | 2732517.00 |
| CO2 Emissions (Tonnes) |   2009 | 4955403.00 |
| CO2 Emissions (Tonnes) |   2010 | 3673268.00 |
| CO2 Emissions (Tonnes) |   2011 | 4007947.00 |
| CO2 Emissions (Tonnes) |   2012 | 5017141.00 |
| CO2 Emissions (Tonnes) |   2013 | 6368144.00 |
| CO2 Emissions (Tonnes) |   2014 | 4644427.00 |
| CO2 Emissions (Tonnes) |   2015 | 3854947.00 |
| CO2 Emissions (Tonnes) |   2016 | 1184682.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |   RUGGT-6 |    RUGPS-6 |   RUGPS-7 |
|:--------------------|-------:|----------:|-----------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 | 1283048.06 |      0.00 |
| Annual Output (MWh) |   2017 |      0.00 |       0.00 |      0.00 |
| Annual Output (MWh) |   2018 |      0.00 |       0.00 |      0.00 |
| Annual Output (MWh) |   2019 |      0.00 |       0.00 |      0.00 |
| Annual Output (MWh) |   2020 |      0.00 |       0.00 |      2.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   RUGPS-6 |   RUGPS-7 |
|:----------------------|-------:|----------:|----------:|
| Capture Price (£/MWh) |   2016 |     33.65 |    nan    |
| Capture Price (£/MWh) |   2020 |    nan    |     23.58 |

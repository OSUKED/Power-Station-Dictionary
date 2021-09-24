### Identifiers

| Relationship   | ID Type              | ID(s)                                                                  |
|:---------------|:---------------------|:-----------------------------------------------------------------------|
| Root           | OSUKED ID            | 10009                                                                  |
| Related        | Settlement BMU ID    | T_LOAN-1, T_LOAN-2, T_LOAN-3, T_LOAN-4                                 |
| Related        | National Grid BMU ID | LOAN-1, LOAN-2, LOAN-3, LOAN-4                                         |
| Related        | EIC ID               | 48W000000LOAN-19, 48W000000LOAN-27, 48W000000LOAN-35, 48W000000LOAN-43 |
| Equivalent     | ESAIL ID             | LOAN                                                                   |
| Equivalent     | Common Name          | Longannet                                                              |
| Equivalent     | EUTL ID              | 96923                                                                  |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.44 |
| Latitude    |   56.05 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |       Value |
|:-----------------------|-------:|------------:|
| CO2 Emissions (Tonnes) |   2005 |  8417779.00 |
| CO2 Emissions (Tonnes) |   2006 | 10126655.00 |
| CO2 Emissions (Tonnes) |   2007 |  6685274.00 |
| CO2 Emissions (Tonnes) |   2008 |  5870515.00 |
| CO2 Emissions (Tonnes) |   2009 |  7301034.00 |
| CO2 Emissions (Tonnes) |   2010 |  9124587.00 |
| CO2 Emissions (Tonnes) |   2011 |  8500896.00 |
| CO2 Emissions (Tonnes) |   2012 |  9116373.00 |
| CO2 Emissions (Tonnes) |   2013 |  9513900.00 |
| CO2 Emissions (Tonnes) |   2014 |  9193891.00 |
| CO2 Emissions (Tonnes) |   2015 |  7457176.00 |
| CO2 Emissions (Tonnes) |   2016 |  1640190.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |    LOAN-1 |    LOAN-2 |    LOAN-3 |    LOAN-4 |
|:--------------------|-------:|----------:|----------:|----------:|----------:|
| Annual Output (MWh) |   2016 | 443125.05 | 477739.32 | 441068.27 | 405003.42 |
| Annual Output (MWh) |   2017 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2018 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2019 |      0.00 |      0.00 |      0.00 |      0.00 |
| Annual Output (MWh) |   2020 |      0.00 |      0.00 |      0.00 |      0.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   LOAN-1 |   LOAN-2 |   LOAN-3 |   LOAN-4 |
|:----------------------|-------:|---------:|---------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    35.42 |    35.81 |    36.13 |    35.38 |

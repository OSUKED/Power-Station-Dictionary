### Identifiers

| Relationship   | ID Type              | ID(s)                              |
|:---------------|:---------------------|:-----------------------------------|
| Root           | OSUKED ID            | 10039                              |
| Related        | Settlement BMU ID    | T_KEAD-1, T_KEADGT-3               |
| Related        | National Grid BMU ID | KEAD-1, KEADGT-3                   |
| Related        | EIC ID               | 48W000000KEAD-15, 48W0000KEADGT-3O |
| Equivalent     | ESAIL ID             | KEAD                               |
| Equivalent     | Common Name          | Keadby                             |
| Equivalent     | EUTL ID              | 98249                              |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | KEAD-1   | KEADGT-3   |
|:------------|:---------|:-----------|
| Fuel Type   | CCGT     | OCGT       |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -0.49 |
| Latitude    |   53.59 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 1343281.00 |
| CO2 Emissions (Tonnes) |   2006 | 1742317.00 |
| CO2 Emissions (Tonnes) |   2007 | 1889513.00 |
| CO2 Emissions (Tonnes) |   2008 | 2036332.00 |
| CO2 Emissions (Tonnes) |   2009 | 1484921.00 |
| CO2 Emissions (Tonnes) |   2010 | 1749851.00 |
| CO2 Emissions (Tonnes) |   2011 | 1232478.00 |
| CO2 Emissions (Tonnes) |   2012 |  156446.00 |
| CO2 Emissions (Tonnes) |   2013 |   24417.00 |
| CO2 Emissions (Tonnes) |   2014 |      51.00 |
| CO2 Emissions (Tonnes) |   2015 |   37691.00 |
| CO2 Emissions (Tonnes) |   2016 |  711016.00 |
| CO2 Emissions (Tonnes) |   2017 |  907295.00 |
| CO2 Emissions (Tonnes) |   2018 | 1026050.00 |
| CO2 Emissions (Tonnes) |   2019 |  803107.00 |
| CO2 Emissions (Tonnes) |   2020 |  812362.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     KEAD-1 |   KEADGT-3 |
|:--------------------|-------:|-----------:|-----------:|
| Annual Output (MWh) |   2016 | 1802320.70 |     176.56 |
| Annual Output (MWh) |   2017 | 2295282.46 |      25.30 |
| Annual Output (MWh) |   2018 | 2533349.33 |     156.79 |
| Annual Output (MWh) |   2019 | 2032228.85 |      79.00 |
| Annual Output (MWh) |   2020 | 2018198.08 |     415.40 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   KEAD-1 |   KEADGT-3 |
|:----------------------|-------:|---------:|-----------:|
| Capture Price (£/MWh) |   2016 |    47.88 |      42.73 |
| Capture Price (£/MWh) |   2017 |    51.16 |      90.72 |
| Capture Price (£/MWh) |   2018 |    59.25 |     126.92 |
| Capture Price (£/MWh) |   2019 |    47.68 |      61.33 |
| Capture Price (£/MWh) |   2020 |    33.88 |     155.26 |

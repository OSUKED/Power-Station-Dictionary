### Identifiers

| Relationship   | ID Type              | ID(s)               |
|:---------------|:---------------------|:--------------------|
| Root           | OSUKED ID            | 10068               |
| Related        | Settlement BMU ID    | T_GRMO-1            |
| Related        | National Grid BMU ID | GRMO-1              |
| Equivalent     | ESAIL ID             | GRMO                |
| Equivalent     | Common Name          | Grangemouth CHP Ltd |
| Equivalent     | EUTL ID              | 97781               |
| Equivalent     | EIC ID               | 48W100000GRMO-1N    |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | CCGT    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -3.03 |
| Latitude    |   55.93 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |     Value |
|:-----------------------|-------:|----------:|
| CO2 Emissions (Tonnes) |   2005 | 707518.00 |
| CO2 Emissions (Tonnes) |   2006 | 745367.00 |
| CO2 Emissions (Tonnes) |   2007 | 723444.00 |
| CO2 Emissions (Tonnes) |   2008 | 647323.00 |
| CO2 Emissions (Tonnes) |   2009 | 750986.00 |
| CO2 Emissions (Tonnes) |   2010 | 734634.00 |
| CO2 Emissions (Tonnes) |   2011 | 758345.00 |
| CO2 Emissions (Tonnes) |   2012 | 607818.00 |
| CO2 Emissions (Tonnes) |   2013 | 628783.00 |
| CO2 Emissions (Tonnes) |   2014 | 683941.00 |
| CO2 Emissions (Tonnes) |   2015 | 685030.00 |
| CO2 Emissions (Tonnes) |   2016 | 612225.00 |
| CO2 Emissions (Tonnes) |   2017 | 680626.00 |
| CO2 Emissions (Tonnes) |   2018 | 702044.00 |
| CO2 Emissions (Tonnes) |   2019 | 639861.00 |
| CO2 Emissions (Tonnes) |   2020 | 615331.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |      Value |
|:--------------------|-------:|-----------:|
| Annual Output (MWh) |   2016 |  919893.34 |
| Annual Output (MWh) |   2017 |  880434.66 |
| Annual Output (MWh) |   2018 | 1030475.11 |
| Annual Output (MWh) |   2019 |  969367.81 |
| Annual Output (MWh) |   2020 |  992358.31 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   38.72 |
| Capture Price (£/MWh) |   2017 |   45.31 |
| Capture Price (£/MWh) |   2018 |   56.36 |
| Capture Price (£/MWh) |   2019 |   42.88 |
| Capture Price (£/MWh) |   2020 |   31.91 |

### Identifiers

| Relationship   | ID Type              | ID(s)            |
|:---------------|:---------------------|:-----------------|
| Root           | OSUKED ID            | 10065            |
| Related        | Settlement BMU ID    | E_FAWN-1         |
| Related        | National Grid BMU ID | FAWN-1           |
| Equivalent     | ESAIL ID             | FAWN             |
| Equivalent     | Common Name          | Fawley Cogen     |
| Equivalent     | EUTL ID              | 96962            |
| Equivalent     | EIC ID               | 48W000000FAWN-1P |

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
| Longitude   |   -1.35 |
| Latitude    |   50.83 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |     Value |
|:-----------------------|-------:|----------:|
| CO2 Emissions (Tonnes) |   2005 | 277790.00 |
| CO2 Emissions (Tonnes) |   2006 | 277119.00 |
| CO2 Emissions (Tonnes) |   2007 | 282585.00 |
| CO2 Emissions (Tonnes) |   2008 | 215921.00 |
| CO2 Emissions (Tonnes) |   2009 | 215609.00 |
| CO2 Emissions (Tonnes) |   2010 | 132747.00 |
| CO2 Emissions (Tonnes) |   2011 |  39142.00 |
| CO2 Emissions (Tonnes) |   2012 |  39064.00 |
| CO2 Emissions (Tonnes) |   2013 |  46104.00 |
| CO2 Emissions (Tonnes) |   2014 |  45723.00 |
| CO2 Emissions (Tonnes) |   2015 |  48063.00 |
| CO2 Emissions (Tonnes) |   2016 |  44380.00 |
| CO2 Emissions (Tonnes) |   2017 |  49527.00 |
| CO2 Emissions (Tonnes) |   2018 |  45127.00 |
| CO2 Emissions (Tonnes) |   2019 |  53465.00 |
| CO2 Emissions (Tonnes) |   2020 |  47309.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     Value |
|:--------------------|-------:|----------:|
| Annual Output (MWh) |   2016 | 724544.62 |
| Annual Output (MWh) |   2017 | 996464.95 |
| Annual Output (MWh) |   2018 | 941954.05 |
| Annual Output (MWh) |   2019 | 865416.02 |
| Annual Output (MWh) |   2020 | 974412.89 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2016 |   41.11 |
| Capture Price (£/MWh) |   2017 |   44.48 |
| Capture Price (£/MWh) |   2018 |   56.84 |
| Capture Price (£/MWh) |   2019 |   42.58 |
| Capture Price (£/MWh) |   2020 |   33.32 |

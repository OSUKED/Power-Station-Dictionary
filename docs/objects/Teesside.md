### Identifiers

| Relationship   | ID Type              | ID(s)              |
|:---------------|:---------------------|:-------------------|
| Root           | OSUKED ID            | 10060              |
| Related        | Settlement BMU ID    | T_TESI-1, T_TESI-2 |
| Related        | National Grid BMU ID | TESI-1, TESI-2     |
| Equivalent     | GPPD ID              | GBR0002514         |
| Equivalent     | ESAIL ID             | TESI               |
| Equivalent     | Common Name          | Teesside           |
| Equivalent     | EUTL ID              | 97075              |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -1.13 |
| Latitude    |   54.57 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                    |
|:------------------------------------|:-------------------------------------------------------------------------|
| Installed Capacity (MW)             | 62.0                                                                     |
| Longitude                           | -1.0955                                                                  |
| Latitude                            | 54.6453                                                                  |
| Primary Fuel Type                   | Wind                                                                     |
| Owner                               | EDF Energy - Northern Offshore Windfarm Ltd                              |
| Source                              | UK Renewable Energy Planning Database                                    |
| URL                                 | https://www.gov.uk/government/collections/renewable-energy-planning-data |
| Geolocation Source                  | UK Renewable Energy Planning Database                                    |
| PLATTS-WEPP ID                      | 1084656.0                                                                |
| Estimated Annual Generation in 2017 | 156.29                                                                   |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 5177349.00 |
| CO2 Emissions (Tonnes) |   2006 | 5009264.00 |
| CO2 Emissions (Tonnes) |   2007 | 4482940.00 |
| CO2 Emissions (Tonnes) |   2008 | 4941647.00 |
| CO2 Emissions (Tonnes) |   2009 | 3263171.00 |
| CO2 Emissions (Tonnes) |   2010 | 2400721.00 |
| CO2 Emissions (Tonnes) |   2011 |    6085.00 |
| CO2 Emissions (Tonnes) |   2012 |    3919.00 |
| CO2 Emissions (Tonnes) |   2013 |     612.00 |

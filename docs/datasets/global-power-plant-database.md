---
hide:
  - toc
---

# Global Power Plant Database

[Homepage](https://datasets.wri.org/dataset/globalpowerplantdatabase)

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

<br>
**Metadata**

| Attribute    | Value(s)                                                  |
|:-------------|:----------------------------------------------------------|
| Keywords     | climate, energy, power plants                             |
| Contributors | Global Energy Observatory (Author)                        |
| Version      | 1.3.0                                                     |
| Licenses     | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |








<br>
**Fields**

| Column                         | Type   | Format   | Title                                     | Description                                                                               |
|:-------------------------------|:-------|:---------|:------------------------------------------|:------------------------------------------------------------------------------------------|
| country                        | string | default  | Country Code                              | The 3-letter ISO 3166-1 alpha code for each country                                       |
| country_long                   | string | default  | Country Name                              | The name of the country the power plant is located within                                 |
| name                           | string | default  | Name                                      | The name of the power plant                                                               |
| gppd_idnr                      | string | default  | GPPD ID                                   | The unique identifier for each power plant in the Global Power Plant Database             |
| capacity_mw                    | number | default  | Installed Capacity (MW)                   | Installed electrical capacity of eachpower plant (MW)                                     |
| latitude                       | number | default  | Latitude                                  | The north-south position of a point on the Earth's surface                                |
| longitude                      | number | default  | Longitude                                 | The east–west position of a point on the Earth's surface                                  |
| primary_fuel                   | string | default  | Primary Fuel Type                         | The primary fuel used by the power plant                                                  |
| other_fuel1                    | string | default  | Secondary Fuel Type                       | The secondary fuel used by the power plant                                                |
| other_fuel2                    | string | default  | Tertiary Fuel Type                        | The tertiary fuel used by the power plant                                                 |
| other_fuel3                    | string | default  | Quaternary Fuel Type                      | The quaternary fuel used by the power plant                                               |
| commissioning_year             | year   | default  | Commissioning Year                        | The first year the plant generated electricity                                            |
| owner                          | string | default  | Owner                                     | The primary owner of the power plant                                                      |
| source                         | string | default  | Source                                    | The source of the data on each power plant                                                |
| url                            | string | default  | URL                                       | URL linking directly to data source                                                       |
| geolocation_source             | string | default  | Geolocation Source                        | The source of the spatial data on each power plant                                        |
| wepp_id                        | number | default  | PLATTS-WEPP ID                            | The unique identifier used to refer to power plants in the PLATTS-WEBB dataset            |
| year_of_capacity_data          | year   | default  | Year of Capacity Report                   | The year of the reported capacity value                                                   |
| generation_gwh_2013            | number | default  | Annual Generation in 2013                 | Annual generation (during 2013) in gigawatt hours (GWhs), gross                           |
| generation_gwh_2014            | number | default  | Annual Generation in 2014                 | Annual generation (during 2014) in gigawatt hours (GWhs), gross                           |
| generation_gwh_2015            | number | default  | Annual Generation in 2015                 | Annual generation (during 2015) in gigawatt hours (GWhs), gross                           |
| generation_gwh_2016            | number | default  | Annual Generation in 2016                 | Annual generation (during 2016) in gigawatt hours (GWhs), gross                           |
| generation_gwh_2017            | number | default  | Annual Generation in 2017                 | Annual generation (during 2017) in gigawatt hours (GWhs), gross                           |
| generation_gwh_2018            | number | default  | Annual Generation in 2018                 | Annual generation (during 2018) in gigawatt hours (GWhs), gross                           |
| generation_gwh_2019            | number | default  | Annual Generation in 2019                 | Annual generation (during 2019) in gigawatt hours (GWhs), gross                           |
| generation_data_source         | string | default  | Generation Source                         | The source of the generation data on each power plant                                     |
| estimated_generation_gwh_2013  | number | default  | Estimated Annual Generation in 2013       | Estimated annual generation (during 2013) in gigawatt hours (GWhs), gross                 |
| estimated_generation_gwh_2014  | number | default  | Estimated Annual Generation in 2014       | Estimated annual generation (during 2014) in gigawatt hours (GWhs), gross                 |
| estimated_generation_gwh_2015  | number | default  | Estimated Annual Generation in 2015       | Estimated annual generation (during 2015) in gigawatt hours (GWhs), gross                 |
| estimated_generation_gwh_2016  | number | default  | Estimated Annual Generation in 2016       | Estimated annual generation (during 2016) in gigawatt hours (GWhs), gross                 |
| estimated_generation_gwh_2017  | number | default  | Estimated Annual Generation in 2017       | Estimated annual generation (during 2017) in gigawatt hours (GWhs), gross                 |
| estimated_generation_note_2013 | string | default  | Estimated Annual Generation Note for 2013 | A note on the estimation process behind calculating gross annual generation (during 2013) |
| estimated_generation_note_2014 | string | default  | Estimated Annual Generation Note for 2014 | A note on the estimation process behind calculating gross annual generation (during 2014) |
| estimated_generation_note_2015 | string | default  | Estimated Annual Generation Note for 2015 | A note on the estimation process behind calculating gross annual generation (during 2015) |
| estimated_generation_note_2016 | string | default  | Estimated Annual Generation Note for 2016 | A note on the estimation process behind calculating gross annual generation (during 2016) |
| estimated_generation_note_2017 | string | default  | Estimated Annual Generation Note for 2017 | A note on the estimation process behind calculating gross annual generation (during 2017) |

<br>

[Download](https://osuked.github.io/Power-Station-Dictionary/attribute_sources/global-power-plant-database/global_power_plant_database.csv){ .md-button }

<br>

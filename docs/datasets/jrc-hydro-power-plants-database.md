---
hide:
  - toc
---

# jrc-hydro-power-plants-database

[Homepage](https://github.com/energy-modelling-toolkit/hydro-power-database)



<br>
**Additional Metadata**

| Attribute   | Value(s)                                                  |
|:------------|:----------------------------------------------------------|
| Licenses    | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |








<br>
**Fields**

| Column                    | Type   | Description                                                                                                                       | Constraints                        |
|:--------------------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------|
| id                        | string | Unique identifier of the hydro-power plant                                                                                        | {'required': True, 'unique': True} |
| name                      | string | Name of the power plant                                                                                                           | {'required': True}                 |
| installed_capacity_MW     | number | Electrical power generation capacity in MW                                                                                        | {'required': True}                 |
| pumping_MW                | number | Pumping capacity in MW (only when specified)                                                                                      | nan                                |
| type                      | string | Typology of the power plant, according to the Dispa-SET classification of technologies http://www.dispaset.eu/en/latest/data.html | {'required': True}                 |
| country_code              | string | Country code according to ISO 3166-1 alpha-2                                                                                      | {'required': True}                 |
| lat                       | number | Latitude of the power plant in decimal degrees                                                                                    | {'required': True}                 |
| lon                       | number | Longitude of the power plant in decimal degrees (-180, 180)                                                                       | {'required': True}                 |
| dam_height_m              | number | Nominal head of the dam in meters                                                                                                 | nan                                |
| volume_Mm3                | number | Useful capacity of the reservoir in million of cubic meters                                                                       | nan                                |
| storage_capacity_MWh      | number | Potential quantity of energy that can be stored in MWh                                                                            | nan                                |
| avg_annual_generation_GWh | number | Expected/average generation per year (GWh)                                                                                        | nan                                |
| pypsa_id                  | number | Association with the ID column from https://github.com/PyPSA/pypsa-eur/blob/master/resources/powerplants.csv                      | nan                                |
| GEO                       | string | Association with the GEO Assigned Identification Number from http://globalenergyobservatory.org/                                  | nan                                |
| WRI                       | string | Association with the WRI Global Power Plant Database from https://www.wri.org/publication/global-power-plant-database             | nan                                |

<br>

[Download](https://osuked.github.io/Power-Station-Dictionary/attribute_sources/jrc-hydro-power-plants-database/jrc-hydro-power-plant-database.csv){ .md-button }

<br>

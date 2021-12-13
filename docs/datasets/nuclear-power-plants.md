---
hide:
  - toc
---

# Nuclear Power Plants Database

[Homepage](https://github.com/cristianst85/GeoNuclearData)

This repository contains a database with information about Nuclear Power Plants worldwide.

<br>
**Additional Metadata**

| Attribute    | Value(s)                                                    |
|:-------------|:------------------------------------------------------------|
| Licenses     | [ODbL-1.0](http://www.opendefinition.org/licenses/odc-odbl) |
| Version      | 0.17.0                                                      |
| Contributors | Cristian Stoica (Author)                                    |








<br>
**Fields**

| Column              | Type     | Format              | Title                   | Description                                                        | Rdftype                                                  |
|:--------------------|:---------|:--------------------|:------------------------|:-------------------------------------------------------------------|:---------------------------------------------------------|
| Id                  | integer  | default             | ID                      | Unique identifier used in this nuclear power plants database       | -                                                        |
| Name                | string   | default             | Name                    | The common name of the power plant                                 | -                                                        |
| Latitude            | number   | default             | Latitude                | The North/South position of the plant                              | http://www.w3.org/2003/01/geo/wgs84_pos#lat              |
| Longitude           | number   | default             | Longitude               | The East/West position of the plant                                | http://www.w3.org/2003/01/geo/wgs84_pos#long             |
| Country             | string   | default             | Country                 | The country in which the power plant is located                    | -                                                        |
| CountryCode         | string   | default             | Country  Code           | The ISO alpha-2 country codes                                      | -                                                        |
| Status              | string   | default             | Status                  | The operational status of the plant                                | -                                                        |
| ReactorType         | string   | default             | Reactor Type            | The type of nuclear reactor used in the plant                      | -                                                        |
| ReactorModel        | string   | default             | Reactor Model           | The model of nuclear reactor used in the plant                     | -                                                        |
| ConstructionStartAt | date     | %Y-%m-%d            | Construction Start Date | The date on which construction began                               | -                                                        |
| OperationalFrom     | date     | %Y-%m-%d            | Operational Start Date  | The date on which the site began operation                         | -                                                        |
| OperationalTo       | date     | %Y-%m-%d            | Operational End Date    | The date on which the site was shutdown                            | -                                                        |
| Capacity            | integer  | default             | Capacity (MW)           | The maximum power output capacity of the plant                     | http://openenergy-platform.org/ontology/oeo/OEO_00230003 |
| LastUpdatedAt       | datetime | %Y-%m-%dT%H:%M:%S%z | Last Updated Datetime   | The datetime when the data on the specified plant was last updated | -                                                        |
| Source              | string   | default             | Data Source             | The source from which the data on this plant was extracted         | -                                                        |
| IAEAId              | integer  | default             | IAEA ID                 | The unique identifier used by the IAEA                             | -                                                        |

<br>

[Download](https://osuked.github.io/Power-Station-Dictionary/attribute_sources/nuclear-power-plants/nuclear_power_plants.csv){ .md-button }

<br>

---
hide:
  - toc
---

# BMU Fuel Types

[Homepage](https://www.bmreports.com/bmrs/?q=eds/main)

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

<br>
**Additional Metadata**

| Attribute    | Value(s)                                                                                            |
|:-------------|:----------------------------------------------------------------------------------------------------|
| Keywords     | Elexon, Fuel                                                                                        |
| Contributors | Elexon (Author)                                                                                     |
| Version      | 1.0.0                                                                                               |
| Licenses     | [Elexon Licence](https://www.elexon.co.uk/using-this-website/disclaimer-and-reservation-of-rights/) |

<br>
<br>
<br>

### Resources


##### bmu-fuel-types



<br>
**Fields**

| Column      | Type     | Format         | Title               | Description                                                                      |
|:------------|:---------|:---------------|:--------------------|:---------------------------------------------------------------------------------|
| NGC_BMU_ID  | string   | default        | NGC BMU ID          | The Balancing Mechanism Unit identifier used by the National Grid Company        |
| SETT_BMU_ID | string   | default        | Settlement BMU ID   | The Balancing Mechanism Unit identifier used for settlement purposes by Elexon   |
| FUEL TYPE   | string   | default        | Fuel Type           | The fuel type consumed by the specified BMU                                      |
| EFF_FROM    | datetime | %d/%m/%Y %H:%M | Date Effective From | Date from which this BMU id has been utilised                                    |
| EFF_TO      | datetime | %d/%m/%Y %H:%M | Date Effective To   | Date that this BMU id has been utilised up to                                    |
| Comments    | any      | default        | Comments            | -                                                                                |
| EELPS?      | any      | default        | EELPS               | EELPS refers to whether the site is an Embedded                                  |
|             |          |                |                     | Exemptable Large Power Station. EELPS sites do not normally have settlement ids. |

<br>

[Download](https://osuked.github.io/Power-Station-Dictionary/attribute_sources/bmu-fuel-types/BMUFuelType 2021-08-09.csv){ .md-button }

<br>

##### detailed-bmu-fuel-types



<br>
**Fields**

| Column     | Type   | Format   | Title      | Description                                                               |
|:-----------|:-------|:---------|:-----------|:--------------------------------------------------------------------------|
| ngc_bmu_id | string | default  | NGC BMU ID | The Balancing Mechanism Unit identifier used by the National Grid Company |
| fuel_type  | string | default  | Fuel Type  | The fuel type consumed by the specified BMU                               |
| comments   | string | default  | Comments   | -                                                                         |

<br>

[Download](https://osuked.github.io/Power-Station-Dictionary/attribute_sources/bmu-fuel-types/fuel_types.csv){ .md-button }

<br>

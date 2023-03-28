---
hide:
  - toc
---

# CfD Contract Portfolio Status

[Homepage](https://www.lowcarboncontracts.uk/data-portal/dataset/cfd-contract-portfolio-status)

This dataset includes each CfD Contract, its Maximum Contract Capacity and latest status of each project.

Status of each CfD project is determined based on the notices issued by LCCC when different milestones get past. Start date is the best estimate date on which the generator will start generating.

<br>
**Additional Metadata**

| Attribute    | Value(s)                                                                                 |
|:-------------|:-----------------------------------------------------------------------------------------|
| Keywords     | LCCC, CfD, Capacity                                                                      |
| Licenses     | [OGL-UK-3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) |
| Contributors | LCCC (Author)                                                                            |
| Version      | 2021-10-01                                                                               |








<br>
**Fields**

| Column                                  | Type     | Format            | Title                                   | Description                                                                                                                                                                                                                                                                                                                       |
|:----------------------------------------|:---------|:------------------|:----------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CFD_ID                                  | string   | default           | CfD ID                                  | ID which identifies each CfD generator                                                                                                                                                                                                                                                                                            |
| Name_of_CFD_Unit                        | string   | default           | Name of CfD Unit                        | Name of a CfD Unit                                                                                                                                                                                                                                                                                                                |
| Allocation_Round                        | string   | default           | Allocation Round                        | The associated CfD allocation round for the site                                                                                                                                                                                                                                                                                  |
| Technology_Type                         | string   | default           | Technology Type                         | Technologies of CfD generators                                                                                                                                                                                                                                                                                                    |
| Transmission_or_Distribution_connection | string   | default           | Transmission or Distribution Connection | Connection type of the transmission or distribution network                                                                                                                                                                                                                                                                       |
| Status                                  | string   | default           | Status                                  | Different stages of CfD contracts. E.g: Pre-Start Date, Post-Start Date,Terminated                                                                                                                                                                                                                                                |
| Expected_Start_Date                     | datetime | %Y-%m-%d %H:%M:%S | Estimated Start Date                    | Estimated date on which the generator will start generating                                                                                                                                                                                                                                                                       |
| Maximum_Contract_Capacity_MW            | number   | default           | Maximum Contract Capacity (MW)          | Generators submit an Initial Installed Capacity Estimate (IICE) at the time of application. The IICE is used as a reference point throughout the CfD. For a successful generator, Installed Capacity can only ever be altered lower than the IICE. The IICE can be adjusted downwards by up to 25% by the Milestone Delivery Date |

<br>

[Download](https://osuked.github.io/Power-Station-Dictionary/attribute_sources/cfd-contract-portfolio-status/cfd-contract-portfolio-status.csv){ .md-button }

<br>

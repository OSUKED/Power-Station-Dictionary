---
hide:
  - toc
---

# Renewable Energy Planning Database

[Homepage](https://www.gov.uk/government/publications/renewable-energy-planning-database-monthly-extract)

The Renewable Energy Planning Database ('REPD') is managed by Barbour ABI on behalf of the Department of Business, Energy & Industrial Strategy ('BEIS’). The databases track the progress of renewable electricity projects (including those that could also be used for CHP), and electricity storage projects  from inception, through planning, construction, operation and decommissioning.

The REPD is updated on a quarterly basis, and contains information on all Renewable Electricity and CHP projects up to the end of the previous calendar month.

<br>
**Additional Metadata**

| Attribute    | Value(s)                        |
|:-------------|:--------------------------------|
| Keywords     | BEIS, REPD, renewable, planning |
| Version      | June 2021                       |
| Contributors | BEIS (Author)                   |








<br>
**Fields**

| Column                                  | Type    | Format   | Description                                                                                                                           | Title                                   | Rdftype                                                  |
|:----------------------------------------|:--------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------|:---------------------------------------------------------|
| Old Ref ID                              | string  | default  | The old reference ID associated with a project in a previous version of the database                                                  | Old Ref ID                              | -                                                        |
| Ref ID                                  | integer | default  | Project reference ID number in REPD database                                                                                          | Ref ID                                  | -                                                        |
| Record Last Updated (dd/mm/yyyy)        | date    | %d/%m/%Y | Date a project record was last updated or checked                                                                                     | Record Last Updated                     | -                                                        |
| Operator (or Applicant)                 | string  | default  | Name of operator or applicant                                                                                                         | Operator (or Applicant)                 | -                                                        |
| Site Name                               | string  | default  | Name of development site                                                                                                              | Site Name                               | -                                                        |
| Technology Type                         | string  | default  | Type of technology (e.g. solar photovoltaics, offshore wind etc.)                                                                     | Technology Type                         | -                                                        |
| Storage Type                            | string  | default  | Describes whether the attached storage is co-located with RES/fossil-fuels or stand-alone                                             | Storage Type                            | -                                                        |
| Storage Co-location REPD Ref ID         | string  | default  | The (new) REPD ID associated with the storage unit attached to the site                                                               | Storage Co-location REPD Ref ID         | -                                                        |
| Installed Capacity (MWelec)             | number  | default  | Installed electrical capacity in megawatts (MW)                                                                                       | Installed Capacity (MWelec)             | http://openenergy-platform.org/ontology/oeo/OEO_00230003 |
| CHP Enabled                             | string  | default  | Is the project capable of combined heat and power output                                                                              | CHP Enabled                             | -                                                        |
| RO Banding (ROC/MWh)                    | number  | default  | The banding levels for the RO subsidy, where each band represents a multiplier to the standard ROC price                              | RO Banding (ROC/MWh)                    | -                                                        |
| FiT Tariff (p/kWh)                      | number  | default  | The price received by the site through the FiT scheme                                                                                 | FiT Tariff (p/kWh)                      | -                                                        |
| CfD Capacity (MW)                       | number  | default  | The maximum contracted capacity which can receive subsidies through the CfD scheme                                                    | CfD Capacity (MW)                       | -                                                        |
| Turbine Capacity (MW)                   | number  | default  | For windfarms, the individual capacity of each wind turbine in megawatts (MW)                                                         | Turbine Capacity (MW)                   | -                                                        |
| No. of Turbines                         | number  | default  | For windfarms, the number of wind turbines to be located on the development site                                                      | No. of Turbines                         | -                                                        |
| Height of Turbines (m)                  | number  | default  | For windfarms, the height of the wind turbines in metres (m)                                                                          | Height of Turbines (m)                  | http://openenergy-platform.org/ontology/oeo/OEO_00140000 |
| Mounting Type for Solar                 | string  | default  | For solar PV developments, whether the PV panels are ground or roof mounted                                                           | Mounting Type for Solar                 | -                                                        |
| Development Status                      | string  | default  | The full description of the current development status                                                                                | Development Status                      | -                                                        |
| Development Status (short)              | string  | default  | The short description of the current development status                                                                               | Development Status (short)              | -                                                        |
| Address                                 | string  | default  | Site address of the development                                                                                                       | Address                                 | -                                                        |
| County                                  | string  | default  | County the development site is located within                                                                                         | County                                  | -                                                        |
| Region                                  | string  | default  | Region the development site is located within                                                                                         | Region                                  | -                                                        |
| Country                                 | string  | default  | Country the development site is located within                                                                                        | Country                                 | -                                                        |
| Post Code                               | string  | default  | Post code of the development site                                                                                                     | Post Code                               | -                                                        |
| X-coordinate                            | integer | default  | X coordinate for development site in British National Grid (EPSG:27700)                                                               | X-coordinate                            | -                                                        |
| Y-coordinate                            | integer | default  | Y coordinate for development site in British National Grid (EPSG:27700)                                                               | Y-coordinate                            | -                                                        |
| Planning Authority                      | string  | default  | The relevant local planning authority for the project                                                                                 | Planning Authority                      | -                                                        |
| Planning Application Reference          | string  | default  | The reference number associated with the planning application                                                                         | Planning Application Reference          | -                                                        |
| Appeal Reference                        | string  | default  | The reference number associated with an appeal                                                                                        | Appeal Reference                        | -                                                        |
| Secretary of State Reference            | string  | default  | The reference number associated with a Secretary of State Intervention                                                                | Secretary of State Reference            | -                                                        |
| Type of Secretary of State Intervention | string  | default  | The type of Secretary of State of Intervention. This can be one of three types: recovery, call-in, or holding direction               | Type of Secretary of State Intervention | -                                                        |
| Judicial Review                         | integer | default  | The latest date of when a legal challenge has been launched to review the lawfulness of a planning application and/or appeal decision | Judicial Review                         | -                                                        |
| Offshore Wind Round                     | string  | default  | Leasing round in which an offshore wind project was established                                                                       | Offshore Wind Round                     | -                                                        |
| Planning Application Submitted          | date    | %d/%m/%Y | Date planning application was validated                                                                                               | Planning Application Submitted          | -                                                        |
| Planning Application Withdrawn          | date    | %d/%m/%Y | Date planning application was withdrawn                                                                                               | Planning Application Withdrawn          | -                                                        |
| Planning Permission Refused             | date    | %d/%m/%Y | Date planning permission was refused                                                                                                  | Planning Permission Refused             | -                                                        |
| Appeal Lodged                           | date    | %d/%m/%Y | Date an appeal was lodged                                                                                                             | Appeal Lodged                           | -                                                        |
| Appeal Withdrawn                        | date    | %d/%m/%Y | Date an appeal was withdrawn                                                                                                          | Appeal Withdrawn                        | -                                                        |
| Appeal Refused                          | date    | %d/%m/%Y | Date an appeal was refused (dismissed)                                                                                                | Appeal Refused                          | -                                                        |
| Appeal Granted                          | date    | %d/%m/%Y | Date an appeal was granted (upheld)                                                                                                   | Appeal Granted                          | -                                                        |
| Planning Permission Granted             | date    | %d/%m/%Y | Date planning permission was granted by the planning authority                                                                        | Planning Permission Granted             | -                                                        |
| Secretary of State - Intervened         | date    | %d/%m/%Y | Date of a project that is 'Called In' by the Secretary of State                                                                       | Secretary of State - Intervened         | -                                                        |
| Secretary of State - Refusal            | date    | %d/%m/%Y | Date planning permission was refused by the Secretary of State                                                                        | Secretary of State - Refusal            | -                                                        |
| Secretary of State - Granted            | date    | %d/%m/%Y | Date planning permission was granted by the Secretary of State                                                                        | Secretary of State - Granted            | -                                                        |
| Planning Permission Expired             | date    | %d/%m/%Y | Date a planning permission expires (as per the planning decision)                                                                     | Planning Permission Expired             | -                                                        |
| Under Construction                      | date    | %d/%m/%Y | Date construction on site has begun                                                                                                   | Under Construction                      | -                                                        |
| Operational                             | date    | %d/%m/%Y | Date a project become operational                                                                                                     | Operational                             | -                                                        |
| Heat Network Ref                        | integer | default  | The reference ID for the associated heat-network within the Heat Networks Planning Database                                           | Heat Network Ref                        | -                                                        |

<br>

[Download](https://osuked.github.io/Power-Station-Dictionary/attribute_sources/renewable-energy-planning-database/renewable-energy-planning-database-q2-june-2021.csv){ .md-button }

<br>

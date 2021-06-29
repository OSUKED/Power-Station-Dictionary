# Climate Subak Fellowship Project on Energy Data Linking

## Overview

### Long-Term Vision for Linked Energy Data 

We want to be able describe datasets in a standardised format and then link these datasets to specific concepts such as network assets - the semantic web provides a framework to realise this in, however, it brings with it a range of potential barriers. These include difficulty in scaling (specifically due to the knowledge engineering component), a lack of incentives to properly mark up data (due to a relative lack of useful applications), and a general complexity overhead relating to the number of tools and languages that need to be used to create a useful knowledge graph. This necessitates tooling and design patterns which enable this complexity to be abstracted - this project aims to develop the core initial components of that infrastructure.

*** To be completed ***

* Add top-level diagram of the knowledge graph, surrounding wrappers, and HTML view
* Discuss the benefits of the decentralised aspect 
* Discuss how splitting this framework across smaller components that can be isolated makes it easier for new users to contribute - as they don't have to understand the full framework to create a new component for their specific dataset/sub-domain
* Discuss how the knowledge graph could extend well beyond simply connecting datasets to physical assets, e.g. by linking agents to datasets/assets, datasets to publications, publications/datasets to software

Top-Level Aims:
* Data publishers can easily release new datasets which can be automatically integrated into the knowledge graph
* Data publishers can automatically validate their datasets
* Data consumers can automatically load raw data (and its associated metadata) into common formats across a variety of programming languages (e.g. Pandas DataFrames)
* Data consumers can automatically merge data that describes related assets, even if the raw datasets contain different ids for those assets
* Data consumers can search for datasets using explicit queries that account for the relationships between the datasets and the assets they describe
* Enable crawlers such as Google to automatically integrate datasets into their dataset search


<br>

### What is In/Out of Scope for this Project

This fellowship project will focus on developing the data structures and tooling for building this knowledge graph, with a pilot example for linking power output and carbon emissions datasets to physical assets. This specific project is not setting out to comprehensively describe the full power system and all energy datasets through a unified knowledge graph, instead we are focusing on developing the infrastructure and software patterns than enable others to develop and merge-in their own knowledge graphs.

The project can be broken down into the following steps:
* Identifying standards that allows rich representation of csv and API metadata
* Developing a standard for describing how a set of physical assets link to external datasets
* Creating Python libraries that can take these metadata standards and map the information they contain into an RDF/OWL knowledge graph representation (and vice versa)
* Creating a front-end that shows the information contained in the knowledge graph, with HTML views for both the datasets and assets

<br>

### Example User Stories

*** To be completed ***


<br>

### What Does Success of this Project Look Like?

* Users are able to easily publish energy datasets using the OpenAPI/FD specifications and then see their datasets appear in a front-end view of the knowledge graph without being required to code anything or to understand the back-end data structures
* Users are able to build their own parsers for converting custom data specifications to the Climate Subak RDF representation with minimal friction (using guides developed in this project)
* The project builds as much as possible on top of existing mature technologies/specifications/design patterns
* The project should be easily extendable by Subak (or external orgs)
* Minimal long-term input from Subak, both in terms of maintaining the codebase and providing community support

N.b. Users refers to people/organisations internal and external to Subak (and who ideally were not involved in the project development).

<br>
<br>

## Dataset Metadata

Before we can link between data-sets we need to represent their metadata in a machine-readable and standardised form. This section outlines the specifications we have identifed as covering the largest range of requirements, the reasoning behind using them in the first place, and how this project differs from similar work on energy metadata standardisation being done by the EDVP.

* Need to discuss that I will be developing Python libraries that map from the metadata specifications to the generalised RDF metadata representations

<br>

### The OpenAPI Specification

*** To be completed ***

* Show an example of the top-level metadata information
* Show an example of how endpoints are described
* Show the spec generation and validation tooling
* Show the auto-generated clients for various languages
* List interesting libraries that integrate with the spec
* Link community/support groups
* List the ontology extensions required to cover the spec

<br>

### The Frictionless Data Specification

*** To be completed ***

* Show an example of the top-level metadata information
* Show an example of how resources are described
* Show the spec generation and validation tooling
* Show the data loading client for Python and JS
* List interesting libraries that integrate with the spec
* Link community/support groups
* List the ontology extensions required to cover the spec

<br>

### Why Introduce Another Layer of Standards on top of RDF/OWL?

We want to be a able to easily grow the dataset knowledge graph in a decentralised way, however, often the expansion of these types of graph stuggles to scale well. This is because trying to create a data specification (and associated tooling) that's able to describe every conceivable concept naturally comes with quite a high complexity overhead. In turn this makes it difficult for new users to contribute. 

To reduce this burden we're piggy-backing off of existing narrower specifications that are used to describe tabular data and APIs. Specifically, we're using the Frictionless Data specification to describe csv-like data, and the OpenAPI specification for describing API endpoints. Both of these come with tooling for generating the metadata representations; as well as a wider ecosystem around auto-generated documentation, download clients, data validation, etc. Additionaly, they both allow highly rich representations of metadata that covers the majority of the use-cases we have identified, those that they don't cover natively can still be included but won't be recognised by external tools.

A further benefit is that data publishers who choose to represent their metadata in these formats can get immediate benefit regardless of whether they are ultimately integrated into the wider knowledge graph (thanks to the wider ecosystem tools previously mentioned). They are also able to host this representation themselves, rather than having to edit the metadata in a centralised data catalog. These both align with the wider project goals of increasing incentives to publish data and ensuring that the individual project components offer value in isolation.

<br>

### Isn't this What the EDVP is Already Doing?

The *Energy Data Visibility Project* (EDVP) was commissioned by BEIS as part of the Modernising Energy Data programme - "It focuses specifically on the Energy Data Task Force report’s recommendation 3, outlining how the energy sector’s data needs to be more visible". Their goals are highly similar to those in this project, namely to make energy data more "discoverable, searchable, and understandable". Our plan is very much to build on top of the work being done as part of the EDVP, however, we believe that there are currently aspects to energy data linkage that the EDVP is not covering, including:

The ability to describe dataset fields, e.g:
* Including field formats enables automated data validation
* Including field types enables more explicit parsing of data for client tools (e.g. specifying types when loading into a Pandas dataframe)
* Including a field RDF URI could enable fields across different datasets to be linked, as well as provide additional information such as units of measurement

An RDF mapping, which would enable:
* The dataset metadata to be merged with other knowledge graphs
* merged data from external graphs to be propogated back to the dataset metadata - e.g. by merging with a graph that describes how assets link to datasets, a new representation of a dataset's specification could be generated that includes information on the assets it describes

The EDVP is currently developing a CKAN repository of energy datasets, merging catalogs developed by organisations such as National Grid ESO. We will aim to map as much CKAN metadata as possible to the RDF dataset representation we are developing, enabling datasets in those catalogs to be integrated into the dataset knowledge graph. Once the metadata has been integrated into the knowledge graph it could then be converted back into its original CKAN form, or into the FD/OpenAPI specifications -  making it much easier for data publishers to convert between specification formats.

TLDR: They're complementary not competitive

* Add in diagram of CKAN -> knowledge graph -> FD/OpenAPI spec

<br>

### Metadata Overlaps

*** To be completed ***

* Create a table where rows are specific metadata attributes and the columns are  specifications/platforms

<br>
<br>

## Asset Dictionary

At its core the dictionary will comprise of a collection of JSON mappings expressing 1:1, 1:N, N:1, and N:N relationships between asset ids (represented as RDF URIs) and ids contained within external datasets. The external ids could represent the exact same entity (just under an alternative indexing system), or a related entity (such as an owner in the case of a power plant dictionary).

The dictionary will itself be an FD package, with the JSON mappings as the dataset resources. The metadata of the asset dictionary will then include information on which external datasets the JSON mappings relate to, down to the specific field name of the column containing those ids. 

The Frictionless Data specification includes the ability to express primary and foreign keys, which could be used to further link to external datasets whilst remaining solely within the FD ecosystem. If they build out their own tools to connect datasets using foreign keys then all of the work we’re doing should immediately be compatible.

* Add in examples of what the dictionary components will look like
* Describe how the dictionary will load the datasets its linked to, extract any semantic data relating to specific assets, and then generate an RDF representation of each asset that contains both the links to the datasets and specific information extracted from them

<br>
<br>

## Front-End

The dictionary ‘back-end’ is a code generator for a series of web-pages (one for each node – e.g. power plant) where:
The header script contains the RDF information as JSON-LD
The visible part of the page shows relationships to other nodes (e.g. datasets/projects analysing the plant/plant owners, etc) 
It also shows attributes which have been extracted from linked datasets with field types that have RDF representations understood by the dictionary (e.g. nameplate_capacity_MW)

Will need to have a page in the dictionary showing which RDF data-types are understood (and will be auto-linked), as well as a guide on how best create new RDF data-types that fit into the ontology


*** To be completed ***


<br>
<br>

## FAQs

*** To be completed ***


<br>
<br>

## Glossary

> Should filter and provide as an appendix to any output documents from the fellowship

*** To be completed ***

* CKAN
* DCAT
* Frictionless Data (FD)
* OpenAPI
* Ontology
* RDF
* Knowledge Graph

<br>
<br>

## Datasets We Should Ideally Include

*** To be expanded ***

* BMRS API
* Elexon csv/xlsx datasets
* Electric Insights (datapackage not API)
* ENTSOE API
* Grant Wilson's historical fuel generation time-series

N.b. datasets included in this section are not necessarily in scope for integration as part of this fellowship project, but should be considered when developing the ontologies.

<br>
<br>

## Organisations/People We Should Engage With

*** To be expanded ***

- [x] Sheffield Solar - Jamie
- [ ] Elexon/BMRS - Reza (developing their Kinnect Insights Solution platform)
- [ ] WPD digitisation team
- [x] LCCC Data Portal team
- [ ] NG ESO Data Portal team - (should also speak to Lyndon Ruff about the carbon intensity API)
- [ ] OpenEnergyMod - Robbie Morrison/Tom Brown
- [x] Electricity Map - Olivier Corradio
- [ ] Energy Informatics Group at Birmingham Uni - Grant Wilson
- [x] Frictionless Data team
- [ ] Open Power Systems Data team
- [ ] Open Energy Ontology team
- [ ] ESC - Jake Verma

<br>
<br>

## Concepts to Capture in the Power System Ontology

> Should think about potential dataset search queries and identify the concepts required to implement them

*** To be expanded ***

* Datetimes
	* Date
	* Time (non-tz localised)
	* Datetime (UTC)
	* Datetime (Europe/London)
	* Settlement Period
* Location 
	* Lon/Lat (could import from `geopoints`)
	* GSP
	* DNO
	* Statistical boundaries (LSOA, MSOA, etc)
* 
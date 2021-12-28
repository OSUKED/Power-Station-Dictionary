### Dictionary Schema & Core Dataset

The dictionary is composed of two files, a csv file containing ids where each row relates to a different asset (in this case power stations) and a json containing metadata describing the columns in the csv, written as an extension to the Frictionless Data Tabular schema. “Frictionless Data is an open-source toolkit that brings simplicity to the data experience” through an open-source standard that defines a specification for describing metadata relating to different types of datasets. Once a dataset has been described using the specification it then becomes incredibly easy to load it using different programming languages as well as export it into a wide range of different formats. What makes Frictionless Data different to most other specifications is that they provide a comprehensive way to describe individual columns within a dataset, including their formats and constraints.

The majority of the schema is the same as the Tabular Schema published by Frictionless Data. The core change is the use of `foreignKeys` to link to external datasets that use ids specified in the dictionary, a separate `attributes` entry then describes the columns which should be extracted from the dataset. The `hierarchy` attribute for each column then describes whether the ids in that column have a `same-as` or `part-of` relationship with the asset they’re linked to. A further `url_format` entry then provides a way to convert specific IDs into urls (e.g. with wikidata ids).

Datasets linked to by the dictionary must be described using the Frictionless Data tabular schema. Data-providers from within the energy sector already using this format include Public Utility Data Library, Open Power System Data, and the Open Energy Platform. However, datasets not using this format can still be linked by the dictionary.  All that is required is that the datasets’ metadata is created in the Frictionless Data schema, either by the data owner or by a third party, and it can be stored separately from the raw data.  As well as being able to link into the dictionary, by publishing your datasets using this standard you can make use of a [wider ecosystem of data tools](https://frictionlessdata.io/software/).

<br>

### Building the Website

The dictionary provides value in itself by enabling users to query and link data relating to an entity described across multiple datasets.  However, to make data exploration and analysis easier we can create a graph where data on a single asset is collated from multiple sources.  

Once the dictionary has been created, a Python library uses it to programmatically identify the different assets it contains and extract data relating to those assets from the datasets linked by the dictionary. The generation steps are as follows:

1. Each row of the dictionary is iterated over with the associated ids extracted for each asset
2. The datasets linked to the dictionary which contain an id relating to the current asset are identified
3. The relevant attributes for each asset which are contained in the linked datasets are then extracted
4. The combined ids, datasets, and attribute data for the asset is saved as JSON
5. For each asset the outputted linked ids, datasets, and attributes are then used to populate a markdown template which forms the basis of a webpage within the dictionary site

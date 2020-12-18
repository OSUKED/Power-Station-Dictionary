# Power Station Dictionary

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/OSUKED/Power-Station-Dictionary/main?urlpath=lab)

<br>

> This repository exposes a power station dictionary that enables mapping between various naming conventions and associated plant metadata, it also explains how you can help contribute to this open-source project.

<br>

The core output of this project is a clean output power plant dataset that includes relevant attributes such as location and capacity, as well as id mappings that can be used to connect them to other datasets. The `powerdict` module will construct this dataset from the files contained in three of the data directories:

* *raw* - source datasets as csvs
* *updates* - JSON mappings from an osuked_id to a new attribute value
* *definitions* - JSON specification of how to process the raw sources

CI/CD is set-up so that any changes in this repository will trigger a reconstruction of the output dataset, additionally a new GitHub releases will automatically trigger a new release on Zenodo and produce an updated DOI. The output dataset can be found [here](https://github.com/OSUKED/Power-Station-Dictionary/blob/main/data/output/power_stations.csv).

<br>
<br>

### Installation

To install the `powerdict` library please run:

```bash
pip install powerdict
```

<br>

### Development Set-Up

To create a new environment you can follow the following code blocks or run the `setup_env` batch script located in the batch_scripts directory.

```
git clone
conda env create -f environment.yml
conda activate powerdict
```

<br>

### Publishing to PyPi

To publish the `powerdict` module to PyPi simply run the following from the batch_scripts directory

```bash
pypi_publish
```

When prompted you should enter your PyPi username and password

After this you will be able to install the latest version of powerdict using `pip install powerdict`
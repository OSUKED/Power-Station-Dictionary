# Welcome to the Power Station Dictionary

<br>

> This site exposes a power station dictionary that enables mapping between various naming conventions and associated plant metadata, it also explains how you can help contribute to this open-source project.

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
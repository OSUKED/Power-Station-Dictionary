# Downloading & Exploring the Input Data



```python
import pandas as pd
import geopandas as gpd
import numpy as np

import requests
from bs4 import BeautifulSoup as bs

import matplotlib.pyplot as plt
import FEAutils as hlp
```

<br>

### *ESAIL* Dataset

This dataset was initially developed by Patrick De Mars and Connor Galbraith, then updated and extended by Ayrton Bourn, all of whom were historically or are currently in the Energy Systems & AI Lab at UCL. 

Currently this dataset is missing key information such as the EIC code, capacity, and owners.

```python
df_ESAIL = pd.read_csv('../data/raw/ESAIL.csv')

df_ESAIL.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sett_bmu_id</th>
      <th>ngc_bmu_id</th>
      <th>bmu_root</th>
      <th>name</th>
      <th>primary_fuel_type</th>
      <th>detailed_fuel_type</th>
      <th>longitude</th>
      <th>latitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>E_MARK-1</td>
      <td>MARK-1</td>
      <td>MARK</td>
      <td>Rothes Bio-Plant CHP 1</td>
      <td>biomass</td>
      <td>bone</td>
      <td>-3.603516</td>
      <td>57.480403</td>
    </tr>
    <tr>
      <th>1</th>
      <td>E_MARK-2</td>
      <td>MARK-2</td>
      <td>MARK</td>
      <td>Rothes Bio-Plant CHP 2</td>
      <td>biomass</td>
      <td>bone</td>
      <td>-3.603516</td>
      <td>57.480403</td>
    </tr>
    <tr>
      <th>2</th>
      <td>T_DIDC1</td>
      <td>DIDC1</td>
      <td>DIDC</td>
      <td>Didcot A (G) 1</td>
      <td>coal</td>
      <td>coalgas_opt_out</td>
      <td>-1.267570</td>
      <td>51.623630</td>
    </tr>
    <tr>
      <th>3</th>
      <td>T_DIDC2</td>
      <td>DIDC2</td>
      <td>DIDC</td>
      <td>Didcot A (G) 2</td>
      <td>coal</td>
      <td>coalgas_opt_out</td>
      <td>-1.267570</td>
      <td>51.623630</td>
    </tr>
    <tr>
      <th>4</th>
      <td>T_DIDC4</td>
      <td>DIDC4</td>
      <td>DIDC</td>
      <td>Didcot A (G) 4</td>
      <td>coal</td>
      <td>coalgas_opt_out</td>
      <td>-1.267570</td>
      <td>51.623630</td>
    </tr>
  </tbody>
</table>
</div>



<br>

We can see how many entries we have

```python
df_ESAIL.shape[0]
```




    493



<br>

We can use `value_counts` to identify the most common fuel types, we can see that most of the plants are wind farms.

```python
df_ESAIL['primary_fuel_type'].value_counts()
```




    wind              147
    gas                94
    coal               74
    fuel_oil           60
    nuclear            34
    run_of_river       31
    pumped_storage     16
    aggregator         14
    other              10
    rgt                 7
    battery             3
    biomass             3
    Name: primary_fuel_type, dtype: int64



<br>

We'll quickly calculate the average number of BMU ids per location

```python
avg_num_BMUs_per_loc = df_ESAIL['sett_bmu_id'].nunique()/df_ESAIL['bmu_root'].nunique()

print(f'The average number of BMU ids per location is {avg_num_BMUs_per_loc:.2f}')
```

    The average number of BMU ids per location is 2.01
    

<br>

Its always useful to visualise this kind of data spatially so we'll load in a basemap with separate zones for each grid supply point

```python
gdf_GSP_locs = gpd.read_file('../data/raw/GSP_shapefile/GSP_regions_20181031.shp')

gdf_GSP_locs.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>RegionID</th>
      <th>RegionName</th>
      <th>geometry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>149</td>
      <td>Beddington (_J)</td>
      <td>POLYGON ((543750.561 167428.882, 549430.486 13...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>150</td>
      <td>Northfleet East</td>
      <td>POLYGON ((571652.936 143992.711, 550968.129 13...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>155</td>
      <td>Sellindge</td>
      <td>POLYGON ((624923.598 137169.470, 624894.947 13...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>160</td>
      <td>Richborough</td>
      <td>POLYGON ((626375.397 137910.687, 623652.026 16...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>156</td>
      <td>Chessington</td>
      <td>POLYGON ((523319.962 166572.557, 526121.634 14...</td>
    </tr>
  </tbody>
</table>
</div>



<br>

We'll then overlay this with the power plant locations.

We can see trends such as run of river hydro in Scotland, as well as nuclear concentrated around the coast where there's easy access to cooling water. It also raises some potential errors, e.g. the fuel oil plant that is shown off the coast.

```python
fuel_types = df_ESAIL['primary_fuel_type'].unique()

## Plotting
fig, ax = plt.subplots(figsize=(3, 5), dpi=250)

gdf_GSP_locs.to_crs('EPSG:4326').plot(ax=ax, alpha=0.3, edgecolor='w')

for fuel_type in fuel_types:
    df_fuel_specific = df_ESAIL[df_ESAIL['primary_fuel_type']==fuel_type]
    ax.scatter(df_fuel_specific['longitude'], df_fuel_specific['latitude'], s=2, alpha=1, label=fuel_type)

hlp.hide_spines(ax, positions=['top', 'bottom', 'left', 'right'])
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-9, 3)
ax.legend(frameon=False, bbox_to_anchor=(1, 0.75))
```




    <matplotlib.legend.Legend at 0x22c0f861b20>




![png](img/nbs/output_12_1.png)


<br>

### *Open Power System Data* Dataset

We want to make sure that we're always downloading the latest available dataset from OPSD so we'll identify which csv that is from their website

```python
opsd_root = 'https://data.open-power-system-data.org'
page_url = f'{opsd_root}/conventional_power_plants/2020-10-01'

r = requests.get(page_url)

r
```




    <Response [200]>



<br>

From this we can search for the csv and then extract the url that it refers to using `BeautifulSoup`

```python
soup = bs(r.content)

csv_url = opsd_root + '/' + soup.find('a', string='conventional_power_plants_EU.csv')['href']
release_date = csv_url.split('/')[-2]

release_date
```




    '2020-10-01'



<br>

We can now use `pandas` to load this directly into a dataframe

```python
df_OPSD = pd.read_csv(csv_url)

df_OPSD.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>company</th>
      <th>street</th>
      <th>postcode</th>
      <th>city</th>
      <th>country</th>
      <th>capacity</th>
      <th>energy_source</th>
      <th>technology</th>
      <th>chp</th>
      <th>...</th>
      <th>type</th>
      <th>lat</th>
      <th>lon</th>
      <th>eic_code</th>
      <th>energy_source_level_1</th>
      <th>energy_source_level_2</th>
      <th>energy_source_level_3</th>
      <th>additional_info</th>
      <th>comment</th>
      <th>source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Marcinelle Energie (Carsid)</td>
      <td>DIRECT ENERGIE</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>BE</td>
      <td>413.0</td>
      <td>Natural gas</td>
      <td>Combined cycle</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>50.41396</td>
      <td>4.40645</td>
      <td>22WMARCIN000179H</td>
      <td>Fossil fuels</td>
      <td>Natural gas</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>https://www.elia.be/en/grid-data/power-generat...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aalst Syral GT</td>
      <td>Electrabel</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>BE</td>
      <td>43.0</td>
      <td>Natural gas</td>
      <td>Gas turbine</td>
      <td>Yes</td>
      <td>...</td>
      <td>CHP/IPP</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Fossil fuels</td>
      <td>Natural gas</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>https://www.elia.be/en/grid-data/power-generat...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Aalst Syral ST</td>
      <td>Electrabel</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>BE</td>
      <td>5.0</td>
      <td>Natural gas</td>
      <td>Steam turbine</td>
      <td>Yes</td>
      <td>...</td>
      <td>CHP/IPP</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Fossil fuels</td>
      <td>Natural gas</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>https://www.elia.be/en/grid-data/power-generat...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AALTER TJ</td>
      <td>Electrabel</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>BE</td>
      <td>18.0</td>
      <td>Oil</td>
      <td>Gas turbine</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Fossil fuels</td>
      <td>Oil</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>https://www.elia.be/en/grid-data/power-generat...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amercoeur 1 R TGV</td>
      <td>Electrabel</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>BE</td>
      <td>451.0</td>
      <td>Natural gas</td>
      <td>Combined cycle</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>50.43004</td>
      <td>4.39518</td>
      <td>22WAMERCO000010Y</td>
      <td>Fossil fuels</td>
      <td>Natural gas</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>https://www.elia.be/en/grid-data/power-generat...</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>



<br>

We'll save this to our raw data directory before continuing

```python
df_OPSD.to_csv('../data/raw/OPSD.csv', index=False)
```

<br>

We can see that there's roughly half the number of entries in the OPSD database for UK plants. However, its worth remembering that were ~2 entries per physcial location in the ESAIL dataset due to some plants having multiple BM units.

```python
df_OPSD_UK = df_OPSD.query('country=="UK"')

df_OPSD_UK.shape[0]
```




    244



<br>

Inspecting the break-down by fuel-type we start to see a slightly different picture though, where hydro takes the top spot and wind is no-where to be seen

```python
df_OPSD_UK['energy_source'].value_counts()
```




    Hydro                  130
    Natural gas             48
    Mixed fossil fuels      26
    Non-renewable waste     13
    Biomass and biogas      12
    Nuclear                  8
    Hard coal                7
    Name: energy_source, dtype: int64



<br>

Visualising this difference for just the Hydro plants shows us that the OPSD dataset has far more granular information on some of the smaller run-of-river hydro plants in Scotland, however they do miss some run-of-river such as Rheidol in Wales.

```python
df_OPSD_UK_hydro = df_OPSD_UK.query('energy_source=="Hydro"')
df_ESAIL_hydro = df_ESAIL.query('primary_fuel_type=="run_of_river" | primary_fuel_type=="pumped_storage"')

# Plotting
fig, axs = plt.subplots(figsize=(6, 5), dpi=250, ncols=2)

ax = axs[0]
ax.set_title(f'OPSD n={df_OPSD_UK_hydro.shape[0]}')
gdf_GSP_locs.to_crs('EPSG:4326').plot(ax=ax, alpha=0.3, edgecolor='w')
ax.scatter(df_OPSD_UK_hydro['lon'], df_OPSD_UK_hydro['lat'], s=2, alpha=1, color='green')

ax = axs[1]
ax.set_title(f'ESAIL n={df_ESAIL_hydro.shape[0]}')
gdf_GSP_locs.to_crs('EPSG:4326').plot(ax=ax, alpha=0.3, edgecolor='w')
ax.scatter(df_ESAIL_hydro['longitude'], df_ESAIL_hydro['latitude'], s=2, alpha=1, color='green')

for ax in axs:
    hlp.hide_spines(ax, positions=['top', 'bottom', 'left', 'right'])
    ax.set_xticks([])
    ax.set_yticks([])
```


![png](img/nbs/output_26_0.png)


<br>

We'll also look at the detail to which they go in for energy sources

```python
df_OPSD[['energy_source_level_1', 'energy_source_level_2', 'energy_source_level_3']].drop_duplicates()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>energy_source_level_1</th>
      <th>energy_source_level_2</th>
      <th>energy_source_level_3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Fossil fuels</td>
      <td>Natural gas</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Fossil fuels</td>
      <td>Oil</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Renewable energy</td>
      <td>Bioenergy</td>
      <td>Biomass and biogas</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Renewable energy</td>
      <td>Hydro</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Nuclear</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Fossil fuels</td>
      <td>Non-renewable waste</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Fossil fuels</td>
      <td>Mixed fossil fuels</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Fossil fuels</td>
      <td>Hard coal</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Other or unspecified energy sources</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>313</th>
      <td>Fossil fuels</td>
      <td>Lignite</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>538</th>
      <td>Renewable energy</td>
      <td>Bioenergy</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>Fossil fuels</td>
      <td>Other fossil fuels</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4792</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5962</th>
      <td>Other</td>
      <td>Other fuels</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6008</th>
      <td>Other or unspecified energy sources</td>
      <td>Waste</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



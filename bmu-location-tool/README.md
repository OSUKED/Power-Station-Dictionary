# BMU Location Manager

A browser-based tool for managing the UK power station dictionary dataset. It helps you find unmatched Balancing Mechanism Units (BMUs), assign them to power stations, add geographic coordinates, and export clean CSV data — all without any installation or build step.

---

## What It Does

UK electricity grid data contains two overlapping ID systems for power plant units:

- **BMUs (Balancing Mechanism Units)** — registered with Elexon/National Grid for settlement purposes
- **Power station dictionary entries** — a curated dataset that groups BMUs under named stations with geographic coordinates

Over time, new BMUs appear in Elexon's registry that don't yet have a matching entry in the station dictionary. This tool surfaces those unmatched BMUs and provides a workflow to:

1. Identify unmatched BMUs (those without a `dictionary_id`)
2. Group similar BMUs that likely belong to the same physical station
3. Auto-suggest REPD matches with one-click station creation
4. Assign BMUs to existing stations or create new station entries
5. Auto-fill coordinates using REPD (Renewable Energy Planning Database) fuzzy matching
6. Edit existing station records, coordinates, and fuel types directly
7. Export updated `ids.csv`, `plant-locations.csv`, and `fuel_types.csv` files

---

## Getting Started

No installation required. Open `bmu-location-tool.html` directly in Chrome or Firefox.

```
open bmu-location-tool.html
```

The app loads entirely in the browser. All data is session-only — nothing is written to disk until you export.

On startup, the app automatically fetches the latest BMU registry from the Elexon API. A spinner in the sidebar shows fetch progress.

---

## Loading Data

Use the file upload buttons in the left sidebar to load your data files. The app works with the files in the `data/` folder of this repository, as well as the Renewable Energy Planning Database provided by the UK Department for Energy Security and Net Zero (DESNZ).

### Required Files

| File | Description |
|------|-------------|
| `ids.csv` | Power Station Dictionary — maps `dictionary_id` to station names, ESAIL IDs, and BMU IDs |
| `plant-locations.csv` | Geographic coordinates — maps `dictionary_id` to `latitude` / `longitude` |

### Optional Files (enhance matching)

| File | Description |
|------|-------------|
| `REPD_Publication_*.csv` | Renewable Energy Planning Database — used for fuzzy name matching and auto-filling BNG coordinates |
| `common-names.csv` | Common name aliases for stations |
| `fuel_types.csv` | Fuel type overrides per NGC BMU ID |

A green dot next to each file button in the sidebar confirms it is loaded; the row count is shown next to it.

---

## Views

### Unmatched BMUs (default view)

Shows all BMUs from the Elexon registry that have no matching entry in `ids.csv`.

**Stats bar** at the top shows total unmatched, selected count, and a breakdown by fuel type.

**Fuel type filter pills** — click WIND, SOLAR, CCGT, BATTERY, etc. to narrow the list. Click ALL to reset.

**Search bar** — filters by BMU ID, unit name, lead party, or GSP group.

Each BMU row shows:
- National Grid and Elexon BMU IDs (monospace)
- Fuel type badge (colour-coded by technology)
- Unit name, lead party, GSP group, and generation capacity (where available)
- A checkbox for selection

**Select All** / **Deselect All** buttons operate on the current filtered view.

#### Auto-Suggested Matches (REPD inline suggestions)

When REPD data is loaded, the top of the unmatched view shows an **Inline Suggestions** panel. Each card represents a group of BMUs with a high-confidence REPD match:

- BMU group root ID and all grouped BMUs
- Matched REPD site name, operator, capacity, technology type, and development status
- Match score (percentage confidence)
- Derived WGS84 coordinates (converted from BNG)

Two action buttons per suggestion:
- **Quick Assign** — immediately creates a new station (or updates an existing one with the same ESAIL ID) using the REPD data. No form required.
- **Review & Edit** — pre-fills the full assignment form so you can inspect or adjust before saving.

If a suggestion duplicates an existing ESAIL ID in `ids.csv`, a yellow **Duplicate ESAIL** badge appears as a warning.

#### BMU Groups

Below the inline suggestions, the **Groups** section shows clusters of unmatched BMUs that share a common ID root (e.g. `MYST-1`, `MYST-2`, `MYST-3`) but have no auto-suggestion. A **Select All in Group** button selects the whole group at once so you can assign them together.

---

### Assigning BMUs to a Station

1. Select one or more BMUs using their checkboxes (or use a group's **Select All**)
2. Click **Assign Selected** to open the assignment panel
3. Choose **+ New Station** to create a new dictionary entry, or **Existing Station** to merge into a station already in `ids.csv`
4. Fill in the station details:
   - **Dictionary ID** — auto-assigned for new stations (next available integer)
   - **ESAIL ID** — short identifier used by Elexon/ESAIL systems (e.g. `DRAXX`)
   - **Station Name** — human-readable name
   - **Latitude / Longitude** — WGS84 decimal degrees
5. **REPD Matches panel** — if REPD data is loaded, fuzzy-matched candidates appear automatically. Click any REPD row to auto-fill the name and coordinates (converted from British National Grid). A **Manual search** field lets you search REPD by site name, operator, or ref ID.
6. **Fuel Type Assignment** — choose between:
   - **Simple mode**: one fuel type for all BMUs in this assignment
   - **Advanced mode**: per-BMU fuel type override (auto-enabled when mixed types are detected; shows each NGC BMU ID with an individual dropdown)
7. Click **Create Station & Save** (new) or **Update Station & Save** (existing)

All changes are tracked in the **Change Log** at the bottom of the sidebar, showing station name, dictionary ID, coordinates, and BMU count for each save.

#### Existing Station Picker

Selecting **Existing Station** shows a searchable list of all stations from `ids.csv`. Green dots indicate stations with coordinates; red dots indicate those without. Click a station to pre-fill the form with its current data and merge the selected BMUs in.

---

### All Stations View

Browse every station in `ids.csv`. Search by name, dictionary ID, ESAIL ID, or BMU ID. Station count shown at the top right.

Each row shows:
- Location indicator (green = has coordinates, red = missing)
- Station name and any common name alias
- Dictionary ID, ESAIL ID, BMU count, and coordinates

Click any row to open the **Edit Station** panel.

---

### Edit Station Panel

Edit an existing station's details:
- Station name and ESAIL ID
- Latitude and longitude
- Settlement BMU IDs (comma-separated)
- NGC BMU IDs (comma-separated)

A **Search BMU JSON** section lets you type a unit name, ID, or lead party to find BMUs from the Elexon registry and add them directly with the **+ Add** button.

---

### Data Editor View

A spreadsheet-style editor with three sub-tabs:

#### Stations tab

Inline editing for every station in `ids.csv`. Filter by:
- **All** — full list
- **No Location** — stations missing a coordinate entry (count shown in the button)
- **No ESAIL** — stations with an empty ESAIL ID

Click any row to expand it and edit: name, ESAIL ID, common name (if `common-names.csv` loaded), fuel type (if `fuel_types.csv` loaded), latitude, longitude, and both BMU ID fields. A **Delete** button with a confirmation step is also available.

#### Locations tab

Inline editing for every row in `plant-locations.csv`. Flags orphaned entries — location rows whose `dictionary_id` has no matching station in `ids.csv`. Click any row to edit latitude and longitude, or delete the row.

#### BMU Fuel Types tab

A per-BMU fuel type editor for all NGC BMU IDs across all stations.

- **Elexon** column shows the fuel type from the Elexon registry (read-only reference)
- **Override dropdown** lets you set a saved fuel type in `fuel_types.csv`; unsaved changes are highlighted in amber
- **Suggested** chip appears when the BMU name contains a keyword (e.g. WIND, SOLAR, BATTERY) that implies a different type — click the chip to apply it
- Hovering a BMU ID shows a tooltip with unit name, operator, GSP group, and capacity
- **Mixed** badge on a station row when its BMU IDs have different fuel types
- Quick filters: **MIXED** (stations with inconsistent types), **Showing Elexon default only** (no override saved), **With name-based suggestion** (keyword-implied type differs from current)
- Each row has a **Save** button that appears only when a pending edit exists

---

### Fill Missing ESAIL IDs

Accessible via the sidebar when `ids.csv` is loaded. The app identifies stations where all BMU IDs share the same root (e.g. `MARK-1`, `MARK-2` → root `MARK`) and suggests that root as the ESAIL ID.

Each suggestion shows the station name, all its BMU IDs, and an editable suggested value. Use **Apply** per-station or **Apply All** to batch-update all suggestions at once.

---

## Exporting

Once you've made your changes, export updated files using the buttons in the sidebar:

- **Export ids.csv** — downloads the full updated station dictionary
- **Export plant-locations.csv** — downloads the full updated coordinates file
- **Export fuel_types.csv** — downloads the full updated per-BMU fuel type overrides (visible after any fuel type has been loaded or modified)

Replace the corresponding files in the 'data' folder with the downloaded versions to persist your changes.

---

## Data File Formats

### `ids.csv`

```
dictionary_id,esail_id,name,sett_bmu_id,ngc_bmu_id,...
10000,MARK,Rothes Bio-Plant CHP,"E_MARK-1, E_MARK-2","MARK-1, MARK-2",...
```

Key columns: `dictionary_id` (integer), `esail_id`, `name`, `sett_bmu_id` (Elexon settlement IDs, comma-separated), `ngc_bmu_id` (National Grid IDs, comma-separated).

### `plant-locations.csv`

```
dictionary_id,longitude,latitude
10000,-3.603516,57.480403
```

### `bmu_data.json`

Array of objects from the Elexon API. Key fields: `elexonBmUnit`, `nationalGridBmUnit`, `bmUnitName`, `fuelType`, `leadPartyName`, `gspGroupName`, `generationCapacity`.

### `fuel_types.csv`

```
ngc_bmu_id,fuel_type,comments
MARK-1,BIOMASS,
```

Maps individual NGC BMU IDs to fuel type overrides. Overrides take priority over the Elexon-reported type.

### `common-names.csv`

```
dictionary_id,common_name
10000,Rothes
```

Short aliases displayed alongside station names throughout the app.

---

## Technical Notes

- **No build step** — the app is a single HTML file using React 18 (CDN) and Babel Standalone for in-browser JSX compilation
- **No data is sent anywhere** — all processing happens locally in the browser; the only outbound request is the Elexon API fetch on startup
- **Coordinate conversion** — British National Grid (BNG) eastings/northings from REPD are converted to WGS84 lat/lon using the Ordnance Survey algorithm
- **Fuzzy matching** — station names are matched against REPD using a combination of bigram similarity, word-level recall scoring, fuel type hinting, and substring matching; withdrawn/refused/abandoned REPD entries are deprioritised automatically
- **Fuel type resolution priority**: `fuel_types.csv` override → Elexon registry → BMU name keyword scan → REPD Technology Type

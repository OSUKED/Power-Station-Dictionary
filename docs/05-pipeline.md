# End-to-End Pipeline



```python
#exports
from powerdict import download, construct, update

import os
from typing import Any

from dagster import execute_pipeline, pipeline, solid, Field
```

<br>

### Dagster Pipeline

We're now going to combine the dictionary generation steps into a pipeline using dagster, first we'll create the individual components.

```python
#exports
@solid()
def download_source_data(_, raw_data_dir: str):
    download.download_opsd_power_plants_data(raw_data_dir)
    
    return 

@solid()
def construct_intermediate_dataset(_, definitions_dir: str, raw_data_dir: str, intermediate_data_dir: str) -> Any:
    df = construct.construct_output_df(definitions_dir, raw_data_dir)
    df.to_csv(f'{intermediate_data_dir}/power_stations.csv')
    
    return df

@solid()
def update_dataset_updates(_, df: Any, updates_data_dir: str) -> Any:
    df = update.apply_updates(df, updates_data_dir)
    
    return df

@solid()
def clean_output_dataset(_, df: Any, definitions_dir: str) -> Any:
    df = update.check_and_apply_output_defs(df, definitions_dir)
    
    return df

@solid()
def save_output_dataset(_, df: Any, output_data_dir: str):
    if not os.path.exists(output_data_dir):
        os.makedirs(output_data_dir)
        
    df.to_csv(f'{output_data_dir}/power_stations.csv')
    
    return
```

<br>

Then we'll combine them in a pipeline

```python
#exports
@pipeline
def generate_output_dataset_pipeline():  
    download_source_data()
    
    df = construct_intermediate_dataset()
    df = update_dataset_updates(df)
    df = clean_output_dataset(df)
    
    save_output_dataset(df)
```

<br>

Which we can then run with `execute_pipeline` whilst also specifying the run_config 

```python
run_config = {
    'solids': {
        'download_source_data': {
            'inputs': {
                'raw_data_dir': '../data/raw'
            },
        },
        'construct_intermediate_dataset': {
            'inputs': {
                'definitions_dir': '../data/definitions',
                'raw_data_dir': '../data/raw',
                'intermediate_data_dir': '../data/intermediate'
            },
        },
        'update_dataset_updates': {
            'inputs': {
                'updates_data_dir': '../data/updates'
            },
        },
        'clean_output_dataset': {
            'inputs': {
                'definitions_dir': '../data/definitions'
            },
        },
        'save_output_dataset': {
            'inputs': {
                'output_data_dir': '../data/output'
            },
        },
    }
}

execute_pipeline(generate_output_dataset_pipeline, run_config=run_config)
```

    [32m2020-12-18 14:38:01[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - ENGINE_EVENT - Starting initialization of resources [asset_store].
    [32m2020-12-18 14:38:01[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - ENGINE_EVENT - Finished initialization of resources [asset_store].
    [32m2020-12-18 14:38:01[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - PIPELINE_START - Started execution of pipeline "generate_output_dataset_pipeline".
    [32m2020-12-18 14:38:01[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - ENGINE_EVENT - Executing steps in process (pid: 23064)
    [32m2020-12-18 14:38:01[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - construct_intermediate_dataset.compute - STEP_START - Started execution of step "construct_intermediate_dataset.compute".
    [32m2020-12-18 14:38:01[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - construct_intermediate_dataset.compute - STEP_INPUT - Got input "definitions_dir" of type "String". (Type check passed).
    [32m2020-12-18 14:38:01[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - construct_intermediate_dataset.compute - STEP_INPUT - Got input "raw_data_dir" of type "String". (Type check passed).
    [32m2020-12-18 14:38:01[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - construct_intermediate_dataset.compute - STEP_INPUT - Got input "intermediate_data_dir" of type "String". (Type check passed).
    [32m2020-12-18 14:38:01[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - construct_intermediate_dataset.compute - STEP_OUTPUT - Yielded output "result" of type "Any". (Type check passed).
    [32m2020-12-18 14:38:01[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - construct_intermediate_dataset.compute - OBJECT_STORE_OPERATION - Stored intermediate object for output result in memory object store using pickle.
    [32m2020-12-18 14:38:01[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - construct_intermediate_dataset.compute - STEP_SUCCESS - Finished execution of step "construct_intermediate_dataset.compute" in 196ms.
    [32m2020-12-18 14:38:01[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - download_source_data.compute - STEP_START - Started execution of step "download_source_data.compute".
    [32m2020-12-18 14:38:01[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - download_source_data.compute - STEP_INPUT - Got input "raw_data_dir" of type "String". (Type check passed).
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - download_source_data.compute - STEP_OUTPUT - Yielded output "result" of type "Any". (Type check passed).
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - download_source_data.compute - OBJECT_STORE_OPERATION - Stored intermediate object for output result in memory object store using pickle.
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - download_source_data.compute - STEP_SUCCESS - Finished execution of step "download_source_data.compute" in 1.02s.
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - update_dataset_updates.compute - STEP_START - Started execution of step "update_dataset_updates.compute".
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - update_dataset_updates.compute - OBJECT_STORE_OPERATION - Retrieved intermediate object for input df in memory object store using pickle.
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - update_dataset_updates.compute - STEP_INPUT - Got input "df" of type "Any". (Type check passed).
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - update_dataset_updates.compute - STEP_INPUT - Got input "updates_data_dir" of type "String". (Type check passed).
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - update_dataset_updates.compute - STEP_OUTPUT - Yielded output "result" of type "Any". (Type check passed).
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - update_dataset_updates.compute - OBJECT_STORE_OPERATION - Stored intermediate object for output result in memory object store using pickle.
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - update_dataset_updates.compute - STEP_SUCCESS - Finished execution of step "update_dataset_updates.compute" in 5.94ms.
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - clean_output_dataset.compute - STEP_START - Started execution of step "clean_output_dataset.compute".
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - clean_output_dataset.compute - OBJECT_STORE_OPERATION - Retrieved intermediate object for input df in memory object store using pickle.
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - clean_output_dataset.compute - STEP_INPUT - Got input "df" of type "Any". (Type check passed).
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - clean_output_dataset.compute - STEP_INPUT - Got input "definitions_dir" of type "String". (Type check passed).
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - clean_output_dataset.compute - STEP_OUTPUT - Yielded output "result" of type "Any". (Type check passed).
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - clean_output_dataset.compute - OBJECT_STORE_OPERATION - Stored intermediate object for output result in memory object store using pickle.
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - clean_output_dataset.compute - STEP_SUCCESS - Finished execution of step "clean_output_dataset.compute" in 4.9ms.
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - save_output_dataset.compute - STEP_START - Started execution of step "save_output_dataset.compute".
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - save_output_dataset.compute - OBJECT_STORE_OPERATION - Retrieved intermediate object for input df in memory object store using pickle.
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - save_output_dataset.compute - STEP_INPUT - Got input "df" of type "Any". (Type check passed).
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - save_output_dataset.compute - STEP_INPUT - Got input "output_data_dir" of type "String". (Type check passed).
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - save_output_dataset.compute - STEP_OUTPUT - Yielded output "result" of type "Any". (Type check passed).
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - save_output_dataset.compute - OBJECT_STORE_OPERATION - Stored intermediate object for output result in memory object store using pickle.
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - save_output_dataset.compute - STEP_SUCCESS - Finished execution of step "save_output_dataset.compute" in 7.25ms.
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - ENGINE_EVENT - Finished steps in process (pid: 23064) in 1.27s
    [32m2020-12-18 14:38:02[0m - dagster - [34mDEBUG[0m - generate_output_dataset_pipeline - c2197f8e-bb11-4d57-8ced-c5a3d2a9d9dd - 23064 - PIPELINE_SUCCESS - Finished execution of pipeline "generate_output_dataset_pipeline".
    




    <dagster.core.execution.results.PipelineExecutionResult at 0x1f33bf5afd0>



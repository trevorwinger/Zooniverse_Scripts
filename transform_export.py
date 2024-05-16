import pandas as pd 
import json
from tqdm.auto import tqdm


df = pd.read_csv('./measuring-the-anzacs-classifications.csv')

# Assuming df is your original DataFrame
# Step 1: Filter the DataFrame
columns_of_interest = ['classification_id', 'user_name', 'workflow_name', 'workflow_version', 'annotations', 'subject_ids']
filtered_df = df[columns_of_interest]

# Step 2: Create separate DataFrames for each workflow_name
workflow_dfs = {name: group for name, group in filtered_df.groupby('workflow_name')}

# Function to handle nested tasks
def process_nested_tasks(task, task_label, value, row):
    if isinstance(value, list):
        for item in value:
            # Check if 'select_label' is present
            if 'select_label' in item:
                column_name = f"{task}_{item['select_label'].replace(' ', '_')}"
                row[column_name] = item.get('label', '')
            else:
                nested_task = item.get('task', '')
                nested_value = item.get('value', '')
                nested_task_label = item.get('label', '').replace(' ', '_')
                process_nested_tasks(nested_task, nested_task_label, nested_value, row)
    else:
        column_name = f"{task}_{task_label}"
        row[column_name] = value

# Step 3: Transform the annotations column
def transform_annotations(row):
    # Load the annotations JSON
    annotations = json.loads(row['annotations'])

    # Extract each task into a separate column
    for annotation in annotations:
        task = annotation['task']
        task_label = annotation.get('task_label', 'null')  # Check for NoneType
        task_label = 'null' if task_label is None else task_label.replace(" ", "_")
        value = annotation['value']

        # Process the task
        process_nested_tasks(task, task_label, value, row)

    return row

# Apply the transformation to each workflow DataFrame
for workflow_name, df in tqdm(workflow_dfs.items(), desc="Processing workflows"):
    tqdm.pandas(desc=f"Transforming {workflow_name}")
    workflow_dfs[workflow_name] = df.progress_apply(transform_annotations, axis=1)

    # Drop the original annotations column as it's no longer needed
    workflow_dfs[workflow_name].drop(columns=['annotations'], inplace=True)

# Save the DataFrames to CSV files
for workflow_name, df in tqdm(workflow_dfs.items(), desc="Saving CSV files"):
    file_name = workflow_name.replace(" ", "_") + ".csv"
    df.to_csv(file_name, index=False)
import os
from datasets import load_dataset
from tqdm.auto import tqdm

folder_path = "path to the text files folder"
parquet_path = "path where the parquet files will be saved"
prefix = folder_path.rstrip('/').split('/')[-1]

# Get all the filenames sorted to ensure order
filenames = sorted([f for f in os.listdir(folder_path) if f.endswith('.txt')])

# Define the batch size (number of files per batch)
batch_size = 100000

# Function to process and save a batch of filenames to parquet
def process_and_save_batch(filenames_batch, batch_index, parquet_path, prefix):
    # Load the batch using load_dataset
    batch_dataset = load_dataset(
        "text",
        data_files=[os.path.join(folder_path, f) for f in filenames_batch],
        split='train', sample_by='document'
    ).add_column("name", filenames_batch)  # Add the filename column

    # Save the batch to a parquet file
    chunk_path = os.path.join(parquet_path, f"{prefix}_{batch_index}.parquet")
    batch_dataset.to_parquet(chunk_path)

# Calculate the number of batches
num_batches = len(filenames) // batch_size + (len(filenames) % batch_size > 0)

# Ensure the parquet directory exists
os.makedirs(parquet_path, exist_ok=True)

# Process each batch using tqdm for progress visualization
for batch_index in tqdm(range(num_batches), desc="Processing batches"):
    start_index = batch_index * batch_size
    end_index = start_index + batch_size
    filenames_batch = filenames[start_index:end_index]
    process_and_save_batch(filenames_batch, batch_index, parquet_path, prefix)

print("All batches have been processed and saved to parquet files.")

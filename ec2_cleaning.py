import boto3
import numpy as np
from indusnlp.cleaning import Cleaning
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Parameters
bucket = 'finalannotated'
checkpoint_file = 'checkpoint.txt'
tasks_file = 'tasks.npy'
batch_size = 50

def get_s3_client():
    return boto3.client('s3')

def download_from_s3(input_key):
    s3 = get_s3_client()
    try:
        response = s3.get_object(Bucket=bucket, Key=input_key)
        return response['Body'].read().decode('utf-8')
    except Exception as e:
        logger.error(f"Failed to download {input_key}: {e}")
        return None

def upload_to_s3(output_key, cleaned_text):
    s3 = get_s3_client()
    try:
        s3.put_object(Bucket=bucket, Key=output_key, Body=cleaned_text)
    except Exception as e:
        logger.error(f"Failed to upload {output_key}: {e}")
        return False
    return True

def clean_text(text):
    try:
        cleaner = Cleaning()
        return cleaner.clean_text(text)
    except Exception as e:
        logger.error(f"Failed to clean text: {e}")
        return None

def clean_text_file(input_key):
    text = download_from_s3(input_key)
    if text is None:
        return False

    cleaned_text = clean_text(text)
    if cleaned_text is None:
        return False

    output_key = input_key.replace('Input/', 'Cleaned/', 1)
    if upload_to_s3(output_key, cleaned_text):
        logger.info(f'Cleaned file {input_key} and saved to {output_key}')
        return True
    return False

def load_tasks():
    if os.path.exists(tasks_file):
        return np.load(tasks_file, allow_pickle=True).tolist()
    else:
        logger.warning(f"No tasks file found at {tasks_file}")
        return []

def load_checkpoint():
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, 'r') as f:
            return int(f.read().strip())
    else:
        return 0

def update_checkpoint(index):
    with open(checkpoint_file, 'w') as f:
        f.write(str(index))

def process_batch(start_index, tasks):
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(clean_text_file, task): task for task in tasks[start_index:start_index+batch_size]}
        for future in as_completed(futures):
            task = futures[future]
            if future.result():
                update_checkpoint(start_index + tasks.index(task) + 1)
            else:
                logger.error(f"Task {task} failed.")

def main():
    tasks = load_tasks()
    if not tasks:
        return

    checkpoint_index = load_checkpoint()
    
    while checkpoint_index < len(tasks):
        logger.info(f"Processing tasks starting from index {checkpoint_index}")
        process_batch(checkpoint_index, tasks)
        checkpoint_index = load_checkpoint()

    logger.info("Processing complete.")

if __name__ == '__main__':
    main()

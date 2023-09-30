import boto3
from indusnlp.cleaning import Cleaning

s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    try:
        # Get the object from the event
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        # Download the file from S3
        file_obj = s3.get_object(Bucket=bucket, Key=key)
        file_content = file_obj['Body'].read().decode('utf-8')
        
        # Clean the text
        cleaner = Cleaning()
        cleaned_text = cleaner.clean_text(file_content)
        
        # Determine the new key for cleaned text
        cleaned_key = key.replace('Input', 'Cleaned', 1)
        
        # Upload cleaned text to S3
        s3.put_object(Bucket=bucket, Key=cleaned_key, Body=cleaned_text)
        
    except Exception as e:
        sns.publish(
            TopicArn='arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:TextCleaningErrors',
            Message=str(e),
            Subject='Text Cleaning Error'
        )
        raise

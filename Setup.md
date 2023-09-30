# Setup Instructions

## Step 1: AWS Setup

- Make sure you have an AWS account and AWS CLI installed and configured on your local machine.
- Create an S3 bucket or use an existing one. For this guide, let's assume the bucket name is `bucketname`.

## Step 2: Create IAM Role

- Navigate to the IAM console in AWS.
- Create a new role for AWS Lambda with permissions to read from and write to S3, publish to SNS, and access to CloudWatch for logging.

## Step 3: Create Lambda Function

- Navigate to the Lambda console and create a new function named `TextCleaningLambda`.
- Use the following code snippet as a reference for your Lambda function. Make sure to replace `"YOUR_BUCKET_NAME"` with `bucketname` and adjust the cleaning function as needed:

## Step 4: Configure S3 Event Notifications

- Go to the S3 console, navigate to the `bucketname` bucket, and select the `Properties` tab.
- Under `Event Notifications`, create a new event notification.
- Select `All object create events` and specify the prefix `Input/` to filter for new files in the `Input` folder.
- Set the Lambda function `TextCleaningLambda` as the destination.

## Step 5: Create SNS Topic (For Error Notifications)

- Navigate to the SNS console and create a new topic named `TextCleaningErrors`.
- Update the `TopicArn` in the Lambda function code with the ARN of the new SNS topic.
- Optionally, subscribe your email to the SNS topic to receive error notifications.

## Step 6: Testing

- Upload a few text files to the `Input` folder in the `bucketname` bucket to trigger the Lambda function.
- Check the `Cleaned` folder to ensure the cleaned text files are being saved correctly.
- Monitor the Lambda function executions in the CloudWatch console and check for any error notifications in the SNS topic.

## Step 7: Optimization

- If necessary, adjust the memory and timeout settings of the Lambda function to better match the requirements of the text cleaning process.
- Review the logs in CloudWatch to identify any potential bottlenecks or errors and adjust the Lambda function code as needed.

This setup provides a fully automated, serverless workflow for cleaning and organizing text files in your S3 bucket. Remember to replace placeholder values in the code and AWS configurations with your actual values.

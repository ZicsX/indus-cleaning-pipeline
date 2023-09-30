# 1. **Text-Cleaning Workflow**

In this architecture, we'll utilize AWS Lambda, AWS Step Functions, and AWS SNS (Simple Notification Service) to build a scalable, automated text-cleaning workflow. The IndusNLP toolkit will be incorporated into a Lambda function which will be triggered by new text files uploaded to the `Input` folder in the S3 bucket. Post-cleaning, the processed files will be saved in the `Cleaned` folder while maintaining the original folder structure.

1. **Triggering Mechanism**:
   - Utilize S3 Event Notifications to trigger a Lambda function whenever a new text file is uploaded to the `Input` folder or any of its subfolders.

2. **Lambda Function (Text Cleaning)**:
   - The triggered Lambda function, let’s call it `TextCleaningLambda`, will:
      - Read the newly uploaded text file from the S3 `Input` folder.
      - Import and utilize the IndusNLP cleaning toolkit (`indusnlp.cleaning`) to clean the text content.
      - Save the cleaned text to the corresponding location within the `Cleaned` folder, replicating the original folder structure.
      - Save the cleaned text to the corresponding location within the `Cleaned` folder, replicating the original folder structure.

3. **Error Handling**:
   - If the Lambda function encounters an error (e.g., unable to read the file, toolkit malfunction, etc.), it will publish an error message to an SNS topic.

4. **Monitoring and Notifications**:
   - Subscribe to the SNS topic to receive error notifications for prompt troubleshooting.
   - Use AWS CloudWatch to monitor the executions of the Lambda function and to set up alarms for any unusual activities.

5. **Step Function Orchestration (Optional)**:
   - If there are additional steps or dependencies in the cleaning process, AWS Step Functions can be utilized to orchestrate the workflow. For example, if a subsequent processing step is required post-cleaning.

6. **Access Control and Security**:
   - Utilize AWS IAM (Identity and Access Management) to control access to the S3 bucket, Lambda function, and other resources.
   - Ensure that the Lambda function has the necessary permissions to read from the `Input` folder, write to the `Cleaned` folder, and publish to the SNS topic.

7. **Optimization**:
   - Optimize the memory and timeout settings of the Lambda function to ensure efficient processing of the text files.
   - If the volume of text files is significant, consider increasing the concurrency limit of the Lambda function to handle multiple files simultaneously.

8. **Logging**:
   - Implement logging within the `TextCleaningLambda` function to capture important events and any potential errors.
   - Store logs in AWS CloudWatch for easy access and analysis.

9. **Testing and Validation**:
   - Initially, test the setup with a small number of text files to validate the workflow.
   - Confirm that the cleaned text files are correctly saved in the `Cleaned` folder with the original folder structure.

This architecture leverages AWS’s serverless capabilities to automate the text-cleaning process efficiently and ensure that the cleaned text files are accurately organized in the `Cleaned` folder within the S3 bucket.
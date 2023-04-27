# Uploading Log File to Amazon S3 using AWS Lambda
We have chosen AWS Lambda over AWS CLI to upload a file from a remote URL to an Amazon S3 bucket because Lambda allows for better scalability, easier management, and automation using Amazon EventBridge for periodic tasks.

### Deploying and Running the Lambda Function using AWS CLI

Here's a step-by-step guide on how to deploy and run the Lambda function using AWS CLI:

1. Create a ZIP archive of the `lambda_package` folder:

   ```bash
   cd lambda_package/
   zip -r ../lambda_package.zip .
   cd ..
   ```

2. Create an IAM role for the Lambda function and attach the necessary policies: [guide](https://repost.aws/knowledge-center/lambda-execution-role-s3-bucket).
3. Create a Lambda function using the AWS CLI, replacing `ROLE_ARN` with the ARN of the IAM role created in the previous step:

   ```bash
   aws lambda create-function \
       --function-name UploadLogFile \
       --runtime python3.10 \
       --role ROLE_ARN \
       --handler lambda_function.lambda_handler \
       --zip-file fileb://lambda_upload_logs.zip
   ```

4. Set the environment variables for the Lambda function:

   ```bash
   aws lambda update-function-configuration \
       --function-name UploadLogFile \
       --environment "Variables={URL=http://www.almhuette-raith.at/apache-log/access.log, BUCKET_NAME=epikast, S3_KEY=access.log}"
   ```

5. Invoke the Lambda function using the AWS CLI:

   ```bash
   aws lambda invoke \
       --function-name UploadLogFile \
       --payload '{}' \
       output.txt
   ```

   Check the `output.txt` file for the function's output.

### Monitoring with Amazon CloudWatch

Amazon CloudWatch is automatically integrated with AWS Lambda to monitor and log your function's activities.
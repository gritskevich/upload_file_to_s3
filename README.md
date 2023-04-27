# AWS S3 Log File Storage Guide

---

Please check this [README](script/README.md) to upload via Python script

---

Please check this [README](lambda_package/README.md) for instructions to use AWS Lambda

---

This guide will help you set up the AWS CLI, create an S3 bucket, set a read-only policy, fetch a publicly available log
file, and store it in the S3 bucket using the AWS CLI.

### Step 1: Set up AWS CLI

1. Download and install the AWS CLI for your operating system:
2. Verify the installation by running `aws --version` in your command line or terminal. You should see the version
   number of your installed AWS CLI.
3. Configure the AWS CLI by running `aws configure`. You will be prompted to provide your AWS Access Key ID, Secret
   Access Key, default region name, and default output format. Enter the corresponding values, and set the default
   region as "us-east-2".

### Step 2: Create an S3 bucket using AWS CLI

1. Run the following command to create a new S3 bucket named "epikast" in the "us-east-2" region:
   ```
   aws s3 mb s3://epikast --region us-east-2
   ```

### Step 3: Set a read-only policy using AWS CLI

1. Create a JSON file, named "read-only-policy.json", with the following content:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "PublicRead",
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::epikast/*"
       }
     ]
   }
   ```
2. Run the following command to unblock public access to the "epikast" bucket:
   ```
   aws s3api put-public-access-block --bucket epikast --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"
   ```
3. Run the following command to apply the read-only policy to the "epikast" bucket:
   ```
   aws s3api put-bucket-policy --bucket epikast --policy file://aws_policy/read-only-policy.json
   ```

### Step 4: Fetch a publicly available log file and store it in the S3 bucket

1. Download the log file:
   ```
   curl http://www.almhuette-raith.at/apache-log/access.log -o access.log
   ```
2. Upload the log file to the "epikast" bucket:
   ```
   aws s3 cp access.log s3://epikast/access.log
   ```

### Step 5: Provide the URL to the S3 bucket with the transferred log file

1. The URL to access the log file in the "epikast" S3 bucket will be:
   ```
   https://epikast.s3.us-east-2.amazonaws.com/access.log
   ```

You can now access the log file using the provided URL.
# Serverless-Architecture:
# Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3
- ## Create several S3 buckets:
### Created 2 s3 buckets
<img width="1869" height="565" alt="image" src="https://github.com/user-attachments/assets/a14f5466-5132-4e95-90a8-823d2d805a04" />

- ## Lambda IAM Role:
<img width="1896" height="805" alt="image" src="https://github.com/user-attachments/assets/87899ef8-0cb6-4db3-8e24-a101baf73dc9" />

- ## Create a Lambda function.
<img width="1652" height="881" alt="image" src="https://github.com/user-attachments/assets/9900c411-5646-462f-a2b7-e7cf0dd9a854" />
<img width="1827" height="521" alt="image" src="https://github.com/user-attachments/assets/844cee97-41f4-4b82-84a4-c76961a737ba" />

- ### Write the Boto3 Python script to:
______________________________________


```

import boto3

s3 = boto3.client("s3")


def lambda_handler(event, context):

    response = s3.list_buckets()

    unencrypted_buckets = []

    for bucket in response["Buckets"]:
        bucket_name = bucket["Name"]

        try:
            encryption = s3.get_bucket_encryption(
                Bucket=bucket_name
            )

            rules = encryption["ServerSideEncryptionConfiguration"]["Rules"]

            if rules:
                print(f"[ENCRYPTED] {bucket_name}")
            else:
                print(f"[NO ENCRYPTION] {bucket_name}")
                unencrypted_buckets.append(bucket_name)

        except s3.exceptions.ClientError:
            print(f"[NO ENCRYPTION CONFIGURATION] {bucket_name}")
            unencrypted_buckets.append(bucket_name)

    print("\nBuckets without detected encryption configuration:")

    for bucket in unencrypted_buckets:
        print(bucket)

    return {
        "statusCode": 200,
        "unencrypted_buckets": unencrypted_buckets
    }

```
<img width="1822" height="912" alt="image" src="https://github.com/user-attachments/assets/bb231417-88d4-4a35-99c0-26f8ed83354e" />

- ### Test Lambda Function:
<img width="715" height="592" alt="image" src="https://github.com/user-attachments/assets/c9a98458-5437-47d1-8e6f-a5f3152cd376" />

- ## List all buckets.
<img width="637" height="541" alt="image" src="https://github.com/user-attachments/assets/b03fbe7f-1910-48a2-a7f0-b83a62c06416" />

- ## Detect buckets without encryption and print their names in the Lambda logs.
<img width="1887" height="922" alt="image" src="https://github.com/user-attachments/assets/b74241ff-0939-48ec-9c45-9bca12f8b190" />

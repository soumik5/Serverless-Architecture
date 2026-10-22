## Assignment 2: Automated S3 Bucket Cleanup Using Lambda and Boto3.
### Task: Create a Lambda function that will automatically Delete s3 object.   

1. Setup:
   - Create s3 bucket.
   <br><br>
   <img width="1918" height="861" alt="image" src="https://github.com/user-attachments/assets/7d6d66c2-f601-4ad5-9f05-892e481ef66e" />
   <img width="1905" height="662" alt="image" src="https://github.com/user-attachments/assets/affa9f04-cfea-41e1-8e2d-0a40dd1f890b" />
   <img width="1918" height="627" alt="image" src="https://github.com/user-attachments/assets/05fa4237-db1b-48cc-9c80-9c0f54db80f5" />
   <br><br>

2. Screenshot after uploading 2–3 test files.
   <img width="1910" height="500" alt="image" src="https://github.com/user-attachments/assets/ae088be5-226d-4af1-8e6f-7bf18a2a170f" />

3. Create/ Update IAM Role (Lambda-ab)
   <img width="1917" height="888" alt="image" src="https://github.com/user-attachments/assets/b38fe642-9357-4051-ae6c-c913a37f3080" />

   
4. Lambda Function Creation:
   - Set up an AWS Lambda function.
  
   <br><br>
   <img width="1908" height="965" alt="image" src="https://github.com/user-attachments/assets/513ac2d1-3a7f-4084-8091-a38e5ee8c89d" />
   <br><br>
   
   - Ensure that the Lambda function has the necessary IAM permissions to describe, stop, and start EC2 instances.

5. Coding:
   - Using Boto3 in the Lambda function:

    ```    
    import boto3
    from datetime import datetime, timezone, timedelta
    
    s3 = boto3.client('s3')
    
    BUCKET_NAME = 'abhash-lambda-s3-2026'
    
    def lambda_handler(event, context):

        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    
        if 'Contents' not in response:
            print("Bucket is empty")
            return
    
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=30)
    
        deleted_files = []
    
        for obj in response['Contents']:
    
            if obj['LastModified'] < cutoff_date:
    
                s3.delete_object(
                    Bucket=BUCKET_NAME,
                    Key=obj['Key']
                )
    
                deleted_files.append(obj['Key'])
    
                print(f"Deleted: {obj['Key']}")
    
        print("Deleted Files:", deleted_files)
    
        return {
            "statusCode": 200,
            "deleted_files": deleted_files
        }        
    ```

   <br><br>
   <img width="1908" height="852" alt="image" src="https://github.com/user-attachments/assets/61acc2e9-c5dd-4d23-8d72-9c3d965928c9" />
   <br><br>

6. Deply and testing:

   - Manually invoke the Lambda function.
    <br><br>
    <img width="1915" height="925" alt="image" src="https://github.com/user-attachments/assets/9e7fd332-c21a-4c47-8aef-1b705ed4804b" />

    <br><br>

7. Confirm that the s3 object is delted successfully.
     <br><br>
      - Befre Delete
        
      - <img width="1915" height="925" alt="image" src="https://github.com/user-attachments/assets/2cef84e6-8a69-4d2b-a41a-2c9c59dd6be1" />

      - After Delete
    
      - <img width="1918" height="577" alt="image" src="https://github.com/user-attachments/assets/59747c98-ae33-4a09-af30-abfcb2536e97" /> 
     <br><br>

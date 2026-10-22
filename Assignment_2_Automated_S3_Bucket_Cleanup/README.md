## Assignment 2: Automated S3 Bucket Cleanup Using Lambda and Boto3.
### Task: Create a Lambda function that will automatically Delete s3 object.   

1. Setup:
   - Create s3 bucket.
   <br><br>

   <img width="1841" height="890" alt="image" src="https://github.com/user-attachments/assets/16c31d56-5006-4bd7-b856-81b7546b084d" />
   <img width="1842" height="937" alt="image" src="https://github.com/user-attachments/assets/2396685f-4f75-44da-bea5-7b79324f2794" />

   <img width="1811" height="627" alt="image" src="https://github.com/user-attachments/assets/9460bfc8-8f75-4c6a-abf2-826485a85cec" />

   <br><br>

2. Screenshot after uploading 2–3 test files.
  <img width="1851" height="780" alt="image" src="https://github.com/user-attachments/assets/201c69de-707d-444f-aa28-8058e3c3165b" />


3. Create/ Update IAM Role (Lambda-ab)
   <img width="1895" height="779" alt="image" src="https://github.com/user-attachments/assets/ddb62c18-75a1-4fa2-ad95-6cc21912000d" />


   
4. Lambda Function Creation:
   - Set up an AWS Lambda function.
  
   <br><br>
  <img width="1900" height="811" alt="image" src="https://github.com/user-attachments/assets/484136ce-9955-4be4-a4e4-f349fab0036c" />

   <br><br>
   
   - Ensure that the Lambda function has the necessary IAM permissions to describe, stop, and start EC2 instances.

5. Coding:
   - Using Boto3 in the Lambda function:

    ```    
    import boto3
    from datetime import datetime, timezone, timedelta
    
    s3 = boto3.client('s3')
    
    BUCKET_NAME = 'soumik-lambda-s3-2026'
    
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
   <img width="1797" height="890" alt="image" src="https://github.com/user-attachments/assets/89f172a0-6999-4757-bbfc-3f888cca7dcf" />

   <br><br>

6. Deply and testing:

   - Manually invoke the Lambda function.
    <br><br>
   <img width="1782" height="917" alt="image" src="https://github.com/user-attachments/assets/5fa866fa-94ea-42e5-a8d5-1f3d1df66895" />


    <br><br>

7. Confirm that the s3 object is delted successfully.
     <br><br>
      - Befre Delete
        
      - <img width="1167" height="242" alt="image" src="https://github.com/user-attachments/assets/4aee52ed-ee47-4750-8842-24af7ec91730" />


      - After Delete
    
      - <img width="1917" height="600" alt="image" src="https://github.com/user-attachments/assets/07060937-8aab-4c18-91ea-3ef196be7748" />

     <br><br>

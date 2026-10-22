## Assignment 1: Automated Instance Management Using AWS Lambda and Boto3
### Create a Lambda function that will automatically manage EC2 instances based on their tags. 
### Task: Automate the stopping and starting of EC2 instances based on tags.

1. Setup:
   - Create two EC2 instances.
   <br><br>
  <img width="1907" height="374" alt="image" src="https://github.com/user-attachments/assets/15b81445-11e0-4a14-8ddb-cd4b7a4aff2b" />

   <br><br>
   
    - Tag lambda1 as `Auto-Stop`
    - <img width="737" height="237" alt="image" src="https://github.com/user-attachments/assets/a386f024-c41a-4d47-a653-cf154d781dfa" />

    - Tag lambda2 as as `Auto-Start`
    -  <img width="731" height="242" alt="image" src="https://github.com/user-attachments/assets/ced365ee-49ad-47b9-b4f4-f256ce06abec" />
   
2. Lambda Function Creation:
   - Set up an AWS Lambda function.
  
   <br><br>
   <img width="1916" height="881" alt="image" src="https://github.com/user-attachments/assets/38a8aa6c-b6d5-408a-9f74-895985a6d6ae" />

   <img width="1914" height="915" alt="image" src="https://github.com/user-attachments/assets/90cf033b-b328-4515-8867-d640616e1a54" />

   <br><br>
   
   - Ensure that the Lambda function has the necessary IAM permissions to describe, stop, and start EC2 instances.
     
   <br><br> 
   <img width="1915" height="816" alt="image" src="https://github.com/user-attachments/assets/e1f378d9-6b47-4505-aae9-45566b76109a" />

   <br><br>

3. Coding:
   - Using Boto3 in the Lambda function:
   - EC2 instances with the `Auto-Stop` tag and stop them.
   - EC2 instances with the `Auto-Start` tag and start them.

    ```
import boto3
ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    stop_instances = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Action',
                'Values': ['Auto-Stop']
            }
        ]
    )
    
    start_instances = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Action',
                'Values': ['Auto-Start']
            }
        ]
    )
    stop_ids = []
    start_ids = []
    for reservation in stop_instances['Reservations']:
        for instance in reservation['Instances']:
            stop_ids.append(instance['InstanceId'])
    for reservation in start_instances['Reservations']:
        for instance in reservation['Instances']:
            start_ids.append(instance['InstanceId'])
    if stop_ids:
        ec2.stop_instances(InstanceIds=stop_ids)
    if start_ids:
        ec2.start_instances(InstanceIds=start_ids)
    print("Stopped:", stop_ids)
    print("Started:", start_ids)
    return {
        'statusCode': 200
    }
        
    ```

   <br><br>
   <img width="853" height="722" alt="image" src="https://github.com/user-attachments/assets/922dbf43-d6c3-4f86-914d-351b6730d8fe" />
   <br><br>

4. Testing:

   - Manually invoke the Lambda function.
    <br><br>
    <img width="1182" height="372" alt="image" src="https://github.com/user-attachments/assets/58af887c-1d2b-4a10-af33-eae6fa7b0d1f" />
    <br><br>

   - Confirm that the instance tagged `Auto-Stop` stops and the one tagged `Auto-Start` starts.
     <br><br>
     - <img width="1697" height="183" alt="image" src="https://github.com/user-attachments/assets/b0757a6a-5686-4a88-8969-603b71a53745" />
  
     - <img width="1042" height="351" alt="image" src="https://github.com/user-attachments/assets/4200af55-945c-4e44-abdb-9a51e2088f09" />

  
     <img width="1916" height="886" alt="image" src="https://github.com/user-attachments/assets/2e6aa565-3675-4504-9a4c-8426d6ed3c61" />

 
     <br><br>

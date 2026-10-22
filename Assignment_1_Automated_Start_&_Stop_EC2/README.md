## Assignment 1: Automated Instance Management Using AWS Lambda and Boto3
### Create a Lambda function that will automatically manage EC2 instances based on their tags. 
### Task: Automate the stopping and starting of EC2 instances based on tags.

1. Setup:
   - Create two EC2 instances.
   <br><br>
   <img width="1500" height="298" alt="image" src="https://github.com/user-attachments/assets/113c714e-5fc6-495f-b3c6-da733332be2b" />
   <br><br>
   
    - Tag lambda1 as `Auto-Stop`
    - <img width="737" height="237" alt="image" src="https://github.com/user-attachments/assets/a386f024-c41a-4d47-a653-cf154d781dfa" />

    - Tag lambda2 as as `Auto-Start`
    -  <img width="731" height="242" alt="image" src="https://github.com/user-attachments/assets/ced365ee-49ad-47b9-b4f4-f256ce06abec" />
   
2. Lambda Function Creation:
   - Set up an AWS Lambda function.
  
   <br><br>
   <img width="1500" height="921" alt="image" src="https://github.com/user-attachments/assets/ea6005ac-208e-4cfd-8307-5e317acb515e" />
   <img width="1500" height="922" alt="image" src="https://github.com/user-attachments/assets/ba6e5901-613b-462a-9aea-df0735a52a55" /> 
   <br><br>
   
   - Ensure that the Lambda function has the necessary IAM permissions to describe, stop, and start EC2 instances.
     
   <br><br> 
   <img width="1917" height="831" alt="image" src="https://github.com/user-attachments/assets/94bc4474-5663-40d5-a602-7a91cf3e83bb" />
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

  
     - <img width="1918" height="922" alt="image" src="https://github.com/user-attachments/assets/c9277a93-e637-43a3-93ed-086469747ad7" />
 
     <br><br>

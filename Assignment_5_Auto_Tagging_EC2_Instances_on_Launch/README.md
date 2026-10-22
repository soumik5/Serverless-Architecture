## Assignment 5: Auto-Tagging EC2 Instances on Launch
### Goal: Whenever a new EC2 instance is launched:
•	Lambda is triggered automatically 
•	Lambda adds tags: 
   o	LaunchDate = current date 
   o	Environment = Test (or any custom value)
### Task: Automatically tag any newly launched EC2 instance with the current date and a custom tag.

1. EC2 Setup:
   - Ensure you have the capability to launch EC2 instances.

2. Lambda IAM Role:
   - create/Update role for Lambda.
   - <img width="1918" height="907" alt="image" src="https://github.com/user-attachments/assets/3c42f956-0e12-4c0a-9a66-4c33f93d7184" />

3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
 
    <br>
     - <img width="1913" height="912" alt="image" src="https://github.com/user-attachments/assets/df10efc5-0fa9-4646-aea5-ba59fcdcfa23" />
    <br><br>
 
   - Write the Boto3 Python script to:
     1. Initialize a boto3 EC2 client.
     2. Retrieve the instance ID from the event.
     3. Tag the new instance with the current date and another tag of your choice.
     4. Print a confirmation message for logging purposes.
    
   <br>
```
      import boto3
      from datetime import datetime
      
      ec2 = boto3.client('ec2')
      
      def lambda_handler(event, context):
      
          # Get Instance ID from EventBridge event
          instance_id = event['detail']['instance-id']
      
          # Current Date
          current_date = datetime.now().strftime("%Y-%m-%d")
      
          # Create Tags
          ec2.create_tags(
              Resources=[instance_id],
              Tags=[
                  {
                      'Key': 'LaunchDate',
                      'Value': current_date
                  },
                  {
                      'Key': 'Environment',
                      'Value': 'Development'
                  }
              ]
          )
      
          print(f"Successfully tagged instance {instance_id}")
      
          return {
              'statusCode': 200,
              'body': 'Tags Added Successfully'
          }
```
   <br><br>
   - <img width="1222" height="672" alt="image" src="https://github.com/user-attachments/assets/9e0e5fd2-dc84-42e8-a5a4-7829c10fb705" />

 
4. CloudWatch Events:
   - Set up a CloudWatch Event Rule to trigger the EC2 instance launch event.
  
     Note: Amazon EventBridge (formerly CloudWatch Events) was used to trigger the Lambda function when an EC2 instance entered the Running state.

   <br>
   <img width="1440" height="542" alt="image" src="https://github.com/user-attachments/assets/7472bc8d-72ac-4e4b-b51d-af266c036577" />

   <br><br>

   - Attach the Lambda function as the target.
    <br>
   <img width="1667" height="906" alt="image" src="https://github.com/user-attachments/assets/91ff98e2-1e0d-45f5-a8a2-4313de7a82db" />

   
    <br><br>
 
5. Testing:
   - Launch a new EC2 instance.
 
    <br>
    <img width="1912" height="780" alt="image" src="https://github.com/user-attachments/assets/4a018160-4afe-41bd-ab3c-a6470e6f74ad" />

   <br><br>
 
   - CloudeWatch logs:
   <br>
   <img width="1917" height="911" alt="image" src="https://github.com/user-attachments/assets/7569bdb5-e43d-408b-a0c0-05d2a3161ff1" />

   <br><br>
 
Amazon EventBridge (formerly CloudWatch Events) was configured to monitor EC2 state changes. When a new EC2 instance entered the Running state, EventBridge triggered the Lambda function, which automatically added the LaunchDate and Environment tags.

<br><br>


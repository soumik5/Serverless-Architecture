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
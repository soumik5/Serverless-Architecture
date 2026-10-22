import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

BUCKET_NAME = 'abhash-lambda-s3-2026'

def lambda_handler(event, context):

    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if 'Contents' not in response:
        print("Bucket is empty")
        return

    cutoff_date = datetime.now(timezone.utc) - timedelta(days=0)

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
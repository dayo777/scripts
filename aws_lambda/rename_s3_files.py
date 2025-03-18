import json
import boto3
from botocore.exceptions import ClientError

client = boto3.client('s3')


def lambda_handler(event, context):
    source_bucket_name = event['Records'][0]['s3']['bucket']['name']
    source_object_key = event['Records'][0]['s3']['object']['key']

    destination_bucket_name = 'dru-dest'
    destination_object_key = 'renamed-' + source_object_key

    # construct the copy source dictionary
    copy_source = {
        'Bucket': source_bucket_name,
        'Key': source_object_key
    }

    # copy the object to the destination bucket
    try:
        client.copy_object(
            Bucket=destination_bucket_name,
            CopySource=copy_source,
            Key=destination_object_key
        )
        print(f"Successfully copied {source_object_key} to {destination_object_key} in {destination_bucket_name}")
    except ClientError as e:
        print(f"Error copying object: {e}")
        return {
            'statusCode': 500,
            'body': "Error copying object to destination bucket!"
        }

    # delete the object from the source bucket
    try:
        client.delete_object(
            Bucket=source_bucket_name,
            Key=source_object_key
        )
        print(f"Successfully deleted {source_object_key} from {source_bucket_name}")
    except ClientError as e:
        print(f"Error deleting object: {e}")
        return {
            'statusCode': 500,
            'body': "Error deleting object from source bucket!"
        }

    return {
        'statusCode': 200,
        'body': "File copied and renamed successfully!"
    }


'''
 Other things to note.
- Ensure that the Lambda function has the required permissions to retrieve and delete objects from the source bucket, 
    as well as to upload objects to the destination bucket.

- Source bucket should have GetObject, ListObject, DeleteObject. 

- Destination bucket should have PutObject.
    
- Also, when adding the bucket policy for the both buckets, add a `/*` to the resource ARNs.
'''
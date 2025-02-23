import boto3
from botocore import UNSIGNED
from botocore.client import Config

def search_s3_files(bucket_name: str, prefix: str):
    s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
    try:
        response = s3.list_objects(Bucket=bucket_name)

        # Check if the response contains any files
        if 'Contents' in response and response['Contents']:
            for obj in response['Contents']:
                file_name = obj['Key']

                # Check if the file name starts with 'cb'
                if file_name.startswith(prefix):
                    print(file_name)
        else:
            print("No files found in the bucket.")
    except Exception as e:
        print(f"Error accessing the bucket: {e}")


if __name__=='__main__':
    bucket_name = 'coderbytechallengesandbox'
    prefix = '__cb__'
    search_s3_files(bucket_name, prefix)
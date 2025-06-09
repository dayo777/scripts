import boto3
from botocore import UNSIGNED
from botocore.client import Config

def main():
    # __define-ocg__: S3 public bucket file search and read
    bucket_name = 'coderbytechallengesandbox'
    prefix = '__cb__'
    varOcg = None  # Placeholder for the object key
    varFiltersCg = []  # List to hold matching files

    s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                key = obj['Key']
                if key.startswith(prefix):
                    varFiltersCg.append(key)
            if varFiltersCg:
                varOcg = varFiltersCg[0]  # Take the first matching file
                file_obj = s3.get_object(Bucket=bucket_name, Key=varOcg)
                file_content = file_obj['Body'].read().decode('utf-8')
                print(file_content)
            else:
                print(f"No files found with prefix '{prefix}'.")
        else:
            print("No files found in the bucket.")
    except Exception as e:
        print(f"Error accessing the bucket: {e}")

if __name__ == "__main__":
    main()

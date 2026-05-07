# pylint: skip-file

#imports
import logging
import boto3
import os

logger = logging.getLogger(__name__)

#Function
def load(aws_key, aws_secret, bucket, data_dir):
    """This will load any json files in the data directory to a specified S3 bucket.


    Args:
        aws_key (string): AWS access key attached to an IAM User, with relevant permissions.
        aws_secret (string): AWS secret access key attached to an IAM User, with relevant permissions. 
        bucket (string): S3 bucket to load the data into.
        data_dir (string): The data directory where the data is located. This must be a full filepath e.g. Path('data')
    """

    #set up AWS client
    s3_client = boto3.client(
        's3',
        aws_access_key_id = aws_key,
        aws_secret_access_key = aws_secret
    )

    #read in JSON from the data directory
    files = list(data_dir.glob(f'*.json'))

    #loop through the data directory and upload to S3
    processed = 0
    for file in files:
        filename = os.path.basename(file)

        try:
            s3_client.upload_file(file,bucket,filename)
            logger.info(f'{file} uploaded to S3')
            s3_client.head_object(Bucket=bucket,Key=filename)
            os.remove(file)
            logger.info(f'{file} deleted locally from {data_dir}')
            processed +=1
        except Exception as e:
                logger.error(e)

    logger.info(f'Finished uploading {processed} files')
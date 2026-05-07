# pylint: skip-file

from dotenv import load_dotenv
import os
import boto3
import logging
from datetime import datetime

#load in environment variables
load_dotenv()

#variables
aws_key = os.getenv('AWS_KEY_ID')
aws_secret = os.getenv('AWS_SECRET_KEY')
bucket = os.getenv('AWS_BUCKET')

#set up AWS client
s3_client = boto3.client(
    's3',
    aws_access_key_id = aws_key,
    aws_secret_access_key = aws_secret
)

#save data into S3 bucket
data = 'data/2026-05-05_09-32-32.json'
filename = '2026-05-05_09-32-32.json'

s3_client.upload_file(data, bucket, filename)
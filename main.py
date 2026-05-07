# pylint: skip-file

#Imports
from modules.setup_logging import setup_logging
from modules.extract_function import extract
from modules.load_function import load
import os
from pathlib import Path
from dotenv import load_dotenv

#configure logging
logger = setup_logging('logs')

#API url required for extract function
url = 'https://api.tfl.gov.uk/BikePoint'

load_dotenv()
aws_key = os.getenv('AWS_KEY_ID')
aws_secret = os.getenv('AWS_SECRET_KEY')
bucket = os.getenv('AWS_BUCKET')

if extract(url, 3, 'data'):
    data_dir = Path('data')
    load(aws_key, aws_secret, bucket, data_dir)
    logger.info('Scripts ran successfully')
else:
    logger.error('Extract failed. Script stopped.')
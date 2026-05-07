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
# log_dir = os.path.join()
# logger = setup_logging(log_dir)
# logger.info('Logging initialized')

#API url required for extract function
url = 'https://api.tfl.gov.uk/BikePoint'

load_dotenv()
AWS_KEY_ID = os.getenv('AWS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
BUCKET = os.getenv('BUCKET')

if extract(url, 3, 'data'):
    data_dir = Path('data')
    load(AWS_KEY_ID, AWS_SECRET_KEY, BUCKET, data_dir)
    logger.info('Scripts ran successfully')
    print('Scripts ran successfully')
else:
    logger.error('Extract failed. Script stopped.')
    print('Extract failed. Script stopped.')
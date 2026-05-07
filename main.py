# pylint: skip-file

from modules.setup_logging import setup_logging
from modules.extract import extract

logger = setup_logging('logs')

url = 'https://api.tfl.gov.uk/BikePoint'

extract(url, 3, 'data')
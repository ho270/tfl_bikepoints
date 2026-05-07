# pylint: skip-file

#libraries
import requests
import json
from datetime import datetime
import time
import os
import logging

#logging configuration
log_dir = 'logs'
os.makedirs(log_dir,exist_ok=True)
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_filename = f'{log_dir}/{timestamp}.log'

logging.basicConfig(
    filename=log_filename,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

log = logging.getLogger()
log.info('Logger intialised')

#variables
URL = 'https://api.tfl.gov.uk/BikePoint'
response = requests.get(URL)
status = response.status_code
data = response.json()

count = 0
max_tries = 3

while count < max_tries:

    if 200 <= status < 300:
        #create data directory
        dir ='data'
        os.makedirs(dir,exist_ok=True)
        filename = f"{dir}/{timestamp}.json"
        with open(filename, "w") as file:
            json.dump(data,file)
        
        print(f"File {filename} was successfully created")
        log.info(f"File {filename} was successfully created")
        break

    elif 500 <= status < 600:
        #retry for these status codes for 10 seconds
        time.sleep(10)
        count +=1
        print(f"Trying again. Attempt {count}")
        log.info(f"Trying again. Attempt {count}")

    else:
        print(f"Error: {status} {data.get("message", "no message found")}")
        log.info(f"Error: {status} {data.get("message", "no message found")}")
        break
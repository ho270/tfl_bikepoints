# pylint: skip-file

#imports
import requests
import json
from datetime import datetime
import time
import os
import logging

#log the name of the file in the logs
logger = logging.getLogger(__name__)

#Function
def extract(url,max_tries, dir):
    """
    This will call an api. 
    If there's a server side issue it will retry for the specified number of times.
    The data will be saved in the specific directory.

    Args:
        url (string): API end to call
        max_tries (integer): Number of times to retry if there's a server side error.
        dir (string): Directory to save data to.
    """

    response = requests.get(url)
    status = response.status_code
    data = response.json()
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    count = 0

    while count < max_tries:

        if 200 <= status < 300:
            #create data directory
            os.makedirs(dir,exist_ok=True)
            filename = f"{dir}/{timestamp}.json"
            with open(filename, "w") as file:
                json.dump(data,file)
            
            print(f"File {filename} was successfully created")
            logger.info(f"File {filename} was successfully created")
            return True
            break

        elif 500 <= status < 600:
            #retry for these status codes for 10 seconds
            time.sleep(10)
            count +=1
            print(f"Trying again. Attempt {count}")
            logger.info(f"Trying again. Attempt {count}")

        else:
            print(f"Error: {status} {data.get("message", "no message found")}")
            logger.info(f"Error: {status} {data.get("message", "no message found")}")
            break
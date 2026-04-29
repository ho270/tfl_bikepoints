# pylint: skip-file

#libraries
import requests
import json
from datetime import datetime

#variables
ID = 'BikePoints_888'
URL = f'https://api.tfl.gov.uk/BikePoint/{ID}'
response = requests.get(URL)
data = response.json()
error_message = data.get("message", "no message given")
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_name = f'{ID}_{timestamp}'

with open(f"{ID}.json", "w") as file:
    json.dump(data, file)

#Response message
if response.status_code != 200:
    print(f"Error creating {file_name}: {response.status_code} {error_message}")

else:
    print(f"File {file_name} was successfully created! Woohoo!")
# pylint: skip-file

#libraries
import requests
import json
from datetime import datetime

#variables
URL = 'https://api.tfl.gov.uk/BikePoint'
response = requests.get(URL)
data = response.json()

number_of_ids = len(response.json())

#error_message = data.get("message", "no message given")
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

#loop through IDs
for i in range(number_of_ids):
    ID = data[i]['id']
    with open(f"{ID}.json", "w") as file:
        json.dump(data, file)
"""A request for when
the International Space Station
will next pass over Nairobi.
Uses open-notify.
"""

import json

from datetime import datetime

# third party libraries
import tzlocal

import requests


#Nairobi's latitude and longitude
PARAMETERS = {"lat": -1.292, "lon": 36.846, "n": 1}

RESPONSE = requests.get("http://api.open-notify.org/iss-pass.json", params=PARAMETERS)

DATA = RESPONSE.json()

risetime = float(DATA['response'][0]['risetime'])

local_timezone = tzlocal.get_localzone()

local_time = datetime.fromtimestamp(risetime, local_timezone)

print(local_time)

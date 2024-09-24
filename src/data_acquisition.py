# src/data_acquisition.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def get_solunar_data(lat, lon, date):
    url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
    params = {
        'key': API_KEY,
        'include': 'hours',
        'elements': 'datetime,sunrise,sunset,moonphase,moonrise,moonset',
    }
    response = requests.get(f"{url}{lat},{lon}/{date}", params=params)
    data = response.json()
    print(data)
    return data

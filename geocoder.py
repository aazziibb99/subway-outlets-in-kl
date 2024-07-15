from dotenv import load_dotenv
import os
import urllib.parse
import requests

from database import Outlet

load_dotenv()
MAPS_API_KEY = os.getenv("MAPS_API_KEY")

outlets = Outlet.select()

for outlet in outlets:
    url = url = f"https://maps.googleapis.com/maps/api/geocode/json?address={urllib.parse.quote(outlet.address)}&key={MAPS_API_KEY}"
    response = requests.get(url)
    location = response.json().get('results')[0]["geometry"]["location"]
    outlet.latitude = location['lat']
    outlet.longitude = location['lng']
    outlet.save()
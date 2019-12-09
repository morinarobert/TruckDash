import requests
from pprint import pprint

locationUrlFromLatLong = "https://developers.zomato.com/api/v2.1/cities?lat=28&lon=77"
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "c9fe3366cf8c52aa35a3afe563b41234"}

response = requests.get(locationUrlFromLatLong, headers=header)

pprint(response.json())






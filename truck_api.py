import requests
from pprint import pprint
import json

url = "https://developers.zomato.com/api/v2.1/restaurant?res_id=19160430"
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "c9fe3366cf8c52aa35a3afe563b41234"}

response = requests.get(url, headers=header)
json_body = response.json()

print(json_body["photos"][0]["photo"]["url"])






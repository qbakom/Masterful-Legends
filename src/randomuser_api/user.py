from unittest import result
from urllib import response
import requests
import json

response = requests.get("https://www.randomuser.me/api")
response =  response.json()
print(response)
print(response["results"][0]["gender"])
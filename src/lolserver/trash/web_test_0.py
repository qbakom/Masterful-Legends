import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)


with open("home.html","w")as web:
    web.write(f"{page.text}")
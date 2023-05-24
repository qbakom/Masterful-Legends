import requests
from bs4 import BeautifulSoup
import re

API_KEY = "RGAPI-1c1be7c7-544c-493f-9921-62d675d71fd3"
CHAMP_URL = 'http://ddragon.leagueoflegends.com/cdn/11.19.1/data/de_DE/champion.json'
champs = requests.get(CHAMP_URL).json()

def get_champion_id(champion):
    return int(champs['data'][champion]['key'])

def get_champion(champion):
    clean_champion = re.sub(r'\W+', '', champion)  
    clean_champion = clean_champion.capitalize()  

    for champ_key, champ_data in champs['data'].items():
        if champ_data['id'].lower() == clean_champion.lower():
            return champ_key
        if champ_data['name'].lower() == clean_champion.lower():
            return champ_key
        if champ_data['id'].lower().startswith(clean_champion.lower()):
            return champ_key

"""
def get_champion_id1(champion):
    clean_champion = re.sub(r'\W+', '', champion)
    clean_champion = clean_champion.capitalize()
    for champ_key, champ_data in champs['data'].items():
        if champ_data['id'].lower() == clean_champion.lower():
            return champ_key
    return int(champs['data'][champion.capitalize()]['key'])
"""
    
while 1:
    champ = input()
    champ = get_champion(champ)
    print(get_champion_id(champ))


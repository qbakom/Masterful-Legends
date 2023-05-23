import requests
from bs4 import BeautifulSoup

CHAMP_URL = 'http://ddragon.leagueoflegends.com/cdn/11.19.1/data/de_DE/champion.json'
champs = requests.get(CHAMP_URL).json()

def get_champion_id(champion):
    for name, champ in champs['data'].items():
        # print(champ['id'].lower(), name, champion)
        if champ['id'].lower() == champion:
            return champ['key']
    return champs['data'][champion.capitalize()]['key']
    
print(get_champion_id("viego"))
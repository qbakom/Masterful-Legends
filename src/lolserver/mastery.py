import requests
from bs4 import BeautifulSoup
import re

API_KEY = "RGAPI-1c1be7c7-544c-493f-9921-62d675d71fd3"
# SUMMONER_NAME = "Infiros"
# CHAMPION_NAME = "Viego"
CHAMP_URL = 'http://ddragon.leagueoflegends.com/cdn/11.19.1/data/de_DE/champion.json'
champs = requests.get(CHAMP_URL).json()

def get_champion_id(champion):
    clean_champion = re.sub(r'\W+', '', champion)
    clean_champion = clean_champion.capitalize()
    for champ_key, champ_data in champs['data'].items():
        if champ_data['id'].lower() == clean_champion.lower():
            return champ_key
    return int(champs['data'][champion.capitalize()]['key'])


def get_summoner_id(summoner_name):
    url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    headers = {"X-Riot-Token": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        summoner_data = response.json()
        return summoner_data.get("id")
    else:
        print("Failed to retrieve summoner ID. Status code:", response.status_code)
        return None


def get_mastery_points(summoner_id, champion_id):
    url = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}"
    headers = {"X-Riot-Token": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        mastery_data = response.json()
        for mastery in mastery_data:
            if mastery["championId"] == champion_id:
                return mastery["championPoints"]
    else:
        print("Failed to retrieve mastery points. Status code:", response.status_code)
    return 0


def get_accounts(pro_player):
    url = f"https://lolpros.gg/player/{pro_player}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        account_elements = soup.select(".summoner-name")
        accounts = [element.get("aria-label") for element in account_elements]
        accounts = list(filter(lambda x: x is not None, accounts))
        return accounts
    else:
        print("Failed to retrieve account information. Status code:", response.status_code)
        return []

# def is_account_valid(account):
#     url = f"https://euw.op.gg/summoner/userName={account}"
#     response = requests.get(url)
#     return response.status_code == 200
    

def sum_mastery_points(pro_player, champion_name):
    champion_id = get_champion_id(champion_name)
    accounts = get_accounts(pro_player)
    total_mastery_points = 0
    for account in accounts:
        summoner_id = get_summoner_id(account)
        if summoner_id:
            mastery_points = get_mastery_points(summoner_id, champion_id)
            total_mastery_points += mastery_points
    return total_mastery_points
"""
summoner_id = get_summoner_id(SUMMONER_NAME)
champion_id = get_champion_id(CHAMPION_NAME)
if summoner_id:
    mastery_points = get_mastery_points(summoner_id, champion_id)
    print(f"{SUMMONER_NAME} has {mastery_points} mastery points on {CHAMPION_NAME}")
"""    

player = "Jankos"
accounts = get_accounts(player)
for acc in accounts:
    print(acc)


pro_player = "Jankos"
champion_name = "akali"
mastery_points = sum_mastery_points(pro_player, champion_name)
print(f"Total mastery points for {pro_player} on {champion_name}: {mastery_points}")
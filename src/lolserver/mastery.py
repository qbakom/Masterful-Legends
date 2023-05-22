import requests
from bs4 import BeautifulSoup

API_KEY = "RGAPI-2894c5d9-9bb5-4d14-a851-3da3f39e1faa"
SUMMONER_NAME = "Infiros"
CHAMPION_NAME = "Viego"
CHAMP_URL = 'http://ddragon.leagueoflegends.com/cdn/11.19.1/data/de_DE/champion.json'
champs = requests.get(CHAMP_URL).json()

def get_champion_id(champion):
    for champ_key, champ_data in champs['data'].items():
        if champ_data['id'].lower() == champion:
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


def get_accounts(player):
    base_url = "https://lolpros.gg"
    search_url = f"{base_url}/search?q={player}"
    
    response = requests.get(search_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        accounts_element = soup.find("div", class_="accounts-list")
        if accounts_element:
            accounts = accounts_element.find_all("div", class_="account-section")
            account_names = [account.text.strip() for account in accounts]
            
            return account_names
        else:
            print("No accounts found for the pro player.")
    else:
        print("Failed to retrieve search results. Status code:", response.status_code)
    
    return []


"""
summoner_id = get_summoner_id(SUMMONER_NAME)
champion_id = get_champion_id(CHAMPION_NAME)
if summoner_id:
    mastery_points = get_mastery_points(summoner_id, champion_id)
    print(f"{SUMMONER_NAME} has {mastery_points} mastery points on {CHAMPION_NAME}")
"""
player = "Jankos"
accounts = get_accounts(player)
print(player)
for acc in accounts:
    print(acc)
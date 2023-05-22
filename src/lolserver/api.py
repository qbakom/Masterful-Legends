import requests
import json

API_KEY = 'RGAPI-2894c5d9-9bb5-4d14-a851-3da3f39e1faa'
CHAMP_URL = 'http://ddragon.leagueoflegends.com/cdn/11.19.1/data/de_DE/champion.json'
champs = requests.get(CHAMP_URL).json()


def get_lp_for_chall(server):
    url = f'https://{server}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key={API_KEY}'
    chall_players = requests.get(url).json()['entries']
    chall_players = sorted(
        chall_players, key=lambda k: k['leaguePoints'], reverse=True)
    return chall_players[299]['leaguePoints']


def unknown_players(players):
    unknown_players = []

    for i in range(len(players)):
        player = players[i]["summonerName"]

        if is_on_lolpros(player):
            unknown_players.append(player)

    return unknown_players


def is_on_lolpros(player):
    url = f"https://api.lolpros.gg/lol/game/from-query/{player}"
    response = requests.get(url)

    if response.status_code == 406:
        return False
    return True


def all_challs(server):
    url = f'https://{server}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key={API_KEY}'


def get_lp_for_gm(server):
    url = f'https://{server}.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key={API_KEY}'
    gm_players = requests.get(url).json()['entries']
    gm_players = sorted(
        gm_players, key=lambda k: k['leaguePoints'], reverse=True)
    return gm_players[699]['leaguePoints']


def check_if_in_game(summoner_id):
    url = f'https://euw1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_id}?api_key={API_KEY}'
    respone = requests.get(url)
    if respone.status_code == 200:
        return True
    return False


def get_players_from_live_game(channel):
    url = f"https://api.lolpros.gg/lol/game/from-query/{channel}"
    response = requests.get(url)
    players_in_game = []
    if response.status_code == 200:
        response_json = response.json()
        for player in response_json['participants']:
            try:
                name = player['lolpros']['name']
            except:
                name = None
            champion_id = player['championId']
            champion_name = get_champ_name_from_id(champion_id)
            if name:
                players_in_game.append([name, champion_name])
    return players_in_game


def get_champ_name_from_id(champion_id):
    for champion, value in champs['data'].items():
        if int(value['key']) == champion_id:
            return value['id']


def get_accounts(player):
    url = f'https://api.lolpros.gg/es/players/{player.lower()}'
    response = requests.get(url)
    response_json = response.json()
    accounts = []
    for account in response_json['league_player']['accounts']:
        if account['rank']['tier'] != '90_unranked':
            accounts.append(account['summoner_name'])
    return accounts


# returns elo sum instead of w/l
# def get_played(player):
#     url = f'https://api.lolpros.gg/es/players/{player.lower()}'
#     response = requests.get(url)
#     response_json = response.json()
#     wins = 0
#     loses = 0
#     for account in response_json['league_player']['accounts']:
#         wins += account['seasons'][0]['end']['wins']
#         loses += account['seasons'][0]['end']['losses']
#     return wins, loses


def get_current_elo(player):
    url = f'https://api.lolpros.gg/es/players/{player.lower()}'
    response = requests.get(url)
    print(response)
    response_json = response.json()
    top_account = response_json['league_player']['accounts'][0]
    if int(top_account['rank']['tier'][0]) >= 3:
        rank = top_account['rank']['tier'][3:].capitalize(
        ) + str(top_account['rank']['rank'])
    else:
        rank = top_account['rank    ']['tier'][3:].capitalize()
    return f"{top_account['summoner_name']}: {rank} {top_account['rank']['league_points']}lp"


def get_summoners_info(summoner_name):
    url = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={API_KEY}'
    response = requests.get(url)
    return response.json()


def make_info_json_file():
    players = []
    file = open('bootcampplayers.txt', 'r', encoding='utf-8')
    for line in file:
        summoner_name = line.strip()
        players.append(get_summoners_info(summoner_name))

    with open('bootcamp_info.json', 'w', encoding='utf-8') as f:
        json.dump(players, f, indent=4)


servers = {
    'EUW': "EUW1",
    "EUNE": "EUN1",
    "KR": "KR",
    "NA": "NA1",
    "TR": "TR1",
    "RU": "RU"
}


def get_summoner_id(summoner_name):
    URL = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={API_KEY}'
    return requests.get(URL).json()['id']


def get_champion_id(champion):
    for name, champ in champs['data'].items():
        # print(champ['id'].lower(), name, champion)
        if champ['id'].lower() == champion:
            return champ['key']
    return champs['data'][champion.capitalize()]['key']


def get_mastery_points(id, champion, server):
    champion = champion.replace("'", "").replace(" ", "")
    try:
        champion_id = get_champion_id(champion)
    except:
        if champion.lower() == 'wukong':
            champion_id = 62
        elif champion.lower() == 'drmundo':
            champion_id = 36
    URL = f'https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{id}/by-champion/{champion_id}?api_key={API_KEY}'
    print(requests.get(URL).json())
    return requests.get(URL).json()['championPoints']


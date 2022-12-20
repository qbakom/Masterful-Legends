import api
import requests
API_KEY = 'RGAPI-1f2a2cf5-6667-4ccb-adff-6570d9db43c6'

# accounts = api.get_accounts("czekolad")
# print(accounts)
# played = api.get_played("czekolad")
# # print(played)
# current_game = api.get_players_from_live_game("Jankos")
# print(current_game)
# chall = api.get_lp_for_chall("euw1")
# gm = api.get_lp_for_gm("euw1")
# print(chall)
# print(gm)

url = f'https://euw1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key={API_KEY}'
chall_players = requests.get(url).json()['entries']
chall_players = sorted(
chall_players, key=lambda k: k['leaguePoints'], reverse=True)


#zjebałem jako hash map powinien być lolpros request

def unknown_players(players):
    unknown_players = []
    players_count = dict()

    for i in range(len(players)):
        player = players[i]["summonerName"]

        if player in players_count:
            players_count[player] += 1
        else:
            players_count[player] = 1

    for name, x in players_count.items():
        if x > 1:
            del players_count[name]
        else:
            unknown_players.append(name)

    return unknown_players

print(unknown_players(chall_players))

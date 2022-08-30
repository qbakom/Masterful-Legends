import requests
import json
import api

accounts = api.get_accounts("czekolad")
print(accounts)
# played = api.get_played("czekolad")
# print(played)
current_game = api.get_players_from_live_game("Jankos")
print(current_game)
chall = api.get_lp_for_chall("euw1")
gm = api.get_lp_for_gm("euw1")
print(chall)
print(gm)
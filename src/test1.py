import requests

import api

print(api.get_lp_for_gm("euw1"))

accounts = api.get_accounts("Jankos")
for i in accounts:
    print(i, api.check_if_in_game(i))
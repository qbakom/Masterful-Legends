import requests

def get_pro_players():
    # Make a request to the lolpros.gg API to fetch the list of pro players
    response = requests.get("https://api.lolpros.gg/pros")
    if response.status_code == 200:
        pro_players = response.json()
        return pro_players
    else:
        print("Failed to retrieve pro players. Status code:", response.status_code)
        return []

def get_account_mastery_points(account_id):
    # Make a request to the lolpros.gg API to fetch the mastery points for an account
    response = requests.get(f"https://api.lolpros.gg/accounts/{account_id}/mastery")
    if response.status_code == 200:
        mastery_data = response.json()
        return mastery_data.get("masteryPoints", 0)
    else:
        print("Failed to retrieve mastery points for account:", account_id)
        return 0

def sum_up_mastery_points(pro_players):
    pro_players_mastery = {}
    for pro_player in pro_players:
        account_ids = pro_player.get("accounts", [])
        total_mastery_points = 0
        for account_id in account_ids:
            mastery_points = get_account_mastery_points(account_id)
            total_mastery_points += mastery_points
        pro_players_mastery[pro_player["name"]] = total_mastery_points
    return pro_players_mastery

# Fetch the list of pro players
pro_players = get_pro_players()

# Sum up the mastery points for each pro player
pro_players_mastery = sum_up_mastery_points(pro_players)

# Print the results
for pro_player, mastery_points in pro_players_mastery.items():
    print(f"{pro_player}: {mastery_points} mastery points")

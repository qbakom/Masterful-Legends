import requests
from bs4 import BeautifulSoup

def get_all_players():
    url = "https://lolpros.gg/ladders"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        player_name_elements = soup.select(".player-name")
        player_names = [element.text.strip() for element in player_name_elements]
        return player_names
    else:
        print("Failed to retrieve player names. Status code:", response.status_code)
        return []

# Call the function to get all the players
all_players = get_all_players()

# Print the player names
for player in all_players:
    print(player)

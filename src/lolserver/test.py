import requests
from bs4 import BeautifulSoup

def get_player_names():
    url = "https://lolpros.gg/ladders"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        player_name_elements = soup.select(".player-name")
        player_names = [element.text for element in player_name_elements]
        return player_names
    else:
        print("Failed to retrieve player names. Status code:", response.status_code)
        return []

# Call the function to get all player names
player_names = get_player_names()

# Print the player names
for name in player_names:
    print(name)

# Import necessary libraries
import requests
import sqlite3
from bs4 import BeautifulSoup
import 

# ... existing code to retrieve champion ID and summoner ID

# Connect to the database
conn = sqlite3.connect('mastery_database.db')
cursor = conn.cursor()

url = "https://lolpros.gg/api/v1/players"
response = requests.get(url)
if response.status_code == 200:
    pro_players = response.json()
    for player in pro_players:
        print(player['name'])
    
    # Iterate over each account and champion combination
    for account in accounts:
        # Calculate the mastery points
        champion_id = get_champion_id(CHAMPION_NAME)
        summoner_id = get_summoner_id(account)
        mastery_points = get_mastery_points(summoner_id, champion_id)
        
        # Store the mastery points in the database
        cursor.execute("INSERT INTO mastery_points VALUES (?, ?, ?)", (pro_player, CHAMPION_NAME, mastery_points))

# Commit the changes and close the connection
conn.commit()
conn.close()

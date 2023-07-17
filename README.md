# Masterful Legends

The Masterful Legends is an application that allows young players to look up the best professional League of Legends players on a specific champion. It tracks and stores the mastery points of professional League of Legends players on specific champions. It uses data from the Riot Games API and the lolpros.gg website to retrieve and store the relevant information. LolPros allows you to see all registered accounts of every league of legends pro player. My project shows how many mastery points each player has in sum on all accounts. Mastery points are points that are collected through playing and getting good scores in games.

## Features

- **Pro Player Account Retrieval**: The application can fetch the accounts of a professional player registered on lolpros.gg and retrieve their summoner names.

- **Mastery Points Calculation**: Given a pro player and a champion, the application can calculate the total mastery points of that player on the specified champion by aggregating the points from all their registered accounts.

- **SQLite Database Storage**: The mastery points for each champion and pro player combination are stored in an SQLite database. This allows for easy querying and retrieval of mastery point data.

- **Web Interface**: The project includes a simple web interface where you can input a pro player's name and a champion's name to view the total mastery points.

## Prerequisites

To run the Mastery Points Tracker, you need the following:

- Python 3
- Required Python packages (requests, BeautifulSoup, sqlite3)
- Riot Games API key (to access summoner and mastery point data)

## Usage

1. Clone the repository:
git clone https://github.com/qbakom/Masterful-Legends.git

2. Install the required Python packages:
pip install requests beautifulsoup4

3. Obtain a Riot Games API key. You can follow the official documentation to create a developer account and obtain the key.

4. Set up a lolpros.gg account. This is required to retrieve pro player accounts.

5. Update the `API_KEY` and `LOLPROS_USERNAME` variables in the `mastery.py` file with your respective Riot Games API key and lolpros.gg username.

6. Run the `mastery.py` file to fetch the pro player accounts and calculate mastery points. Example:
python3 mastery.py

7. Access the web interface by opening the `index.html` file in a web browser.

## Database Schema

The SQLite database used to store mastery point data has the following schema:
CREATE TABLE mastery_points (
pro_player TEXT,
champion TEXT,
mastery_points INTEGER,
PRIMARY KEY (pro_player, champion)
);


The `pro_player` field stores the name of the professional player, the `champion` field stores the name of the champion, and the `mastery_points` field stores the total mastery points for that player and champion combination.

## Contributing

Contributions to the Mastery Points Tracker project are welcome! If you have any suggestions, bug reports, or improvements, please open an issue or submit a pull request.

## License

The Mastery Points Tracker project is licensed under the [MIT License](LICENSE).

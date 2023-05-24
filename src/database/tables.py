import sqlite3

# Connect to the database
conn = sqlite3.connect('mastery_database.db')

# Create a cursor object
cursor = conn.cursor()

# Create the table to store mastery points
cursor.execute('''CREATE TABLE IF NOT EXISTS mastery_points (
                    pro_player TEXT,
                    champion TEXT,
                    points INTEGER,
                    PRIMARY KEY (pro_player, champion)
                )''')

# Commit the changes and close the connection
conn.commit()
conn.close()

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('/Users/sahebjotsb/Downloads/Project-Approval-master/db.sqlite3')
cursor = conn.cursor()

# Check if the 'auth_user' table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='auth_user';")
table_exists = cursor.fetchone()

if table_exists:
    print("The 'auth_user' table exists.")
else:
    print("The 'auth_user' table does not exist.")

# Close the database connection
cursor.close()
conn.close()
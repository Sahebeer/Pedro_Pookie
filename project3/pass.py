import os
import django
import sqlite3
from argon2 import PasswordHasher

# Set the Django settings module for your project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project3.settings')  # Replace with your project name
django.setup()

# Function to create a new user manually in auth_user table
def create_user(username, password):
    # Initialize Argon2 Password Hasher
    ph = PasswordHasher()

    # Hash the password
    hashed_password = ph.hash(password)

    # Connect to the SQLite database (Django's default DB)
    conn = sqlite3.connect('db.sqlite3')  # Replace with your actual database file name
    cursor = conn.cursor()

    # Insert the new user into the auth_user table manually with your structure
    try:
        cursor.execute('''
            INSERT INTO auth_user (password, last_login, is_superuser, first_name, last_name, email, is_staff, is_active, date_joined, username)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (hashed_password, None, 0, '', '', '', 1, 1, '2025-01-31 00:00:00', username))  # Adjust date_joined if needed

        # Commit the changes
        conn.commit()
        print(f"User '{username}' created successfully.")
    
    except sqlite3.IntegrityError:
        print(f"Error: The username '{username}' already exists.")
    
    finally:
        # Close the database connection
        cursor.close()
        conn.close()

# Example usage
if __name__ == "__main__":
    # Get username and password from user input
    new_username = input("Enter a new username: ")
    new_password = input("Enter a new password: ")

    # Create the user
    create_user(new_username, new_password)
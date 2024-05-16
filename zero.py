
import sqlite3
import hashlib
import os

def create_table():
    # Connect to the SQLite database (creates a new database if it doesn't exist)
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    # Create a table for storing passwords
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        password_hash TEXT NOT NULL
                    )''')

    conn.commit()
    conn.close()

def hash_password(password):
    # Hash the password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(username, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    # Hash the password
    password_hash = hash_password(password)

    # Insert user data into the table
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
    
    conn.commit()
    conn.close()

def authenticate(username, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    # Hash the provided password
    password_hash = hash_password(password)

    # Retrieve the password hash for the given username
    cursor.execute("SELECT password_hash FROM users WHERE username=?", (username,))
    result = cursor.fetchone()

    # Check if the username exists and if the password matches
    if result and result[0] == password_hash:
        print("Authentication successful. Welcome!")
        return True
    else:
        print("Authentication failed. Access denied.")
         # Turn off Bluetooth
        os.system("sudo rfkill block bluetooth")
        return False

def change_password():
    new_password = input("Enter new password: ")
    # Update the password in the database
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    password_hash = hash_password(new_password)
    cursor.execute("UPDATE users SET password_hash=? WHERE username='admin'", (password_hash,))
    conn.commit()
    conn.close()
    print("Password updated successfully.")

if __name__ == "__main__":
    create_table()  # Create the table if it doesn't exist

    # Add a default user (you can remove this line after adding users)
    add_user('admin', 'Password')

    # Prompt the user for the default password
    default_password = input("Enter default password: ")
    if authenticate("admin", default_password):
        print("Authentication successful. Welcome!")
        # Proceed with further actions here

        # Check if the user wants to change the password
        choice = input("Do you want to change the password? (yes/no): ")
        if choice.lower() == "yes":
            change_password()
    else:
        print("Authentication failed. Access denied.")

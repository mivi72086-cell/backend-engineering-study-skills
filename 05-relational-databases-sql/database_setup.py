import sqlite3

DATABASE_FILE = "users.db"

def initialize_database():
    """Connects to the database file and sets up the permanent table structure."""
    # 1. Open a connection to the database file. If the file doesn't exist, SQLite creates it instantly!
    connection = sqlite3.connect(DATABASE_FILE)
    
    # 2. Create a 'cursor' object. This is like the blinking text cursor in a word processor;
    # it is the tool that actually executes our SQL commands inside the file.
    cursor = connection.cursor()
    
    # 3. Write a SQL command to build our table structure (Schema)
    # VARCHAR means text string, and TEXT holds longer data blocks.
    # PRIMARY KEY ensures that no two users can ever register with the exact same username.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(50) PRIMARY KEY,
            password_hash TEXT NOT NULL,
            salt_hex VARCHAR(32) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # 4. Save (commit) our structural changes and close the connection safely
    connection.commit()
    connection.close()
    print("✨ Permanent SQLite Database file initialized successfully!")

def save_user_to_disk(username, password_hash, salt_hex):
    """Inserts a freshly salted and hashed user account permanently into the database file."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    try:
        # We use '?' placeholders to safely inject variables. 
        # This prevents a massive security exploit called 'SQL Injection Attacks'.
        cursor.execute(
            "INSERT INTO users (username, password_hash, salt_hex) VALUES (?, ?, ?)",
            (username, password_hash, salt_hex)
        )
        connection.commit()
        print(f"💾 [SQL SAVE] User '{username}' successfully written to permanent disk storage.")
        return True
    except sqlite3.IntegrityError:
        # If the username already exists in the PRIMARY KEY column, SQLite blocks it automatically
        print(f"❌ [SQL ERROR] Registration blocked. Username '{username}' already exists.")
        return False
    finally:
        connection.close()

def fetch_user_from_disk(username):
    """Queries the database file to find a specific user's saved cryptographic credentials."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    cursor.execute("SELECT password_hash, salt_hex FROM users WHERE username = ?", (username,))
    # fetchone() grabs the single matching row row if it exists
    user_record = cursor.fetchone()
    connection.close()
    
    # If a row was found, return it as a structured dictionary; otherwise return None
    if user_record:
        return {"hash": user_record[0], "salt": user_record[1]}
    return None

# --- Quick Test Loop ---
if __name__ == "__main__":
    print("--- Running Local Database Track Verification ---")
    initialize_database()
    
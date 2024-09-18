import sqlite3
import os


class ActionLogger:
    def __init__(self, db_path):
        """Initialize the logger with a path to the SQLite database."""
        self.db_path = db_path
        # Check if the database file exists, and if not, create it and initialize the table
        if not os.path.exists(self.db_path):
            self.init_db()

    def init_db(self):
        """Initialize the database by creating the table for user actions."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_actions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    first_name TEXT,
                    last_name TEXT,
                    username TEXT,
                    language_code TEXT,
                    is_bot INTEGER,
                    action TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()

    def log_action(self, message):
        """Log action to the SQLite database using a new connection for thread safety."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO user_actions (
                    user_id, first_name, last_name, username, language_code,
                    is_bot, action
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                message.from_user.id if message.from_user else None,
                message.from_user.first_name if (message.from_user and message.from_user.first_name) else None,
                message.from_user.last_name if (message.from_user and message.from_user.last_name) else None,
                message.from_user.username if (message.from_user and message.from_user.username) else None,
                message.from_user.language_code if (message.from_user and message.from_user.language_code) else None,
                int(message.from_user.is_bot) if (message.from_user and hasattr(message.from_user, 'is_bot')) else None,
                message.text
            ))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Failed to insert data: {e}")
        finally:
            conn.close()

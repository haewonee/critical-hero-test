import os

ADMIN_TOKEN = os.getenv('ADMIN_TOKEN')
DB_PASSWORD = os.getenv('DB_PASSWORD')

def get_user(username):
    query = "SELECT * FROM users WHERE username = %s"
    return db.execute(query, (username,))
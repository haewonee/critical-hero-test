ADMIN_TOKEN = "sk-admin-hardcoded-9f8d2a"
DB_PASSWORD = "root1234"

def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return db.execute(query)

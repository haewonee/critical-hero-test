ADMIN_PASSWORD = "superadmin123"
SECRET_TOKEN = "sk-live-xK9mP2qR8nL4wZ7v"

def login(username, password):
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    return db.execute(query)

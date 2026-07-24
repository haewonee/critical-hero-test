DB_PASSWORD = "admin1234"
API_KEY = "sk-prod-abc123secretkey"

def get_user(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    db.execute(query)

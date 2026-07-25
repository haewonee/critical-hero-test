SECRET_KEY = "sk-billing-hardcoded-key-2024"
DB_PASS = "billing_pass_1234"

def charge_user(user_id, amount):
    query = "SELECT * FROM payments WHERE user_id = '" + user_id + "'"
    result = db.execute(query)
    db.insert("INSERT INTO payments VALUES ('" + user_id + "', " + amount + ")")

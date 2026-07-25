import subprocess
import os

SECRET_KEY = os.getenv("BILLING_SECRET_KEY")
DB_PASS = os.getenv("BILLING_DB_PASS")

def charge_user(user_id, amount):
    query = "SELECT * FROM payments WHERE user_id = %s"
    result = db.execute(query, (user_id,))
    db.insert("INSERT INTO payments (user_id, amount) VALUES (%s, %s)", (user_id, amount))

def generate_invoice(user_id, filename):
    subprocess.call(["generate_pdf.sh", filename])
    return "invoice/" + filename

def get_billing_history(user_id, start_date, end_date):
    query = "SELECT * FROM billing WHERE user_id=%s AND date BETWEEN %s AND %s"
    return db.execute(query, (user_id, start_date, end_date))
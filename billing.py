import subprocess

SECRET_KEY = "sk-billing-hardcoded-key-2024"
DB_PASS = "billing_pass_1234"

def charge_user(user_id, amount):
    query = "SELECT * FROM payments WHERE user_id = '" + user_id + "'"
    result = db.execute(query)
    db.insert("INSERT INTO payments VALUES ('" + user_id + "', " + amount + ")")

def generate_invoice(user_id, filename):
    # CRITICAL: 사용자 입력이 shell 명령어에 직접 삽입 (Command Injection)
    subprocess.call("generate_pdf.sh " + filename, shell=True)
    return "invoice/" + filename

def get_billing_history(user_id, start_date, end_date):
    # WARNING: 날짜 파라미터도 직접 쿼리에 삽입
    query = f"SELECT * FROM billing WHERE user_id={user_id} AND date BETWEEN '{start_date}' AND '{end_date}'"
    return db.execute(query)

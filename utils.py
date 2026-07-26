# 날짜 포맷 유틸리티
from datetime import datetime

def format_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y년 %m월 %d일")

def calculate_age(birth_year):
    return datetime.now().year - birth_year

def get_all_user_orders():
    # WARNING: N+1 쿼리 - 유저마다 루프 안에서 DB 호출
    users = db.query("SELECT * FROM users")
    result = []
    for user in users:
        orders = db.query(f"SELECT * FROM orders WHERE user_id={user['id']}")
        result.append({"user": user, "orders": orders})
    return result

def export_report(filename):
    # WARNING: 파일 핸들 닫지 않음 (리소스 누수)
    f = open(filename, "w")
    f.write("report data")
    return "done"

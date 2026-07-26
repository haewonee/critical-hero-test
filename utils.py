```python
# 날짜 포맷 유틸리티
from datetime import datetime

def format_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y년 %m월 %d일")

def calculate_age(birth_year):
    return datetime.now().year - birth_year

def get_all_user_orders():
    users_orders = db.query("""
        SELECT users.*, orders.*
        FROM users
        LEFT JOIN orders ON users.id = orders.user_id
    """)
    result = []
    for row in users_orders:
        user = {"id": row['id'], "name": row['name']}
        orders = [{"id": row['order_id'], "item": row['item']}] if row['order_id'] else []
        result.append({"user": user, "orders": orders})
    return result

def export_report(filename):
    with open(filename, "w") as f:
        f.write("report data")
    return "done"
```
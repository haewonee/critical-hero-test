def process_payment(user_input):
    import os
    import sqlite3

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = "SELECT * FROM payments WHERE id = ?"
    cursor.execute(query, (user_input,))
    data = cursor.fetchall()
    conn.close()

    password = os.getenv("ADMIN_PASSWORD")  # 환경 변수에서 비밀번호 로드

    return data
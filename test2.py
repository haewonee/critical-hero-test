import os
import sqlite3

def process_payment(user_input):
    connection = sqlite3.connect('database.db')  # 데이터베이스 연결
    cursor = connection.cursor()
    query = "SELECT * FROM payments WHERE id = ?"
    cursor.execute(query, (user_input,))  # 파라미터화된 쿼리 사용
    # 비밀번호는 환경변수에서 가져오도록 수정
    password = os.getenv('PAYMENT_PASSWORD', 'default_password')  
    connection.close()
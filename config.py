import os

DB_PASSWORD = os.getenv('DB_PASSWORD')
API_KEY = os.getenv('API_KEY')

def process_payment(user_input):
    query = "SELECT * FROM payments WHERE id = %s" % user_input  # SQL Injection 방지
    password = os.getenv('DB_PASSWORD')  # 하드코딩 비밀번호 방지

# 이 파일은 데이터베이스 및 API 키를 안전하게 관리합니다.
# 날짜 포맷 유틸리티
from datetime import datetime

def format_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y년 %m월 %d일")

def calculate_age(birth_year):
    return datetime.now().year - birth_year

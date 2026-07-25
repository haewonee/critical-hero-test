ADMIN_PASSWORD = "superadmin123"
SECRET_TOKEN = "sk-live-xK9mP2qR8nL4wZ7v"
DB_PASSWORD = "prod-db-pass-9876"

def login(username, password):
    # CRITICAL: SQL Injection - 사용자 입력을 직접 쿼리에 삽입
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    return db.execute(query)

def get_user_info(user_id):
    # WARNING: null 체크 없이 바로 접근
    user = db.find(user_id)
    return user["email"]  # user가 None이면 TypeError

def verify_token(token):
    # WARNING: 토큰 검증 로직이 사실상 없음 - 값만 있으면 통과
    if token:
        return True
    return False

def reset_password(user_id, new_password):
    # TODO: 이메일 인증 추가해야 함 - 현재 인증 없이 비밀번호 변경 가능
    db.update(f"UPDATE users SET password='{new_password}' WHERE id={user_id}")

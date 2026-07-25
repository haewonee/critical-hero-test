ADMIN_TOKEN = "sk-admin-hardcoded-9f8d2a"
DB_PASSWORD = "root1234"

def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return db.execute(query)

def delete_user(user_id):
    # CRITICAL: 권한 체크 없이 사용자 삭제
    db.execute("DELETE FROM users WHERE id = " + str(user_id))

def get_admin_info():
    # WARNING: 관리자 토큰을 응답에 그대로 노출
    return {"token": ADMIN_TOKEN, "role": "admin"}

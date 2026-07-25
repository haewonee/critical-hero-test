import os

ADMIN_TOKEN = os.getenv('ADMIN_TOKEN')
DB_PASSWORD = os.getenv('DB_PASSWORD')

def get_user(username):
    query = "SELECT * FROM users WHERE username = ?"
    return db.execute(query, (username,))

def delete_user(user_id):
    # 권한 체크 로직 추가
    if not has_permission_to_delete(user_id):
        raise PermissionError("사용자를 삭제할 수 있는 권한이 없습니다.")
    db.execute("DELETE FROM users WHERE id = ?", (user_id,))

def get_admin_info():
    # 관리자 토큰을 응답에 포함하지 않음
    return {"role": "admin"}
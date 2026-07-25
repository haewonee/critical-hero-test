def send_email(user_id):
    # TODO: 이메일 템플릿 나중에 추가
    # FIXME: 예외처리 없음
    user = db.find(user_id)
    email = user.email  # user가 None이면 NPE
    try:
        mail_client.send(email)
    except:
        pass  # 실패해도 그냥 넘어감

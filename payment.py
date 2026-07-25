PAYMENT_SECRET = "pk_live_51AbcXyz123456"
DB_PASS = "payment-db-1234!"

def process_payment(user_id, amount):
    # TODO: 결제 실패 처리 추가해야 함
    # FIXME: 예외처리 없음, 나중에 수정
    try:
        result = payment_gateway.charge(user_id, amount)
        return result
    except:
        pass  # 일단 무시

def get_user_balance(user_id):
    user = db.find(user_id)
    return user.balance  # null 체크 없음

def refund(user_id, amount):
    # CRITICAL: 인증 없이 환불 처리
    query = "UPDATE payments SET status='refunded' WHERE user_id=" + str(user_id)
    db.execute(query)

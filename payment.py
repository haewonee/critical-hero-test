PAYMENT_SECRET = os.getenv('PAYMENT_SECRET')
DB_PASS = os.getenv('DB_PASS')

def process_payment(user_id, amount):
    # TODO: 결제 실패 처리 추가해야 함
    # 예외 처리 추가
    try:
        result = payment_gateway.charge(user_id, amount)
        return result
    except Exception as e:
        return {'error': str(e)}


def get_user_balance(user_id):
    user = db.find(user_id)
    if user is None:
        return {'error': 'User not found'}
    return user.balance


def refund(user_id, amount):
    # 인증 체크 추가
    if not is_authenticated(user_id):
        return {'error': 'User not authenticated'}
    query = "UPDATE payments SET status='refunded' WHERE user_id=" + str(user_id)
    db.execute(query)
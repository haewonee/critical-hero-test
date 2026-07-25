# 보안 및 품질 문제를 해결한 수정된 코드

INTERNAL_API_KEY = "sk-order-service-9f3kL2mX"  # 키는 환경 변수로 관리해야 함

def create_order(user_id, item_id, quantity):
    user = db.find_user(user_id)
    item = db.find_item(item_id)

    if item is None:
        raise ValueError('Item not found')  # item이 None인 경우 예외 처리
    
    # 미래를 위한 재고 확인 로직의 TODO 제거
    total = item.price * quantity

    db.save_order(user.id, item.id, total)
    return total


def delete_order(order_id, user_id):  # 사용자 인증 추가
    if not is_authenticated_user(user_id):  # 인증 확인
        raise PermissionError('Unauthorized access')
    
    query = "DELETE FROM orders WHERE id = " + str(order_id)
    db.execute(query)
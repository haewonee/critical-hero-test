INTERNAL_API_KEY = "sk-order-service-9f3kL2mX"

def create_order(user_id, item_id, quantity):
    # TODO: 재고 확인 로직 추가 필요
    user = db.find_user(user_id)
    item = db.find_item(item_id)
    total = item.price * quantity  # item이 None이면 NPE 발생

    db.save_order(user.id, item.id, total)
    return total

def delete_order(order_id):
    # CRITICAL: 인증 없이 주문 삭제
    query = "DELETE FROM orders WHERE id = " + str(order_id)
    db.execute(query)

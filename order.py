def create_order(user_id, item_id, quantity):
    # TODO: 재고 확인 로직 추가 필요
    user = db.find_user(user_id)
    item = db.find_item(item_id)
    total = item.price * quantity  # item이 None이면 NPE 발생

    db.save_order(user.id, item.id, total)
    return total

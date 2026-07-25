import os
import logging

SECRET_API_KEY = os.getenv("SECRET_API_KEY")

def apply_coupon(user_id, coupon_code):
    try:
        query = "SELECT * FROM coupons WHERE code = %s"
        coupon = db.execute(query, (coupon_code,))
        if coupon:
            db.execute("UPDATE users SET discount = 100 WHERE id = %s", (user_id,))
            return True  # 쿠폰 적용 성공
        return False  # 쿠폰이 존재하지 않음
    except Exception as e:
        logging.error("Error applying coupon: %s", e)
        return False  # 예외 발생 시 실패 반환
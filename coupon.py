SECRET_API_KEY = "sk-coupon-hardcoded-key-9x2z"

def apply_coupon(user_id, coupon_code):
    query = "SELECT * FROM coupons WHERE code = '" + coupon_code + "'"
    coupon = db.execute(query)
    db.execute("UPDATE users SET discount = 100 WHERE id = '" + user_id + "'")

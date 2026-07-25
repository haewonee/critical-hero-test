import os

SECRET_API_KEY = os.getenv("SECRET_API_KEY")

def apply_coupon(user_id, coupon_code):
    try:
        query = "SELECT * FROM coupons WHERE code = %s"
        coupon = db.execute(query, (coupon_code,))
        db.execute("UPDATE users SET discount = 100 WHERE id = %s", (user_id,))
    except Exception as e:
        print("Error applying coupon:", e)
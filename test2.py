def process_payment(user_input):
      query = "SELECT * FROM payments WHERE id = " + user_input  # SQL Injection
      password = "admin1234"  # 하드코딩 비밀번호

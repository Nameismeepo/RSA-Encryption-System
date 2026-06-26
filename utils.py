def display_keys(public_key, private_key):
    """نمایش کلیدها"""
    print("\n" + "="*50)
    print("🔑  کلیدهای تولید شده")
    print("="*50)
    print(f"کلید عمومی  (e, n): {public_key}")
    print(f"کلید خصوصی (d, n): {private_key}")
    print("="*50)

def display_encrypted(encrypted):
    """نمایش پیام رمزنگاری شده"""
    print("\n" + "="*50)
    print("🔒  پیام رمزنگاری شده")
    print("="*50)
    print(' '.join(map(str, encrypted)))
    print("="*50)

def display_decrypted(decrypted):
    """نمایش پیام رمزگشایی شده"""
    print("\n" + "="*50)
    print("🔓  پیام رمزگشایی شده")
    print("="*50)
    print(decrypted)
    print("="*50)

def get_user_input():
    """دریافت پیام از کاربر"""
    print("\n" + "="*50)
    print("   سیستم رمزنگاری RSA")
    print("="*50)
    message = input("\nپیام خود را وارد کنید: ")
    return message
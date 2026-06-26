from rsa_core import generate_keys, encrypt_message, decrypt_message
from utils import display_keys, display_encrypted, display_decrypted, get_user_input

def main():
    # دریافت پیام
    message = get_user_input()

    # تولید کلید
    print("\n⏳ در حال تولید کلیدها...")
    public_key, private_key = generate_keys()

    # نمایش کلیدها
    display_keys(public_key, private_key)

    # رمزنگاری
    print("\n⏳ در حال رمزنگاری...")
    encrypted = encrypt_message(message, public_key)
    display_encrypted(encrypted)

    # رمزگشایی
    print("\n⏳ در حال رمزگشایی...")
    decrypted = decrypt_message(encrypted, private_key)
    display_decrypted(decrypted)

    # بررسی صحت
    print("\n" + "="*50)
    if message == decrypted:
        print("✅  رمزنگاری و رمزگشایی با موفقیت انجام شد!")
    else:
        print("❌  خطا در فرآیند")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
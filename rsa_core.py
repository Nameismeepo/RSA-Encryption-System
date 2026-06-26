import random
import math

def is_prime(n):
    """بررسی اول بودن عدد"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_prime(bits=8):
    """تولید عدد اول تصادفی"""
    while True:
        num = random.randint(2**(bits-1), 2**bits)
        if is_prime(num):
            return num

def gcd(a, b):
    """بزرگترین مقسوم علیه مشترک"""
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """الگوریتم اقلیدس توسعه‌یافته"""
    if a == 0:
        return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    return g, y - (b // a) * x, x

def mod_inverse(e, phi):
    """محاسبه معکوس ضربی"""
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise ValueError("معکوس وجود ندارد")
    return x % phi

def generate_keys():
    """تولید کلیدهای عمومی و خصوصی"""
    p = generate_prime(bits=8)
    q = generate_prime(bits=8)
    while q == p:
        q = generate_prime(bits=8)

    n = p * q
    phi = (p - 1) * (q - 1)

    # انتخاب e
    e = 65537
    if e >= phi or gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

def encrypt_message(message, public_key):
    """رمزنگاری پیام"""
    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted

def decrypt_message(encrypted, private_key):
    """رمزگشایی پیام"""
    d, n = private_key
    decrypted = [chr(pow(char, d, n)) for char in encrypted]
    return ''.join(decrypted)
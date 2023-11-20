import random
import math

def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def inverse(e, phi_n):
    for d in range(3, phi_n):
        if (d * e) % phi_n == 1:
            return d
    raise ValueError("Could not generate the inverse")

def generate_prime(min_n, max_n):
    p = random.randint(min_n, max_n)
    while not is_prime(p):
        p = random.randint(min_n, max_n)
    return p

def generate_public_key(phi_n):
    e = random.randint(3, phi_n-1) 
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n-1)
    return e

def generate_private_key(e, phi_n):
    return inverse(e, phi_n)

if __name__=="__main__":
    p = generate_prime(3, 9999)
    q = generate_prime(3, 9999)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = generate_public_key(phi_n)
    d = generate_private_key(e, phi_n) 

    msg = "Radu Calin"
    print(f"Original Message: {msg}")
    msg_enc = [ord(c) for c in msg]
    print(f"Converted message to decimal: {''.join(str(c) for c in msg_enc)}")

    cipher = [pow(c, e, n) for c in msg_enc]
    print(f"Cipher text is: {''.join(str(c) for c in cipher)}")

    msg_dec = [pow(c, d, n) for c in cipher]
    print(f"Converted decrypted message to decimal: {''.join(str(c) for c in msg_dec)}")
    msg = "".join(chr(c) for c in msg_dec)
    print(f"Decrypted Message: {msg}")
import random

#theory: https://www.youtube.com/watch?v=M1bq-LSnKPI

# should be a large prime number
p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039

# should be 1 < g < p
g = 2

# x = random.randint(1, p) 
x = 1234
y = pow(g, x, p)

pub_key = (p, g, y)
print(f"Public Key: {pub_key}")
priv_key = (p, x)


msg = "Radu Calin"
print(f"Original Message: {msg}")
msg_enc = [ord(c) for c in msg]
print(f"Encoded Message to decimal format: {msg_enc}")


# k = random.randint(1, p)
k = 4321

A = pow(g, k, p) 
print(f"A: {A}")
B = [(c * pow(y, k, p)) % p for c in msg_enc]
print(f"B: {B}")


msg_dec = [(c * pow(pow(A, x, p), -1, p)) % p for c in B]
print(f"Decrypted Message: {msg_dec}")
print(f"Decoded decrypted Message: {''.join(chr(c) for c in msg_dec)}")
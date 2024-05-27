import math
import decimal
import time

decimal.getcontext().prec = 100

def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp
 
 
p = decimal.Decimal(int(input("p = " )))
q = decimal.Decimal(int(input("q = " )))
n = decimal.Decimal(p*q)
e = decimal.Decimal(2)
phi = decimal.Decimal((p-1)*(q-1))

print("n = ",n)
print("phi = ",phi)
 
while (e < phi):
 
    # e must be co-prime to phi and
    # smaller than phi.
    if(gcd(e, phi) == 1):
        break
    else:
        e = e+1
print("e = ",e)

# Private key (d stands for decrypt)
# choosing d such that it satisfies
# d*e = 1 + k * totient (d*e = 1 mod Phi / yani Euler Phi sağlasın diye)
 
k = decimal.Decimal(2)
d = decimal.Decimal((1 + (k*phi))/e)
 
# Şifrelenecek Mesaj
msg = int(input("Message Data = "))

start_time = time.perf_counter() * 1000

# Şifreleme c = (msg ^ e) % n
c = pow(msg, int(e), int(n))
print("Encrypted data =", c)

end_time = time.perf_counter() * 1000
total_time = end_time - start_time

print("Encryption time : ", total_time, "Miliseconds")

start_time = time.perf_counter() * 1000

# Deşifreleme m = (c ^ d) % n
m = pow(c, int(d), int(n))
print("Original Message Sent = ", m)

end_time = time.perf_counter() * 1000
total_time = end_time - start_time

print("Decryption time : ", total_time, "Miliseconds")
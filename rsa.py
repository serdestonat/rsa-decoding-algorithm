import math
import time

# gcd hesaplama

def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp

p = int(input("p = "))
q = int(input("q = "))
n = p * q
e = int(input("e = "))
phi = (p - 1) * (q - 1)

print("n = ", n)
print("phi = ", phi)

while gcd(e, phi) != 1:
    e += 1

# e değeri excel değerinde verildiği için elimizde olan
# e değerinden hareketle "d*e = 1 mod phi" olacak şekilde d hesaplıyoruz

start_time = time.perf_counter() * 1000  # süre başlangıcı

d = pow(e, -1, phi)
print("d = ", d)

end_time = time.perf_counter() * 1000  # süre bitişi
total_time = end_time - start_time  # süre hesabı 

print("Gizli Anahtar Oluşturma Süresi : ", total_time, "Milisaniye")  # süre yazdırılması

# yukarıda verilen süre hesaplarını aşağıda metin şifrelerken ve deşifrelerken de kullanacağız.

# d hesaplama 

# Şifrelenecek Mesaj
msg = int(input("Şifrelenecek Mesaj = "))

start_time = time.perf_counter() * 1000

# Şifreleme c = (msg ^ e) % n
c = pow(msg, e, n)
print("Şifrelenmiş Mesaj =", c)

end_time = time.perf_counter() * 1000
total_time = end_time - start_time

print("Şifreleme Süresi : ", total_time, "Milisaniye")

start_time = time.perf_counter() * 1000

# Deşifreleme m = (c ^ d) % n
m = pow(c, d, n)
print("Gönderilmiş Orijinal Mesaj = ", m)

end_time = time.perf_counter() * 1000
total_time = end_time - start_time

print("Deşifreleme Süresi : ", total_time, "Milisaniye")

import random
import math
 
# A set will be the collection of prime numbers,
# where we can select random primes p and q
prime = [13,17,19,23,29,31,37,41,43,
        503,509,521,523,541,547,557,563,569,
        23663,23669,23671,23677,23687,23689,23719,23741,23743,
        569851,569861,569869,569887,569893,569897,569903,569927,569939,
        26985551,26985559,26985571,26985577,26985583,26985587,26985619,26985659,26985677,
        4771212547,4868747809,7373533723,7408868921,5949670231,3842610773,9731236789,9753236789,2999999929,
        10691097123712491259,11111111111111111011,11138479445180240497,12345678901234567891, 13337779797779999999, 
        20212223242526272829, 21576695089956874999,24681012141618202211, 36484957213536676883, 38775788043632640001, 
        43252003274489855999,44444444443333332221]
 
public_key = int(input("Public Key = " ))
private_key = None
n = None
 
# Picking a random prime number and erasing that prime
# number from list because p!=q
def pickrandomprime():
    global prime
    k = random.randint(0, len(prime) - 1)
    it = iter(prime)
    for _ in range(k):
        next(it)
 
    ret = next(it)
    prime.remove(ret)
    return ret
 
 
def setkeys():
    global public_key, private_key, n
    prime1 = pickrandomprime()  # First prime number
    prime2 = pickrandomprime()  # Second prime number
 
    n = prime1 * prime2
    phi = (prime1 - 1) * (prime2 - 1)
 
    e = public_key
    while True:
        if math.gcd(e, phi) == 1:
            break
 
    # d = (k*Φ(n) + 1) / e for some integer k
    public_key = e
 
    d = 2
    while True:
        if (d * e) % phi == 1:
            break
        d += 1
 
    private_key = d
 
 
# To encrypt the given number
def encrypt(message):
    global public_key, n
    e = public_key
    encrypted_text = 1
    while e > 0:
        encrypted_text *= message
        encrypted_text %= n
        e -= 1
    return encrypted_text
 
 
# To decrypt the given number
def decrypt(encrypted_text):
    global private_key, n
    d = private_key
    decrypted = 1
    while d > 0:
        decrypted *= encrypted_text
        decrypted %= n
        d -= 1
    return decrypted
 
 
# First converting each character to its ASCII value and
# then encoding it then decoding the number to get the
# ASCII and converting it to character
def encoder(message):
    encoded = []
    # Calling the encrypting function in encoding function
    for letter in message:
        encoded.append(encrypt(ord(letter)))
    return encoded
 
 
def decoder(encoded):
    s = ''
    # Calling the decrypting function decoding function
    for num in encoded:
        s += chr(decrypt(num))
    return s
 
 
if __name__ == '__main__':
    setkeys()
    message = int(input("Initial Message : " ))
    # Uncomment below for manual input
    # message = input("Enter the message\n")
    # Calling the encoding function
    coded = encoder(message)
 
    print("\n\nThe encoded message(encrypted by public key)\n")
    print(''.join(str(p) for p in coded))
    print("\n\nThe decoded message(decrypted by public key)\n")
    print(''.join(str(p) for p in decoder(coded)))
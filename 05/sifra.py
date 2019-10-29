key = 3
plaintext = input('Zadaj text:')
ciphertext = ''
for znak in plaintext:
    novyznak = znak
    if 'a' <= znak <= 'z':
        novyznak = chr( (ord(znak) - 97+key) % 26 + 97 )
        ciphertext = ciphertext+novyznak
print(ciphertext)
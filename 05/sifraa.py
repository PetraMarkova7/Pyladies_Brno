key = int(input('Zadaj klúč:'))
plaintext = input('Zadaj text:')
ciphertext = ''
for znak in plaintext:
    novyznak = znak
    if 'a' <= znak <= 'z':
        novyznak = chr( (ord(znak) + key - 97) % 26 + 97 )
        ciphertext = ciphertext+novyznak
print(ciphertext)
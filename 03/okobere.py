from random import randrange

cislo = 0
while cislo < 21:
    print('mám', cislo , 'bodov')
    odpoved = input('Otočit kartu? ')
    if odpoved == 'ano':
        karta = randrange(2, 11)
        cislo = cislo + karta
    elif odpoved == 'ne': 
        break
    else:
        print('zle')

print(cislo) 

cislo > 21
if cislo > 21:
    print('prehral si')
else:
    print('vyhral si')
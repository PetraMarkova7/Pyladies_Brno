from random import randrange

cislo = 0

# mám 5 a beriem dalšiu kartu
    
    print('mám', cislo , 'bodov')

    odpoved = input('Otočit kartu? ')

    if odpoved == 'ano':
        # beriem si kartu 5
        karta = randrange(2, 11)

        # spocítam  0 + 5
        cislo = cislo + karta

    elif odpoved == 'ne': 
        break

    else:
        print('zle')


    # mám 22 a prehrala som
    print('mám', cislo , 'bodov')



print(cislo) 

cislo > 21
if cislo > 21:
    print('prehral si')
else:
    print('vyhral si')
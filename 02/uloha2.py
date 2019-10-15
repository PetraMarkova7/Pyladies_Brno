tah_pocitaca = 'kamen'
tah_cloveka = input('kamen, nožnice, nebo papier? ')
if tah_cloveka == tah_pocitaca:
    print('Remíza.')
elif (tah_cloveka == 'kamen'and tah_pocitace == 'papier') or (tah_cloveka == 'papier'and tah_pocitaca == 'nožnice') or (tah_cloveka == 'nožnice'and tah_pocitaca == 'kamen'):
    print('Počítač vyhral.')
elif (tah_cloveka == 'kamen'and tah_pocitace == 'nožnice') or (tah_cloveka == 'papier'and tah_pocitaca == 'kamen') or (tah_cloveka == 'nožnice'and tah_pocitaca == 'papier'):
    print('Človek vyhral.')
else:
    print('Nerozumím.')
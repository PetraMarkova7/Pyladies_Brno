stastna_retezec = input('Jsi šťastná?')
bohata_retezec = input('Jsi bohatá?')

if stastna_retezec == 'ano':
    if bohata_retezec == 'ano':
        print ("ty se máš")
    elif bohata_retezec == 'ne':
        print ("zkus mín utrácet")
elif stastna_retezec == 'ne':
    if bohata_retezec == 'ano':
        print ("zkus se víc usmívat")
    elif bohata_retezec == 'ne':
        print ("to je mi líto")
else:
    print ("Nerozumím.")
from math import pi

def obsah_elipsy(a,b):
    "Vráti obsah elipsy daných rozmerov"
    return pi * a * b

print(obsah_elipsy(5,2))     

def objem_eliptickeho_valce(a,b, vyska):
    return pi * a * b * vyska

print(objem_eliptickeho_valce(5,2,3))   
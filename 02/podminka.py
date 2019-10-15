strana = float(input('zadaj stranu stvorca v cm: '))
cislo_je_spravne = strana > 0
if cislo_je_spravne == True:
    print('obvod stvorca se stranou', strana, 'je', 4 * strana, 'cm')
    print('obsah stvorca se stranou 356 je', 356 * 356, 'cm2')
else:
    print('musi byt vescia nez 0')

print('dekujeme')
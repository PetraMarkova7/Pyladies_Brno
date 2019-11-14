hrac = "x"
pocitac = "o"

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif  "-" not in pole:
        return "!"
    else:
        return "-"

def tah(pole, cislo_policka, symbol):
    pole = list(pole)
    pole[cislo_policka] = symbol
    return "".join(pole)

def tah_hrace(pole):
    while True:
        cislo_policka = int(input("zadaj políčko: "))

        if cislo_policka >= 0 and cislo_policka < len(pole):
            if pole[cislo_policka] == "-":
                break 
            else:
                print("pole je obsadene")
        else: 
            print("mimo pole")

    return tah(pole, cislo_policka, hrac) 

def tah_pocitace(pole):
    for cislo_policka in range(len(pole)):
        if pole[cislo_policka] == "-":
            return tah(pole, cislo_policka, pocitac) 
    return pole


def piskvorky1D():
    pole = "--------------------"
    hraje = "pocitac"
    while True:
        print(pole, "hraje: ", hraje)
        if hraje == "pocitac":
            pole = tah_pocitace(pole) 
            hraje = "clovek"
        else:
            pole = tah_hrace(pole)
            hraje = "pocitac"

        vysledek_hry = vyhodnot(pole)
        if vysledek_hry == "x":
            print("vyhralo x")
            break
        if vysledek_hry == "o":
            print("vyhralo o")
            break
        if vysledek_hry == "!":
            print("remiza")
            break

piskvorky1D()


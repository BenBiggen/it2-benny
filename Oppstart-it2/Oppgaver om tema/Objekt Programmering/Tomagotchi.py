


Tomagotchis = {"Fido": {"sult":5, "energi":5, "glede":5}, "Pusur": {"sult":5, "energi":5, "glede":5}}

def tomagotchiInfo(navn):
    global valg
    print(f"{navn}: Sult {Tomagotchis[navn]["sult"]}, Energi {Tomagotchis[navn]["energi"]}, Glede {Tomagotchis[navn]["glede"]}")
    print("1: Mate, 2: Sove, 3: Leke, 0: Avslutt")
    valg = int(input("Velg:"))
    print("-----------------------------")
    

def main():
    global valg
    toma_valg = input("Hvilke Tomagotchi vil du se?:")
    while True:
        tomagotchiInfo(toma_valg)

        if valg == 0:
            print("Du tok livet av Fido")
            print("-----------------------------")
            break
        elif valg == 1:
            print("Du mater Fido")
            print("-----------------------------")
            mate()
            tiden_gaar()
        elif valg == 2:
            print("Du legger Fido til å sove")
            print("-----------------------------")
            sove()
            tiden_gaar()
        elif valg == 3:
            print("Du leker med Fido")
            print("-----------------------------")
            leke()
            tiden_gaar()
        else:
            print("Please velg 0, 1, 2 eller 3")
            print("-----------------------------")

def begrens(verdi):
    return max(0, min(10, verdi))

def tiden_gaar():
    global sult
    global glede
    sult = begrens(sult+1)
    glede = begrens(glede-1)


def mate():
    global sult
    global glede
    sult = begrens(sult-3)
    glede = begrens(glede+1)

def sove():
    global energi
    global sult
    energi = begrens(energi+4)
    sult = begrens(sult+1)

def leke():
    global energi
    global glede
    global sult
    if energi >= 2:
        glede = begrens(glede+3)
        energi = begrens(energi-2)
        sult = begrens(sult+1)
    else:
        print("Fido er for trøtt")
        print("-----------------------------")

main()

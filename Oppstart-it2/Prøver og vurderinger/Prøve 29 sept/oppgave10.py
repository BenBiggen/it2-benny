økter = []
øktlengder = []
def startmeny():
    print("--- Treningslogg ---")
    print("1: Registrer økt")
    print("2: Vis alle økter")
    print("3: Statistikk")
    print("4: Avslutt")
    try:
        menyValg = int(input("Velg: "))
        if menyValg == 1:
            registrerØkt()
        elif menyValg == 2:
            visØkter()
        elif menyValg == 3:
            statistikk()
        elif menyValg ==4:
            print("Du avsluttet økten din")
        else:
            print("Ugyldig tall, skriv inn 1, 2, 3 eller 4")
            startmeny()
    except ValueError:
        print("Ugyldig input, skriv inn 1, 2, 3 eller 4")
        startmeny()



def registrerØkt():
    gyldig = False
    aktivitet = input("Skriv inn aktivitet:").lower()

    while gyldig == False:
        try:
            lengde = int(input("Skriv inn lengden av økten i minutter:"))
            if lengde >= 0:
                gyldig = True
            else:
                gyldig = False
        except ValueError:
            gyldig = False

    økter.append(aktivitet)
    øktlengder.append(lengde)
    startmeny()

def visØkter():
    print("Økter:")
    lengde = len(økter)

    for i in range(lengde):
        print(f"{i+1}. {økter[i]}: {øktlengder[i]} min")
    startmeny()

def statistikk():
    antallØkter = len(økter)
    print(f"Du har {antallØkter} økter totalt")
    print(f"Du har trent i {sum(øktlengder)} minutter totalt")
    startmeny()

startmeny()








    
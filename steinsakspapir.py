import random

def valg():
    print("Stein:1, Saks:2, Papir:3")
    tall = int(input("Skriv inn 1, 2 eller 3 for stein, saks eller papir:"))

    tallhus = random.randint(1,3)
    print("")
    ssp("du", tall)
    ssp("huset", tallhus)
    if tall == tallhus:
        print("UAVGJORT")
    elif tall == 1 and tallhus == 2:
        print("DU VINNER")
    elif tall == 2 and tallhus == 3:
            print("DU VINNER")
    elif tall == 3 and tallhus == 1:
            print("DU VINNER")
    elif tallhus == 1 and tall == 2:
            print("HUSET VINNER")
    elif tallhus == 2 and tall == 3:
            print("HUSET VINNER")
    elif tallhus == 3 and tall == 1:
            print("HUSET VINNER")
    print("")
    valg()

def ssp(bruker, valg):
    if valg == 1:
        print(f"{bruker} har valgt stein")
    elif valg == 2:
        print(f"{bruker} har valgt saks")
    elif valg == 3:
        print(f"{bruker} har valgt papir")
    else:
        print("Ikke gyldig input, skriv 1, 2 eller 3 din nepe")
        valg()

valg()
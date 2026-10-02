gyldig = False

while gyldig == False:
    try:
        antall = int(input("Hvor mange biletter har du lyst å køpe:"))
        if antall <= 10 and antall > 0:
            gyldig = True
        elif antall > 10 or antall <= 0:
            print("Du skrev et ugyldig tall")
    except ValueError:
        print("Please skriv inn et heltall")

print(f"Bilettene din vil koste {antall*150} kr")
    
    
    
    

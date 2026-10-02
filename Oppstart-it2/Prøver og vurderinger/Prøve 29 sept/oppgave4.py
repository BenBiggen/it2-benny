alder = int(input("Skriv inn alder:"))
if alder < 0 or alder > 120:
    print("Ingen bilett på deg småtten, du er under 0 eller over 120")
elif alder < 12:
    print("Biletten koster 80 kr")
elif alder <= 30:
    bevis = int(input("Har du student bevis? Skriv 1 for ja, og 2 for nei:"))
    if bevis == 1:
        print("du har gyldig studentbevis")
        print("Biletten koster 110 kr")
    else:
        print("du har ikke gyldig studentbevis")
elif alder < 67:
    print("Biletten koster 150 kr")
elif alder >= 67: 
    print("Biletten koster 100 kr")

alder = input("Hvor gammel er du? ")

if alder >= 18 #her mangler det kolon
    print("Du er myndig.")
elif alder = 17: #her skal det være to er lik tegn
    print("Du blir myndig neste år!")
else:
    print(f"Du blir myndig om {18 - alder} år.")

#rettet:
alder = input("Hvor gammel er du? ")

if alder >= 18:
    print("Du er myndig.")
elif alder == 17:
    print("Du blir myndig neste år!")
else:
    print(f"Du blir myndig om {18 - alder} år.")
#når json filen er i samme mappe:
import json

with open("data.json", "r") as fil:
    data = json.load(fil)

print(data)

#når json filen IKKE er i samme mappe men samme struktur:
#for å få denne strukturen må man bare høyre klikke og ta copy relative path
#import json

with open("../data/data.json", "r") as fil:
    data = json.load(fil)

print(data)
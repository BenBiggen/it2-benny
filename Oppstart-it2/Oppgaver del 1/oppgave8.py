import math

radius=float(input("Skriv inn radius til en sirkel:"))

def regnUtSirkelOmkrets(radius):
    omkrets=radius*2*math.pi
    return omkrets

print(regnUtSirkelOmkrets(radius))
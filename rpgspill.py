import random

roomCommonLoot = ["Vanlig Sverd", "Vanlig Bue", "Vanlig Spyd"]
roomRareLoot = ["Sjeldent Sverd", "Sjelden Bue", "Sjeldent spyd"]
roomLegendaryLoot = ["Legendarisk Flamme Sverd", "Legendarisk Skarpt Spyd", "Legendarisk Sterk Bue"]
enemies = ["Farlig Gnom", "Kjempe Stor Kjempe"]
heldWeapon = "a"



def choiceYN():
    gyldigInput = False

    while not gyldigInput:
        yesno = input("[Y, N]: ")
        positiveAlternativer = ["Y","y","yes", "Ja"]
        negativeAlternativer = ["N","n","No","Nei"]

        if yesno in positiveAlternativer:
            gyldigInput = True
            yesno = "Y"
        elif yesno in negativeAlternativer:
            gyldigInput = True
            yesno="N"
        else:
            gyldigInput = False
            print("Invalid Input (Y, N)")

    return yesno

def weaponEquip(weapon):
    if heldWeapon != weapon:
        heldWeapon = weapon

def damageEnemy():
    if heldWeapon in roomCommonLoot:
        dmgMultiplier = 1
    elif heldWeapon in roomRareLoot:
        dmgMultiplier = 2
    elif heldWeapon in roomLegendaryLoot:
        dmgMultiplier = 4

    damage = random.randint(1, 3)*dmgMultiplier
        

def lootEncounter(lootTable):
    lootFind = random.choice(lootTable)
    print (f"Du trakk {lootFind}, vil du bytte ut våpenet ditt?")
    if choiceYN() == "Y":
        weaponEquip(lootFind)
        return lootFind
    

#def roomEncounter():

print(lootEncounter(roomCommonLoot))

import random

roomCommonLoot = ["Vanlig Sverd", "Vanlig Bue", "Vanlig Spyd"]
roomRareLoot = ["Sjeldent Sverd", "Sjelden Bue", "Sjeldent spyd"]
roomLegendaryLoot = ["Legendarisk Flamme Sverd", "Legendarisk Skarpt Spyd", "Legendarisk Sterk Bue"]
    
def choiceYN():
    gyldigInput = False

    while not gyldigInput:
        yesno = input("[Y, N]:")
        positiveAlternativer = ["Y","y","yes", "Ja"]
        negativeAlternativer = ["N","n","No","Nei"]

        if yesno in positiveAlternativer:
            print("positivt innstilt")
            gyldigInput = True
        elif yesno in negativeAlternativer:
            print("negativ")
            gyldigInput = True
        else:
            gyldigInput = False
        

def lootEncounter(lootTable):
    return random.choice(lootTable)

#def roomEncounter():

choiceYN()

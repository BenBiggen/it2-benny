def er_sterkt_passord(passord):
    gyldighetLengde = False
    gyldighetSiffer = False
    gyldighetBokstav = False
    str(passord)
    lengde = len(passord)
    if lengde >= 8:
        gyldighetLengde = True

    for i in range(lengde):
        tegn = passord[i]
        if tegn.isdigit():
            gyldighetSiffer = True
        if tegn.isupper():
            gyldighetBokstav = True

    if gyldighetLengde == True and gyldighetSiffer == True and gyldighetBokstav == True:
        return True
    else:
        return False

print(er_sterkt_passord("hemmelig"))
print(er_sterkt_passord("Hemmelig"))
print(er_sterkt_passord("Hemmelig1"))


poeng = {"Ada": 42, "Linus": 17, "Grace": 58, "Alan": 17, "Guido": 33}
antall = len(poeng)
deltakere = ["Ada", "Linus", "Grace", "Alan", "Guido"]


for i in range(antall):
    deltaker = deltakere[i]
    poengsum = poeng[deltaker]
    print(f"{deltaker} har {poengsum} poeng")
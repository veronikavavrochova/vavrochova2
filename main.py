ovoce = {
    "nazev":"pomeranč",
    "cena":10,
    "fresh":True,
    "cenyTentoMěsíc":[10,15,12],
    "obchodCena":{"Lidl":12, "Penny":15, "Albert":10}
}

znamky = {
    "Anna":[1,2,4,5],
    "Josef":[2,3,4]
}

studenti = {
    "Anna":{"vek":16, "trida":"1A","znamky":{"matika":[1,2,3], "čeština":[3,2,1]}},
    "David":{"vek":18, "trida":"4A","znamky":{"matika":[4,5,3], "čeština":[3,3,1]}},
    "Roman":{"vek":15, "trida":"1A","znamky":{"matika":[1,2,1], "čeština":[4,2,1]}}
}

trida = studenti["Anna"]["trida"]
print(trida)

znamky = studenti["David"]["znamky"]["matika"]
soucetZnamek = sum(znamky)
prumer = soucetZnamek/3
print(prumer)

for student, hodnota in studenti.items():  
    znamky = hodnota["znamky"]["matika"]
    print(sum(znamky)/len(znamky))

for student, hodnota in studenti.items():
    trida = hodnota["trida"]
    if trida=="1A":
        print(f"Student {student} je z 1.A")

for student, hodnota in studenti.items():
    print(hodnota)
    hodnota["dochazka"] = "100%"
    print(hodnota)
for student, hodnota in studenti.items():
    hodnota["znamky"]["matika"].append(2)
    print(hodnota["znamky"]["matika"])

import random 
mm = ["oranje","bruin","blauw","groen"]
zak= [ ]
aantal = int(input("hoeveel m&m's wilt u? "))
damm={

    "groen":0,
    "blauw":0,
    "oranje":0,
    "bruin":0
}
color1 = 0
color2 = 0
color3 = 0
color4 = 0

def aantalmm():
    damm["groen"] = color1
    damm["blauw"] = color2
    damm["oranje"] = color3
    damm["bruin"] = color4

def randommenm():
    global zak, color1,color2,color3,color4
    for x in range(aantal):
        randommm=random.choice(mm)
        zakm = randommm
        zak.append(randommm)
        mm.append(zakm)
        color1 += zakm.count("groen")
        color2 += zakm.count("blauw")
        color3 += zakm.count("oranje")
        color4 += zakm.count("bruin")
        


randommenm()
aantalmm()
print(damm)
print(zak)
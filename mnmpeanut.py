import random 
mm = ["oranje","bruin","blauw","groen"]
aantal = int(input("hoeveel m&m's wilt u? "))


def MnM():
    global damm
    
    damm={}

    for x in range(aantal):
        color = random.choice(mm)
        if color in damm:
            damm[color]+=1
        else:
            damm[color]=1


MnM()
print(damm)
import random 
mm = ["oranje","bruin","blauw","bruin"]
aantal = int(input("hoeveel m&m's wilt u? "))
b = []

def randommenm(aantal):
    
    for x in range (aantal):
        zakm = random.choice(mm)
        b.append(zakm)
    print (*b)    


randommenm(aantal)
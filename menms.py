import random 
mm = ["oranje","bruin","blauw","bruin"]

aantal = int(input("hoeveel m&m's wilt u? "))

def randommenm(aantal):
    for x in range (aantal):
        zakm = random.choice(mm)
        print(zakm)

randommenm(aantal)
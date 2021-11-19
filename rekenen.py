getal_1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
getal_2 = [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
plust =["+","+","+","+","+","+","+","+","+","+"]
isteken =["=","=","=","=","=","=","=","=","=","="]
mint =["-","-","-","-","-","-","-","-","-","-"]
keert =["x","x","x","x","x","x","x","x","x","x",]
gedeeldt=[":",":",":",":",":",":",":",":",":",":",]
def plus():
    print()
    print("-----------------")
    print("  add list")
    eind = [a + b for a, b in zip(getal_1, getal_2)]
    pluslist = [getal_1, plust, getal_2,isteken, eind]

    for a in zip(*pluslist):
        print(*a)




def min():
    print()
    print("-----------------")
    print("  subract list")
    eind = [a - b for a, b in zip(getal_1, getal_2)]
    minlist =[getal_1,mint, getal_2, isteken, eind]
    for a in zip(*minlist):
        print(*a)

def keer():
    print()
    print("-----------------")
    print("  multiply list")
    eind = [a * b for a, b in zip (getal_1, getal_2)]
    keerlist = [getal_1,keert,getal_2,isteken,eind]
    for a in zip(*keerlist):
        print(*a)
def gedeeld():
    print()
    print("-----------------")
    print("  divide list")
    eind = [a / b for a, b in zip(getal_1, getal_2)]
    gedeeldlist =[getal_1, gedeeldt, getal_2, isteken, eind]

    for a in zip(*gedeeldlist):
        print(*a)



plus()
min()
keer()
gedeeld()
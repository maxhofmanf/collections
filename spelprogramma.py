import random
spellist = ['monopoly','yathzee','bridge','poker','pesten','mens erger je niet','cluedo']

def spelProgramma(spellist,minimum, maximum):
    num =random.randrange(minimum, maximum)
    for x in range (num):
        print(random.choice(spellist))

spelProgramma(spellist,3,10)
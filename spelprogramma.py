import random
spel = ['monopoly','yathzee','bridge','poker','pesten','mens erger je niet','cluedo']
num =random.randrange(3, 10)
for x in range (num):
    print(random.choice(spel))

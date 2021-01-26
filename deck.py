
import random
import itertools
hand=[]
dealer=[]
betting_amount=g

g=int(input("new game y/n"))
if g == "yes":
    cardvalue = ["2","3","4","5","6","7","8","9","10","Ace","Jack","Queen","King"]
    cardsuit = ["Of diamonds", "Of clubs", "Of spades", "Of hearts"]

    deck = list(itertools.product(cardvalue, cardsuit))
    random.shuffle(deck)

    x = (random.choice(deck))
    print(x)
else:
    print("no game")




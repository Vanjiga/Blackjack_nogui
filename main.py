#imports
import random
import itertools

#global varriales 
hand=[]
dealer=[]
starter_hand = 2
i = 0

#starter logic
g=int(input("new game? 1 yes 0 no "))
if g > 0:
    #card deck
    print("game")
    cardvalue = ["2","3","4","5","6","7","8","9","10","Ace","Jack","Queen","King"]
    cardsuit = ["Of diamonds", "Of clubs", "Of spades", "Of hearts"]

    deck = list(itertools.product(cardvalue, cardsuit))
    random.shuffle(deck)
    #output
    x = (random.choice(deck))
    for i in starter_hand:
        hand.append(x)
        print(hand)

else:
    print("no game")


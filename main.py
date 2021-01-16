#imports
import random
import itertools

#global varriales 
hand=[]
dealer=[]
sequence= 2

cardvalue = ["2","3","4","5","6","7","8","9","10","Ace","Jack","Queen","King"]
cardsuit = ["Of diamonds", "Of clubs", "Of spades", "Of hearts"]
deck = list(itertools.product(cardvalue, cardsuit))
random.shuffle(deck)
x = (random.choice(deck))




#starter logic
game_start = input(str("new game? y/n"))
if game_start == "y":
    for i in deck:
        x = (random.choice(deck))
        y = (random.choice(deck))
    hand.append(x)
    print(hand)
    dealer.append(y)
    print(dealer)
else:
   print("no game")
   
game_continue= input(str("Hit/Stand"))
if game_continue == "hit":
        x = (random.choice(deck))
        y = (random.choice(deck))

        hand.append(x)
        print(hand)
        dealer.append(y)
        print(dealer)
        
else:



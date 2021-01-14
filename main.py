import random
import itertools
product=()
cardvalue = ["1","2","3","4","5","6","7","8","9","10","Ace","Jack","Queen","King"]
cardsuit = ["Of diamonds", "Of clubs", "Of spades", "Of hearts"]

deck = list(itertools.product(cardvalue, cardsuit))
random.shuffle(deck)

print(random.choice(deck)
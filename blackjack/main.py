import random

cards = []
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])


# Shuffle the deck function
def shuffle():
    # From imported `random` library - randomize the cards
    random.shuffle(cards)


# Dealing the cards function
def deal(number):
    cards_dealt = []
    # Loops as many times as what is entered as `number`
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt


shuffle()
cards_dealt = (deal(2))
card = cards_dealt[0]

print(cards_dealt)
print(card)

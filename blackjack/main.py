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
    # Loops as many times as what is passed in  as `number`
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt


shuffle()
cards_dealt = (deal(2))
card = cards_dealt[0]
rank = card[1]

# Assign  rank it's  numerical value
if rank == "A":
    value = 11
elif rank == "K" or rank == "J" or rank == "Q":
    value = 10
else:
    value = rank

# Dictionary for rank and value
rank_dict = {
    "rank": rank,
    "value": value
}

print(cards_dealt)
print(card)
print(rank_dict["rank"], rank_dict["value"])

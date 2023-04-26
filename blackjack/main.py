import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):  # provide a string representation of an object.
        return f"{self.rank['rank']} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        # Dictionaries in a list
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "1", "value": 1},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):  # Shuffle the deck method
        # From imported `random` library - randomize the cards
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):  # Dealing the cards method
        cards_dealt = []
        # Loops as many times as what is passed in  as `number`
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt


class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)


deck = Deck()
deck.shuffle()

hand = Hand()
hand.add_card(deck.deal(2))
print(hand.cards[0])

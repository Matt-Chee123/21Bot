import random

class Card:
    def __init__(self,value,name,suit):
        self.value = value
        self.name = name
        self.suit = suit

    def __repr__(self):
        return f"{self.name} of {self.suit} {self.value}"

import random

class Deck:
    suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    names = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
    values = range(1, 14)

    def __init__(self, numDecks=1):
        self.cards = []
        for _ in range(numDecks):
            for suit in self.suits:
                for index,name in enumerate(self.names):
                    if index == 0:
                        self.cards.append(Card(11,name,suit))
                    elif index < 9:
                        self.cards.append(Card(index+1,name,suit))
                    else:
                        self.cards.append(Card(10,name,suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

deck = Deck()
deck.shuffle()
print(deck)

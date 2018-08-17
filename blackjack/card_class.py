from random import choice

class Card(object):
    def __init__(self, value, symbol):
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return '{0} of {1}s'.format(self.value, self.symbol)

class Card_Deck(object):
    def __init__(self):
        self.cards = []
        for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']:
            for symbol in ['Heart', 'Diamond', 'Spade', 'Club']:
                self.cards.append(Card(value, symbol))

    def deal_card(self):
        card = choice(self.cards)
        self.cards.remove(card)
        return card

class Hand(object):
    def __init__(self):
        self.cards = []

    def add_card(self, deck):
        self.cards.append(deck.deal_card())

    def __str__(self):
        rep = []
        for card in self.cards:
            rep.append(str(card))
        return str(rep)





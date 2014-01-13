from deck import Deck

from gin.gin_card import GinCard


class GinDeck(Deck):
    def __init__(self):
        self.cards = []

        for suit in ('Clubs', 'Spades', 'Hearts', 'Diamonds'):
            for value in (list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']):
                self.cards.append(GinCard(str(value), suit))



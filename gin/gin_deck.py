from deck import Deck

from gin.gin_card import GinCard


class GinDeck(Deck):
    def __init__(self):
        cards = []

        for suit in ('Clubs', 'Spades', 'Hearts', 'Diamonds'):
            for value in (list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']):
                cards.append(GinCard(str(value), suit))

        super(GinDeck, self).__init__(cards=cards)



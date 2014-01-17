from deck import Deck

from gin.gin_card import GinCard


class GinDeck(Deck):
    def __init__(self):
        cards = []

        for suit in ('♤', '♧', '♡', '♢'):
            for value in (list(range(2, 11)) + ['J', 'Q', 'K', 'A']):
                cards.append(GinCard(str(value), suit))

        super(GinDeck, self).__init__(cards=cards)



from base.deck import Deck

from gin.card import GinCard


class GinDeck(Deck):
    def __init__(self):
        from gin.controller import GinController

        cards = []

        for suit in GinController.SUITS:
            for value in (list(range(2, 11)) + ['J', 'Q', 'K', 'A']):
                cards.append(GinCard(str(value), suit))

        super(GinDeck, self).__init__(cards=cards)



from card import Card

class GinCard(Card):
    value   = None
    suit    = None

    def __init__(self, value, suit, *args, **kwargs):
        super(GinCard, self).__init__(*args, **kwargs)

        self.value = value
        self.suit = suit

    def __str__(self):
        return '{}{}'.format(self.suit, self.value)

    def __repr__(self):
        return self.__str__()

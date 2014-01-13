from card import Card

class GinCard(Card):
    value   = None
    suit    = None

    def __init__(self, value, suit, *args, **kwargs):
        super(GinCard, self).__init__(*args, **kwargs)

        self.value = value
        self.suit = suit

    def __str__(self):
        return '{} of {}'.format(self.value, self.suit)

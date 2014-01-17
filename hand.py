from card import Card

class Hand(object):
    cards = ()

    def __str__(self):
        return 'Hand:\n{}'.format(' '.join([str(card) for card in self.cards]))

    def __len__(self):
        return len(self.cards)

    def add(self, cards):
        # if handed a single card
        if isinstance(cards, Card):
            self.cards.append(cards)
        else:
            for card in cards:
                self.cards.append(card)

    def discard(self, pos):
        return self.cards.pop(pos)

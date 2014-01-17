from itertools import chain

def bridge_shuffle(cards, **kwargs):
    half = len(cards)//2

    stack_1 = cards[:half]
    stack_2 = cards[half:]

    return list(chain(*zip(stack_1, stack_2)))

def cut_deck(cards, pivot=0.5):
    half = int(len(cards) * pivot)

    stack_1 = cards[:half]
    stack_2 = cards[half:]

    return stack_2 + stack_1

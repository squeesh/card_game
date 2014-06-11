from random import random
from itertools import chain


def bridge_shuffle(cards, **kwargs):
    half = len(cards)//2

    stacks = [cards[:half], cards[half:]]
    draw_order = []
    output = []

    for i in range(len(cards)):
        draw_order.append(int(random() * 2))

    for i in draw_order:
        if len(stacks[i]):
            output.append(stacks[i].pop(0))
        else:
            output += stacks[0] + stacks[1]
            break

    return output


def cut_deck(cards, pivot=0.5):
    if pivot < 0.15:
        pivot = 0.15
    elif pivot > 0.85:
        pivot = 0.85

    half = int(len(cards) * pivot) + (int(random() * 7) - 3)

    stack_1 = cards[:half]
    stack_2 = cards[half:]

    return stack_2 + stack_1

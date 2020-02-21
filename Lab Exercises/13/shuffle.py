import random

def shuffle(cards):
    orig_cards = cards.copy()
    orig_len = len(orig_cards)
    for i in range(orig_len - 1, -1, -1):
        ran = random.randint(0, i)
        cards[i] = orig_cards[ran]
        del orig_cards[ran]


cards = list(range(54))
shuffle(cards)
print(cards)
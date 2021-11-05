from card import DokoCard

import numpy as np

def encode_cards(cards):
    plane = np.zeros(24, dtype=int)
    for card in cards:
        card_id = get_card_id(card)
        plane[card_id] += 1
    return plane


def get_card_id(card):
    rank_id = get_rank_id(card)
    suit_id = get_suit_id(card)
    return rank_id + 6 * suit_id

def get_rank_id(card):
    return DokoCard.valid_rank.index(card.rank)


def get_suit_id(card):
    return DokoCard.valid_suit.index(card.suit)
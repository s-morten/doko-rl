class DokoCard:

    valid_suit = ['S', 'H', 'D', 'C']
    valid_rank = ['A', '9', 'T', 'J', 'Q', 'K']

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.string = self.get_string()
        self.is_pig = False
        self.trump = self.isTrump()

    def get_string(self):
        return self.suit + "-" + self.rank

    def pig(self, pig):
        self.is_pig = pig

    def equal(self, card):
        if self.suit != card.suit or self.rank != card.rank:
            return False
        return True

    def higher(self, card):
        """ Compares self to a given Card. Returns True if self wins the Tick, False if the other Card wins the Tick """
        if self.trump and not card.trump: return True
        if not self.trump and card.trump: return False
        if self.trump and card.trump: return self.compareCardTrump(card)
        if self.suit != card.suit: return True
        else: return self.compareRank(card)


    def isTrump(self):
        if self.suit == 'D':
            return True

        if self.rank == 'Q' or self.rank == 'J':
            return True

        if self.rank == 'T' and self.suit == 'H':
            return True

        return False

    def compareSuit(self, card):
        if self.suit == 'C': return True
        else:
            if card.suit == 'C': return False
        if self.suit == 'S': return True
        else:
            if card.suit == 'S': return False
        if self.suit == 'H': return True
        else:
            if card.suit == 'H': return False
        return True
        

    def compareCardTrump(self, card):
        if self.is_pig: return True
        if card.is_pig: return False
        if card.rank == 'T' and card.suit == 'H': return False
        if self.rank == 'T' and self.suit == 'H': return True
        if self.rank == 'Q':
            if card.rank != 'Q': return True
            else:
                return self.compareSuit(card)
        if self.rank == 'J':
            if card.rank != 'J': return True
            else:
                return self.compareSuit(card)
        if self.rank == 'A': return True
        else:
            if card.rank == 'A': return False
        if self.rank == 'T': return True
        else:
            if card.rank == 'T': return False
        if self.rank == 'K': return True
        else:
            if card.rank == 'K': return False
        return True

    def compareRank(self, card):
        if self.rank == 'A': return True
        if self.rank == 'T' and card.rank != 'A': return True
        if self.rank == 'K' and card.rank != 'A' and card.rank != 'T': return True
        if self.rank == '9' and card.rank == '9': return True
        else: return False
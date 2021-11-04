class DokoCard:

    info = {'color':  ['H', 'C', 'D', 'S'],
            'number': ['9', '10', 'J', 'Q', 'K', 'A']}

    def __init__(self, color, number):

        self.color = color
        self.number = number
        self.string = self.get_string()
        self.is_pig = False
        self.trump = self.isTrump()

    def get_string(self):
        return self.color + "-" + self.number

    def pig(self, pig):
        self.is_pig = pig

    def equal(self, card):
        if self.color != card.color or self.number != card.number:
            return False
        return True

    def higher(self, card):
        """ Compares self to a given Card. Returns True if self wins the Tick, False if the other Card wins the Tick """
        if self.trump and not card.trump: return True
        if not self.trump and card.trump: return False
        if self.trump and card.trump: return self.compareCardTrump(card)
        if self.color != card.color: return True
        else: return self.compareNumber(card)


    def isTrump(self):
        if self.color == 'D':
            return True

        if self.number == 'Q' or self.number == 'J':
            return True

        if self.number == '10' and self.color == 'H':
            return True

        return False

    def compareSuit(self, card):
        if self.color == 'C': return True
        else:
            if card.color == 'C': return False
        if self.color == 'S': return True
        else:
            if card.color == 'S': return False
        if self.color == 'H': return True
        else:
            if card.color == 'H': return False
        return True
        

    def compareCardTrump(self, card):
        if self.is_pig: return True
        if card.is_pig: return False
        if card.number == '10' and card.color == 'H': return False
        if self.number == '10' and self.color == 'H': return True
        if self.number == 'Q':
            if card.number != 'Q': return True
            else:
                return self.compareSuit(card)
        if self.number == 'J':
            if card.number != 'J': return True
            else:
                return self.compareSuit(card)
        if self.number == 'A': return True
        else:
            if card.number == 'A': return False
        if self.number == '10': return True
        else:
            if card.number == '10': return False
        if self.number == 'K': return True
        else:
            if card.number == 'K': return False
        return True

    def compareNumber(self, card):
        if self.number == 'A': return True
        if self.number == '10' and card.number != 'A': return True
        if self.number == 'K' and card.number != 'A' and card.number != '10': return True
        if self.number == '9' and card.number == '9': return True
        else: return False
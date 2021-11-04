class DokoCard:

    info = {'color':  ['H', 'C', 'D', 'S'],
            'number': ['9', '10', 'J', 'Q', 'K', 'A']}

    def __init__(self, color, number):

        self.color = color
        self.number = number
        self.string = self.get_string()
        self.is_pig = False

    def get_string(self):
        return self.color + "-" + self.number

    def pig(self, pig):
        self.is_pig = pig

    def equal(self, card):
        if self.color != card.color or self.number != card.number:
            return False
        return True
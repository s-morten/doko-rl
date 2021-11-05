from card import DokoCard

class DokoDealer:
    def __init__(self, np_random):
        self.np_random = np_random
        self.decks_prepaired = False
        while not self.decks_prepaired:
            self.deck = self.init_deck()
            self.shuffle()
            self.decks_prepaired, self.prepared_decks = self.prep_deal()

    def shuffle(self):
        self.np_random.shuffle(self.deck)

    def init_deck(self):
        deck = []
        suits = DokoCard.valid_suit
        ranks = DokoCard.valid_rank

        for suit in suits:
            for rank in ranks:
                deck.append(DokoCard(suit, rank))
                deck.append(DokoCard(suit, rank))

        return deck

    def prep_deal(self):
        decks = []
        for _ in range(4):
            player = []
            for _ in range(12):
                player.append(self.deck.pop())
            if self.is_marriage(player):
                return False, None
            player = self.set_pig(player)
            decks.append(player)
        return True, decks        


    def is_marriage(self, cards):
        num_club_queens = 0
        cq = DokoCard('C', 'Q')
        for card in cards:
            if cq.equal(card):
                num_club_queens += 1
        if num_club_queens >= 2: 
            return True

    def set_pig(self, cards):
        num_diamond_ace = 0
        cq = DokoCard('D', 'A')
        for card in cards:
            if cq.equal(card):
                num_diamond_ace += 1
        if num_diamond_ace >= 2: 
            for card in cards:
                if cq.equal(card):
                    card.pig(True)

        return cards


    def deal_card(self, player):
        player.hand = self.prepared_decks.pop()

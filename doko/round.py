class DokoRound():
    def __init__(self, np_random, dealer):
        self.np_random = np_random
        self.current_player = dealer
        self.num_players = 4
        self.current_trick = []
        self.is_over = False
        self.winner = None
        self.rounds = 0

    def proceed_round(self, players, action):
        # from action to card?
        card = action
        self.current_trick.append(card)
        player = players[self.current_player]
        player.hand.remove(card)
        self.rounds += 1
        if self.rounds >= self.num_players:
            self.is_over = True
        else:
            self.current_player += 1 if (self.current_player < self.num_players-1) else 0

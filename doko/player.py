class DokoPlayer:
    def __init__(self, player_id, np_random):
        self.np_random = np_random
        self.player_id = player_id
        self.dealer = False
        self.hand = []
        self.tricks = []

    def set_dealer(self, is_dealer):
        self.dealer = is_dealer

    def get_player_id(self):
        return self.player_id
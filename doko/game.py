from round import DokoRound
from utils import encode_cards, get_card_id
from dealer import DokoDealer
from player import DokoPlayer
from round import DokoRound
import numpy as np
import math

class DokoGame:
    def __init__(self):
        self.nprandom = np.random.RandomState()
        self.num_players = 4
        self.all_played = []

    def init_game(self):
        self.dealer = DokoDealer(self.nprandom)

        self.players = [DokoPlayer(i, self.np_random) for i in range(self.num_players)]

        for player in self.players:
            self.dealer.deal_card(player)

        dealer = np.random.randint(0,4)
        self.round = DokoRound(self.nprandom, dealer)

        player_id = self.round.current_player

        state = self.get_state(player_id)

        return state, player_id

    def step(self, action):
        self.round.proceed_round(self.players, action)
        # from action to card
        self.all_played.append(card=action)
        player_id = self.round.current_player
        state = self.get_state(player_id)
        return state, player_id

    def get_state(self, player_id):
        state = {}

        state['player_id'] = self.round.current_player
        obs = np.zeros(24)
        for x in self.players[self.round.current_player].hand:
            obs[get_card_id(x)] += 1
        state['hand'] = obs
        obs = np.zeros(24)
        for x in self.all_played:
            obs[get_card_id(x)] += 1
        state['played'] = obs

        return state

    def get_legal_actions(self, player_id):
        legal_actions = []
        num_cards = len(self.all_played)
        completed_ticks = math.floor(num_cards/4)*4
        trick = self.all_played[completed_ticks:]
        hand = self.players[player_id].hand
        if len(trick) > 0:
            required_suit = trick[0].suit
            for card in hand:
                if card.suit == required_suit:
                    legal_actions.append(encode_cards(card))
            if not legal_actions:
                for card in hand:
                    legal_actions.append(encode_cards(card))

    def get_num_players(self):
        return 4

    def get_num_actions(self):
        return 12
from rlcard.envs import Env
from game import DokoGame
from utils import encode_cards

import numpy as np

DEFAULT_GAME_CONFIG = {
        'game_num_players': 4,
        }


class DokoEnv(Env):

    def __init__(self, config):
        self.name = 'Doppelkopf'
        self.default_game_config = DEFAULT_GAME_CONFIG
        self.game = DokoGame()
        super().__init__(config)
        self.state_shape = [[2, 24] for _ in range(self.num_players)]
        self.action_shape = [None for _ in range(self.num_players)]

    def _extract_state(self, state):
        current_player = self.game.round.current_player
        hand_cards = encode_cards(self.game.players[current_player].hand)
        played_cards = encode_cards(self.game.all_played)
        obs = np.array([hand_cards, played_cards])
        extracted_state = {'obs': obs, 'legal_actions': self._get_legal_actions(), 'raw_legal_actions': list(self._get_legal_actions().keys())}
        extracted_state['raw_obs'] = obs
        return extracted_state

    def _get_legal_actions(self):
        legal_actions = self.game.get_legal_actions(self.game.round.current_player)
        return legal_actions
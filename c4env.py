import gym
from gym import spaces
import numpy as np
from typing import List

from connectfour.game import Game, GAME_STATUS


class C4Env(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    board_width = 7
    board_height = 6
    game = Game(board_width, board_height)

    def __init__(self):
        super(C4Env, self).__init__()
        self.reset()
        # The player has the option to
        self.action_space = spaces.Discrete(self.board_width)
        # Example for using image as input:
        self.observation_space = spaces.Box(low=-1, high=1, shape=(self.board_width, self.board_height), dtype=np.int8)

    def step(self, action):
        # Execute one time step within the environment
        self.game.play(self.game.random_action(), self.game.current_player)
        

        reward = 0  # self.balance * delay_modifier
        
        done = self.game.get_status()
        
        obs = self.game.board
        return obs, reward, done, {}

    def reset(self):
        # Reset the state of the environment to an initial state
        self.game = Game(self.board_width, self.board_height)

    def render(self, mode='human', close=False):
        # Render the environment to the screen
        print()
        print(np.matrix(self.game.board).transpose())

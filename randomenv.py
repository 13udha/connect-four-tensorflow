import gym
from gym import spaces
import numpy as np
from typing import List
from colorama import init, Fore , Back , Style
from minmax import minmax,find_best_move
from c4env import C4Env
init()

from connectfour.game import Game, GAME_STATUS


class RandomEnv(C4Env):

    def step(self, action):
        # Execute one time step within the environment (each player makes a move)
        self.game.play(action, self.game.current_player)
        if (not self.game.get_status()):
            self.game.play(self.game.random_action(), self.game.current_player) 
    
        self.steps += 1
        reward = float(-self.game.winner) / self.steps 
        done = self.game.get_status()

        
        obs = self.game.board
        return obs, reward, done, {} #TODO was ist {}

    def reset(self):
        # Reset the state of the environment to an initial state
        self.game = Game(self.board_width, self.board_height)
        self.steps = 0
        if (self.game.current_player==1): # so ist immer der RL Agent als erstes im step dran und kann keinen illegalen zug machen wenn er als action das selbe feld wählt wie der Gegner
            self.game.play(self.game.random_action(), self.game.current_player) 
        return np.array(self.game.board)
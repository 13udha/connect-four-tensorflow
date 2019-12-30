import gym
from gym import spaces
import numpy as np
from typing import List
from colorama import init, Fore , Back , Style
from minmax import minmax,find_best_move
from c4env import C4Env
import pickle
init()

from connectfour.game import Game, GAME_STATUS


class RandomEnv(C4Env):

    def step(self, action):
        # Execute one time step within the environment (each player makes a move)
        self.game.play(action, self.game.current_player)
        if (not self.game.get_status()):
            self.game.play(self.game.random_action(), self.game.current_player) 
            self.game.get_status()
        self.steps += 1

        reward =self.boardchecker()

        #reward = float(-self.game.winner) / self.steps 

        done = self.game.get_status()
        if(done):
            self.reward_list.append(reward) 
            self.reward_file = open(self.reward_list_name, mode='wb')
            pickle.dump(self.reward_list,self.reward_file)
            self.reward_file.close()
        obs = self.game.board
        return obs, reward, done, {} #TODO was ist {}

    def reset(self):
        # Reset the state of the environment to an initial state
        self.game = Game(self.board_width, self.board_height)
        self.steps = 0
        if (self.game.current_player==1): # so ist immer der RL Agent als erstes im step dran und kann keinen illegalen zug machen wenn er als action das selbe feld wählt wie der Gegner
            self.game.play(self.game.random_action(), self.game.current_player) 
        return np.array(self.game.board)

    def boardchecker(self):
        #Anzahl der 2er,3er und 4er Ketten der Spieler werden verrechnet
        return (self.game.check_for_streak(-1,2) + (self.game.check_for_streak(-1,3)*10)+ (self.game.check_for_streak(-1,4)*1000))-(self.game.check_for_streak(1,2) + (self.game.check_for_streak(1,3)*10)+ (self.game.check_for_streak(1,4)*1000))
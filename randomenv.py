import gym
from gym import spaces
import numpy as np
from typing import List
from colorama import init, Fore , Back , Style
from minmax import minmax,find_best_move

init()

from connectfour.game import Game, GAME_STATUS


class RandomEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    board_width = 7
    board_height = 6
    game = Game(board_width, board_height)

    def __init__(self):
        super(RandomEnv, self).__init__()
        self.reset()
        # The player has the option to
        # action space kann nicht verändert werden daher besteht immer die möglichkeit in volle reihen zu werfen 
        self.action_space = spaces.Discrete(self.board_width)# wenn in voll -> verloren TODO oder die policy verändern dass es nicht mehr möglich ist
        # Example for using image as input:
        self.observation_space = spaces.Box(low=-1, high=1, shape=(self.board_width, self.board_height), dtype=np.int8)

    def step(self, action):
        # Execute one time step within the environment (each player makes a move)
        if(self.game.current_player==1):
            self.game.play(self.game.random_action(), self.game.current_player) 
            if(not self.game.get_status()):
                self.game.play(action, self.game.current_player)
        else:
            self.game.play(action, self.game.current_player)
            if(not self.game.get_status()):
                self.game.play(self.game.random_action(), self.game.current_player) 
        
        self.steps += 1
        reward = -self.game.winner / self.steps 
        
        done = self.game.get_status()
        
        obs = self.game.board
        return obs, reward, done, {} #TODO was ist {}

    def reset(self):
        # Reset the state of the environment to an initial state
        self.game = Game(self.board_width, self.board_height)
        self.steps = 0
        return np.array(self.game.board)

    def render(self, mode='human', close=False):
        # Render the environment to the screen
        input = np.fliplr(np.rot90(self.game.board, axes=(1,0)))

        print(Back.BLUE)
        for i in range(len(input)):
            for j in range(len(input[i])):
                if input[i][j]==-1:
                    print('\033[31m' + "\u25CF" , end =" ")
                elif input[i][j]==1:
                    print('\033[33m' + "\u25CF" , end =" ")
                else:
                    print('\033[30m' + "\u25CF" , end =" ")
            print(Style.RESET_ALL + '\x1b[K')
            print(Back.BLUE, end ="")
        print(Style.RESET_ALL+'\x1b[K')

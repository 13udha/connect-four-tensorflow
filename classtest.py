from connectfour.game import Game, GAME_STATUS
from minmax import minmax,find_best_move
import numpy as np
from colorama import init, Fore , Back , Style
import datetime

BOARD_WIDTH = 7
BOARD_HIGHT = 6
game = Game(BOARD_WIDTH, BOARD_HIGHT)
print(game.board)
# game.current_player= 1
# game.play(2, 1)
# game.play(2, -1)
# game.play(4, 1)
# game.play(4, -1)




# before = datetime.datetime.now()
# minmax(game,7)
# after = datetime.datetime.now()
# print(after-before)
print(find_best_move(minmax(game,4)))




input = np.fliplr(np.rot90(game.board, axes=(1,0)))

print(Back.BLUE, end ="")
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
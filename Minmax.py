from connectfour.game import Game, GAME_STATUS
import numpy as np
from colorama import init, Fore , Back , Style
import copy
import datetime

board_width = 7
board_height = 6
game = Game(board_width, board_height)

# game.play(3, game.current_player)
# game.play(2, game.current_player)
# game.play(3, game.current_player)
# game.play(2, game.current_player)
# # game.play(3, game.current_player)
# # game.play(2, game.current_player)
# # game.play(3, game.current_player)
# game.play(4, game.current_player)
# game.play(4, game.current_player)
# game.play(4, game.current_player)
# game.play(4, game.current_player)
# game.play(4, game.current_player)
# game.play(4, game.current_player)



def minmax(board,depth):
    depth -=1
    if board.get_status():
        return board.winner
    if depth > 0:
        chances = []
        for i in range(len(board.get_legal_moves())):
            if board.get_legal_moves()[i]:
                newboard = copy.deepcopy(board)
                nextmm = checknext(newboard,1)
                newboard.play(i, newboard.current_player)
                if any(nextmm):
                    chances.append(minmax(newboard,1))
                else:
                    chances.append(minmax(newboard,depth))
            else:
                chances.append(None)
        return chances
    else:
        return 0

def checknext(board, depth):
    if board.get_status():
        return board.winner
    elif depth > 0:
        chances = []
        for i in range(len(board.get_legal_moves())):
            if board.get_legal_moves()[i]:
                newboard = copy.deepcopy(board)
                newboard.play(i, newboard.current_player)
                chances.append(checknext(newboard,depth-1))
            else:
                chances.append(None)
        return chances
    else:
        return 0



before = datetime.datetime.now()
minmax(game,7)
after = datetime.datetime.now()
print(after-before)

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
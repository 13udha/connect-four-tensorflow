from connectfour.game import Game, GAME_STATUS
import numpy as np
from colorama import init, Fore , Back , Style
import copy
import datetime
import random

# BOARD_WIDTH = 7
# BOARD_HIGHT = 6
# game = Game(BOARD_WIDTH, BOARD_HIGHT)

# game.current_player= 1
# game.play(2, 1)
# game.play(2, -1)
# game.play(4, 1)
# game.play(4, -1)






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
        
def find_best_move(mmtree):
    moves = []
    for elem in mmtree:
        if isinstance(elem, list): 
            moves.append(go_deeper(elem))
        else:
            if elem != None:
                moves.append(elem)
    if moves.count(max(moves))==1:
        return moves.index(max(moves))  
    else:
        indices = [i for i, x in enumerate(moves) if x == max(moves)]
        #print (max(moves))
        #print (indices)
        return random.choice(indices)

def go_deeper(branch):
    chance = []
    for elem in branch:
        if isinstance(elem, list): 
            chance.append(go_deeper(elem))
        else:
            if elem != None:
                chance.append(elem)

    return (sum(chance)/len(chance)) 
   
# before = datetime.datetime.now()
# minmax(game,7)
# after = datetime.datetime.now()
# print(after-before)
# print(find_best_move(minmax(game,4)))



# input = np.fliplr(np.rot90(game.board, axes=(1,0)))

# print(Back.BLUE, end ="")
# for i in range(len(input)):
#     for j in range(len(input[i])):
#         if input[i][j]==-1:
#             print('\033[31m' + "\u25CF" , end =" ")
#         elif input[i][j]==1:
#             print('\033[33m' + "\u25CF" , end =" ")
#         else:
#             print('\033[30m' + "\u25CF" , end =" ")
#     print(Style.RESET_ALL + '\x1b[K')
#     print(Back.BLUE, end ="")
# print(Style.RESET_ALL+'\x1b[K')
import pickle
import matplotlib.pyplot as plt

filename = 'data'
winner = []
loser = []
equal = []
try:
    infile = open(filename,'rb')
    recorded_games = pickle.load(infile)
    infile.close()
except FileNotFoundError:
    recorded_games = [tuple()]

first,snd = zip(*recorded_games)
for i in range(len(first)):
    if first[i] == -1:
        loser.append((snd[i]))
        winner.append(None)
        equal.append(None)
    elif first[i] == 1:
        winner.append((snd[i]))
        loser.append(None)
        equal.append(None)
    else:
        equal.append((snd[i]))
        winner.append(None)
        loser.append(None)

plt.scatter(list(range(len(winner))),winner)
plt.scatter(list(range(len(loser))),loser)
plt.scatter(list(range(len(equal))),equal)
plt.show()
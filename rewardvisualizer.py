import pickle
import argparse
import matplotlib.pyplot as plt

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    
    rewardlist =pickle.load(open(args.filename, mode='rb'))
    plt.plot(list(range(len(rewardlist))),rewardlist, 'ro')
    plt.ylabel('reward')
    plt.show()
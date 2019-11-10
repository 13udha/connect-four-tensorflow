from rl.policy import EpsGreedyQPolicy
import numpy as np
import random

class EpsGreedyQPolicyC4(EpsGreedyQPolicy):

    def __init__(self,environment , eps=.1):
        super().__init__()
        self.environment = environment

    def select_action(self, q_values):
        """Return the selected action
        # Arguments
            q_values (np.ndarray): List of the estimations of Q for each action
        # Returns
            Selection action
        """
        legalmoves = self.environment.get_legal_moves()
        assert len(legalmoves) == q_values.shape[0]
        qdict = {}
        for i, move in enumerate(legalmoves):
            if move:
                qdict[i]= q_values[i]
        assert q_values.ndim == 1
        if(not self.environment.game.get_status()):
            if np.random.uniform() < self.eps:
                action = random.choice(list(qdict.keys()))
                #np.random.randint(0, nb_actions)
            else:
                action = max(qdict, key=qdict.get)#alles überspringen wenn board voll ist und random aktion?
        else:
            action = np.random.randint(0, q_values.shape[0])
        return action
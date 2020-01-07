import numpy as np
import gym
from c4env import C4Env
from randomenv import RandomEnv

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

#from rl.agents.dqn import DQNAgent
from rl.agents import SARSAAgent
from C4Policy import EpsGreedyQPolicyC4
#from rl.memory import SequentialMemory
import wandb
from wandb.keras import WandbCallback


config_defaults = dict(
    dropout = 0.2,
    hidden_layer_size = 128,
    layer_1_size = 16,
    layer_2_size = 32,
    learn_rate = 0.01,
    decay = 1e-6,
    momentum = 0.9,
    epochs = 25,
    )
    
wandb.init(config=config_defaults) 
# Config is a variable that holds and saves hyperparameters and inputs
config = wandb.config


# Get the environment and extract the number of actions.
env = RandomEnv()
np.random.seed(123)
env.seed(123)
nb_actions = env.action_space.n

# Each Layer has a Size of two times the boardsize
layersize = env.observation_space.shape[0] * env.observation_space.shape[1] * 2

results_path = './results/'
weights_filename = results_path + 'dqn_weights.h5f'

# Next, we build a very simple model.
model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Dense(layersize))
model.add(Activation('relu'))
model.add(Dense(layersize))
model.add(Activation('relu'))
model.add(Dense(layersize))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))
print(model.summary())

# Finally, we configure and compile our agent. You can use every built-in Keras optimizer and
# even the metrics!
#memory = SequentialMemory(limit=50000, window_length=1)
policy = EpsGreedyQPolicyC4(env)
# dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=10,
#                target_model_update=1e-2, policy=policy,test_policy=policy)
# dqn.compile(Adam(lr=1e-3), metrics=['mae'])
sarsa = SARSAAgent(model=model, nb_actions=nb_actions, nb_steps_warmup=10, policy=policy,test_policy=policy)
sarsa.compile(Adam(lr=1e-3), metrics=['mae'])

# Load weights
try:
    #dqn.load_weights(weights_filename)
    sarsa.load_weights(weights_filename)
except OSError:
    print("no saved weights found")
# Okay, now it's time to learn something! We visualize the training here for show, but this
# slows down training quite a lot. You can always safely abort the training prematurely using
# Ctrl + C.
#dqn.fit(env, nb_steps=5000000, visualize=False, verbose=2)
sarsa.fit(env, nb_steps=50000, visualize=False, verbose=1, callbacks=[WandbCallback()])

# After training is done, we save the final weights.
#dqn.save_weights('dqn_{}_weights.h5f'.format(ENV_NAME), overwrite=True)

# Finally, evaluate our algorithm for 5 episodes.
#dqn.test(env, nb_episodes=5, visualize=True)
sarsa.test(env, nb_episodes=5, visualize=True)

# Save weights
#dqn.save_weights(weights_filename, overwrite=True)
sarsa.save_weights(weights_filename, overwrite=True)
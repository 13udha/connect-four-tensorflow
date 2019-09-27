import gym
from c4env import C4Env

env = C4Env()
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        # print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print(f"Episode finished after {t+1} timesteps + action {action}")
            break
env.close()
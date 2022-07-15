import numpy as np
import gym
import time

#create environment
env=gym.make('CartPole-v1')

observation=env.reset()
print(observation)

#Reset environment
#4 observation
for _ in range(100):
    env.render()

import gymnasium as gym
from game_env import GameEnv

env = GameEnv()
env.reset()

for i in range(100):
    action = env.action_space.sample()
    env.step(action=action)

env.reset()
for i in range(100):
    action = env.action_space.sample()
    env.step(action=action)
import os
from stable_baselines3 import PPO
from game_env import GameEnv

models_dir = 'models'
log_dir = 'logs'

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

env = GameEnv()
env.reset()
model = PPO.load('models/first', env)

timesteps = 1000
gen = 1

while True:
    model.learn(total_timesteps=timesteps, reset_num_timesteps=False)
    model.save(f'{models_dir}/first{gen}')
    gen+=1
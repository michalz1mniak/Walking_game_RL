import os
from stable_baselines3 import PPO
from game_env import GameEnv

models_dir = 'modelsppo0'
log_dir = 'logs'

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

env = GameEnv()
env.reset()
model = PPO.load('modelsppo0/34900000.zip', env)

timesteps = 10000
gen = 3532

while True:
    model.learn(total_timesteps=timesteps, reset_num_timesteps=False)
    model.save(f'{models_dir}/{gen*timesteps}')
    gen+=1
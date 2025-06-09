import os
from stable_baselines3 import A2C
from game_env import GameEnv

models_dir = 'models'
log_dir = 'logs'

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

env = GameEnv()
env.reset()
model = A2C.load('models/200000.zip', env)

timesteps = 100000
gen = 3

while True:
    model.learn(total_timesteps=timesteps, reset_num_timesteps=False)
    model.save(f'{models_dir}/{gen*timesteps}')
    gen+=1
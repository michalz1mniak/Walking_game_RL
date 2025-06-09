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
model = A2C("MlpPolicy", env, verbose=1, tensorboard_log=log_dir)

timesteps = 10000
gen = 1

while True:
    
    model.learn(total_timesteps=timesteps, reset_num_timesteps=False)
    model.save(f'{models_dir}/{timesteps*gen}')
    gen+=1










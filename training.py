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
model = PPO("MlpPolicy", env, verbose=1, tensorboard_log=log_dir)

timesteps = 1000
gen = 1

while True:
    
    model.learn(total_timesteps=timesteps, reset_num_timesteps=False)
    model.save(f'{models_dir}/gen{gen}')
    gen+=1










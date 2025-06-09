import gymnasium as gym
from stable_baselines3 import A2C
from game_env import GameEnv

env = GameEnv()
env.reset()

models_dir = models_dir = 'models'
model_path = f'{models_dir}/.zip'

model = A2C.load(model_path, env=env)

episodes = 10

for ep in range(episodes):
    obs, _ = env.reset()
    done = False
    while not done:
        action, _ = model.predict(obs)
        obs, reward, done, _, info = env.step(action)

env.close


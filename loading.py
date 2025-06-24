import gymnasium as gym
from stable_baselines3 import PPO
from game_env import GameEnv

env = GameEnv(render=True)
env.reset()

models_dir = models_dir = 'modelsppo0'
model_path = f'{models_dir}/42090000.zip'

model = PPO.load(model_path, env=env)

episodes = 10

for ep in range(episodes):
    obs, _ = env.reset()
    done = False
    while not done:
        action, _ = model.predict(obs)
        obs, reward, done, _, info = env.step(action)

env.close


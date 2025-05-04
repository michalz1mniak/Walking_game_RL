import gymnasium as gym
from stable_baselines3 import PPO
from game_env import GameEnv

env = GameEnv()
env.reset()

models_dir = models_dir = 'models'
model_path = f'{models_dir}/1m.zip'

model = PPO.load(model_path, env=env)

episodes = 10

for ep in range(episodes):
    obs, _ = env.reset()
    done = False
    while not done:
        env.render()
        action, _ = model.predict(obs)
        obs, reward, done, _, info = env.step(action)

env.close


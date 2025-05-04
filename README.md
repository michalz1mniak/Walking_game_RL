# Walking\_game\_RL

**A custom 2D physics-based game environment for reinforcement learning experiments.**

## Overview

This project contains a 2D physics-based game developed using **Pygame** and **Pymunk**, where the player controls a humanoid character with four limbs. The game has been adapted to serve as a custom environment for reinforcement learning (RL). The goal is to make the character move forward without falling (especially avoiding head collisions with the ground). This reinforcement learning environment is built upon the game logic and physics from a separate repository, available [here](https://github.com/michalz1mniak/Walking_game_RL).

## Features

* Custom 2D physics-based humanoid agent
* Discrete action space with 8 movement options
* Basic reward system for moving forward and avoiding falls
* Step/reset interface inspired by OpenAI Gym
* Real-time visualization using Pygame

## Installation

```bash
git clone https://github.com/michalz1mniak/Walking_game_RL.git
cd Walking_game_RL
pip install -r requirements.txt
```

## Action Space

The agent has **8 discrete actions**, corresponding to different limb movements:

* Left/right rotation of arms and legs (independently)

## Observations

The environment returns a vector of physical states including positions and velocities of each body part.

## License

This project is licensed under the [MIT License](LICENSE).

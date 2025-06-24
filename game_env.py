import pymunk, pygame
import gymnasium as gym
import numpy as np
from game_files.player import Player
from game_files.ground import Walls
import random
from pymunk.vec2d import Vec2d

class GameEnv(gym.Env):
    def __init__(self, render = False):
        self.done = False
        self.render = render

        super().__init__()
        self.move_motor = 40

        self.action_space = gym.spaces.MultiDiscrete([3, 3, 3, 3])
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(38,), dtype=np.float32)
        if render:
            pygame.init()
            self.screen = pygame.display.set_mode((1280, 720))
            self.clock = pygame.time.Clock()

    def _collision(self,a,s,d):
        # self.done = True
        return True
    
    def _get_obs(self):
        parts = [
            self.player.head_body,
            self.player.torso_body,
            self.player.left_arm_body,
            self.player.right_arm_body,
            self.player.left_leg_body,
            self.player.right_leg_body
        ]

        obs = []
        for part in parts:
            # pozycja (x, y)
            obs.append(part.position[0])
            obs.append(part.position[1])

            # prędkość (vx, vy)
            obs.append(part.velocity[0])
            obs.append(part.velocity[1])

            # kąt i prędkość kątowa
            obs.append(part.angle)
            obs.append(part.angular_velocity)

        obs.extend([self.goal_position[0], self.goal_position[1]])

        if self.render:
            None
            # print(obs)
        

        return np.array(obs, dtype=np.float32)
        
    def reset(self, seed = None, options = None):
        self.done = False
        self.steps = 0  # licznik kroków

        self.space = pymunk.Space()
        self.space.gravity = (0,900)
        self.handler = self.space.add_collision_handler(1,2)
        self.handler.begin = self._collision

        self.player = Player()
        self.player.add_to_space(self.space)

        self.walls = Walls()
        self.walls.add_to_space(self.space)

        if random.random() < 0.5:
            x = random.uniform(100,400)
        else:
            x = random.uniform(800,1200)

        y = random.uniform(550, 650)
        self.goal_position = (x, y)

        return self._get_obs(), {}

    def _apply_action(self, action):
        
        rates = [-self.move_motor, 0, self.move_motor]  # 0, 1, 2

        self.player.torso_left_arm_motor.rate = rates[action[0]]
        self.player.torso_right_arm_motor.rate = rates[action[1]]
        self.player.torso_left_leg_motor.rate = rates[action[2]]
        self.player.torso_right_leg_motor.rate = rates[action[3]]
    
    def step(self, action):
        self.steps += 1
        if self.render:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.screen.fill((255,255,255))
            self.walls.draw(screen= self.screen, offset = (0,0))
            self.player.draw_all(screen = self.screen, offset=(0,0))
            pygame.draw.circle(self.screen,(0, 255, 0),(int(self.goal_position[0]), int(self.goal_position[1])),10)
            pygame.display.flip()
            self.clock.tick(60)
            # print(action)

        prev_pos = self.player.head_body.position
        self._apply_action(action)

        self.space.step(1/50)
        new_pos = self.player.head_body.position

        reward = 0

            # nagroda za przemieszczanie się w kierunku celu
        old_dist = prev_pos.get_distance(self.goal_position)
        new_dist = new_pos.get_distance(self.goal_position)
        progress = old_dist - new_dist
        reward += progress * 5  # wzmocnienie progresu

            # nagroda końcowa, jeśli bardzo blisko celu
        if new_dist < 50:
            reward += 500
            self.done = True
        
        if self.steps >= 500:
            reward -=200
            self.done = True
        

        return self._get_obs(), reward, self.done, False, {}
    




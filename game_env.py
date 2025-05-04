import pymunk, pygame
import gymnasium as gym
import numpy as np
from game_files.player import Player
from game_files.ground import Walls

class GameEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.move_motor = 40
        self.did_fall = False

        self.action_space = gym.spaces.Discrete(8)
        self.observation_space = gym.spaces.Box(low = 0, high = 10000 ,shape=(12,), dtype = np.float32)

        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

    def _collision(self,a,s,d):
        self.done = True
        self.did_fall = True
        return True
    
    def _get_obs(self):
        headx = self.player.head_body.position[0]
        heady = self.player.head_body.position[1]

        torsox = self.player.torso_body.position[0]
        torsoy = self.player.torso_body.position[1]

        left_armx = self.player.left_arm_body.position[0]
        left_army = self.player.left_arm_body.position[1]

        right_armx = self.player.right_arm_body.position[0]
        right_army = self.player.right_arm_body.position[1]

        left_legx = self.player.left_leg_body.position[0]
        left_legy = self.player.left_leg_body.position[1]

        right_legx = self.player.right_leg_body.position[0]
        right_legy = self.player.right_leg_body.position[1]

        self.observation = [headx, heady, torsox, torsoy, left_armx, left_army, right_armx, right_army, left_legx, left_legy, right_legx, right_legy]
        
        return self.observation
        
    def reset(self, seed = None, options = None):
        self.done = False
            
        self.space = pymunk.Space()
        self.space.gravity = (0,900)
        self.handler = self.space.add_collision_handler(1,2)
        self.handler.begin = self._collision

        self.player = Player()
        self.player.add_to_space(self.space)

        self.walls = Walls()
        self.walls.add_to_space(self.space)

        return self._get_obs(), {}

    def _apply_action(self, action):
        if action == 0:
            self.player.torso_left_arm_motor.rate = -self.move_motor
        elif action == 1:
            self.player.torso_left_arm_motor.rate = self.move_motor
        else:
            self.player.torso_left_arm_motor.rate = 0

        if action == 2:
            self.player.torso_right_arm_motor.rate = -self.move_motor
        elif action == 3:
            self.player.torso_right_arm_motor.rate = self.move_motor
        else:
            self.player.torso_right_arm_motor.rate = 0

        if action == 4:
            self.player.torso_left_leg_motor.rate = -self.move_motor
        elif action == 5:
            self.player.torso_left_leg_motor.rate = self.move_motor
        else:
            self.player.torso_left_leg_motor.rate = 0
            
        if action == 6:
            self.player.torso_right_leg_motor.rate = -self.move_motor
        elif action == 7:
            self.player.torso_right_leg_motor.rate = self.move_motor
        else:
            self.player.torso_right_leg_motor.rate = 0
    
    def step(self, action):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        self.screen.fill((255,255,255))
        self.walls.draw(screen= self.screen, offset = (0,0))
        self.player.draw_all(screen = self.screen, offset=(0,0))
        pygame.display.flip()
        self.clock.tick(60)
        
        self.prev = int(self.player.head_body.position[0])

        self._apply_action(action)

        self.space.step(1/50)

        self.new = int(self.player.head_body.position[0])

        self.reward  = 0

        if self.prev > self.new: self.reward = -10
        else: self.reward = 0.1

        if self.did_fall:
            self.reward = -1000
        
        if self.new > 3200:
            self.done = True

        return self._get_obs(), self.reward, self.done, False, {}
    




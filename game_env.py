import pymunk, pygame
import gymnasium as gym
import numpy as np
from game_files.player import Player
from game_files.ground import Walls

class GameEnv(gym.Env):
    def __init__(self):
        self.done = False

        super().__init__()
        self.move_motor = 40

        self.action_space = gym.spaces.Discrete(8)
        self.observation_space = gym.spaces.Box(low = 0, high = 10000 ,shape=(6,), dtype = np.float32)

        # pygame.init()
        # self.screen = pygame.display.set_mode((1280, 720))
        # self.clock = pygame.time.Clock()

    def _collision(self,a,s,d):
        #self.done = True
        return True
    
    def _get_obs(self):
        heady = self.player.head_body.position[1]

        torsoy = self.player.torso_body.position[1]

        left_army = self.player.left_arm_body.position[1]

        right_army = self.player.right_arm_body.position[1]

        left_legy = self.player.left_leg_body.position[1]

        right_legy = self.player.right_leg_body.position[1]

        self.observation = [heady, torsoy, left_army, right_army, left_legy, right_legy]
        
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
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         exit()
        # self.screen.fill((255,255,255))
        # self.walls.draw(screen= self.screen, offset = (0,0))
        # self.player.draw_all(screen = self.screen, offset=(0,0))
        # pygame.display.flip()
        # self.clock.tick(60)

        prev = int(self.player.head_body.position[0])

        self._apply_action(action)

        self.space.step(1/50)

        new = int(self.player.head_body.position[0])

        reward  = 0

        reward += new - prev

        if new > 1300:
            self.done = True

        return self._get_obs(), reward, self.done, False, {}
    




import pygame, pymunk, sys, time
import pymunk.pygame_util
from player import Player
from ground import Walls
from start_screen import Start

def get_camera_offset(player_pos, screen_size):
    offset_x = player_pos.x - screen_size[0] // 2
    offset_y = 0  
    return pymunk.Vec2d(offset_x, offset_y)


def collision(a,s,d):
    global remaining_frames, player
    if remaining_frames == 0:
        player.color = (255,0,0)
        remaining_frames = 10
    return True


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
background = pygame.image.load('game_files/backgrounds/background.png')
win_background = pygame.image.load('game_files/backgrounds/win_background.png')
font = pygame.font.Font('game_files/font/OrbitronFont.ttf',40)
score = 0

space = pymunk.Space()
space.gravity = (0,900)
handler = space.add_collision_handler(1,2)
handler.begin = collision

player = Player()
player.add_to_space(space)

walls = Walls()
walls.add_to_space(space)

start = Start()

game_state = False
remaining_frames = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        player.torso_left_arm_motor.rate = -10
    elif keys[pygame.K_w]:
        player.torso_left_arm_motor.rate = 10
    else:
        player.torso_left_arm_motor.rate = 0

    if keys[pygame.K_e]:
        player.torso_right_arm_motor.rate = -10
    elif keys[pygame.K_r]:
        player.torso_right_arm_motor.rate = 10
    else:
        player.torso_right_arm_motor.rate = 0

    if keys[pygame.K_a]:
        player.torso_left_leg_motor.rate = -10
    elif keys[pygame.K_s]:
        player.torso_left_leg_motor.rate = 10
    else:
        player.torso_left_leg_motor.rate = 0
        
    if keys[pygame.K_d]:
        player.torso_right_leg_motor.rate = -10
    elif keys[pygame.K_f]:
        player.torso_right_leg_motor.rate = 10
    else:
        player.torso_right_leg_motor.rate = 0
    
    if game_state == False and keys[pygame.K_SPACE]:
        game_state = True
        start = Start()

    if game_state:
        offset = get_camera_offset(player.torso_body.position, screen.get_size())

        screen.blit(background, (-offset.x-100, 0))
        walls.draw(screen, offset)
        player.draw_all(screen, offset)

        if player.head_body.position[0]>3300:
            start.image = win_background
            game_state = False

        if remaining_frames>0:
            remaining_frames-=1
            if remaining_frames == 0:
                game_state = False

        score = (player.head_body.position[0] - 640) * 500 / 2660
        text = font.render(f'Score: {int(round(score,0))}', False, (255,255,255))
        score_box1 = pygame.draw.rect(screen, (95, 99, 102), (25, 25, 300, 90), border_radius=20)
        score_box2 = pygame.draw.rect(screen, (255,255,255), (25, 25, 300, 90), border_radius=20, width=5)
        screen.blit(text, (50,45))
        print(player.torso_left_arm_motor.rate)

                
    else:
        
        start.draw(screen)
        space = pymunk.Space()
        space.gravity = (0,900)
        handler = space.add_collision_handler(1,2)
        handler.begin = collision

        player = Player()
        player.add_to_space(space)

        walls = Walls()
        walls.add_to_space(space)

    clock.tick(120)
    space.step(1/50)  
    pygame.display.flip()

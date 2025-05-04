import pygame

class Start():
    def __init__(self):
        self.image = pygame.image.load('game_files/backgrounds/start_background.png')
        self.color = (95, 99, 102)

    def draw(self, screen):
        screen.blit(self.image, (0,0))
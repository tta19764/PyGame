import pygame

class Background:
    def __init__(self):
        self.sky = pygame.image.load('Resources/Graphics/BG/SkyLong.png').convert()
        self.ground = pygame.image.load('Resources/Graphics/BG/groundLong.png').convert()
        self.sky_x = 0
        self.ground_x = 0

    def move(self, screen, speed):
        # bg sky movement
        if self.sky_x > (-2247+800):
            self.sky_x -= speed
        else:
            self.sky_x = 0
        screen.blit(self.sky, (self.sky_x,0))

        # bg ground movement
        if self.ground_x > -27:
            self.ground_x -= speed
        else:
            self.ground_x = 0
        screen.blit(self.ground, (self.ground_x, 300))
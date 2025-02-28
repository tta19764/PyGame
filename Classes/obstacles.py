import pygame
from random import randint

class Obstacles:
    def __init__(self):
        snail_frame_1 = pygame.image.load('Resources/Graphics/Snail/snail1.png').convert_alpha()
        snail_frame_2 = pygame.image.load('Resources/Graphics/Snail/snail2.png').convert_alpha()
        self.snail = [snail_frame_1, snail_frame_2]
        self.snail_index = 0
        fly_frame_1 = pygame.image.load('Resources/Graphics/Fly/Fly1.png').convert_alpha()
        fly_frame_2 = pygame.image.load('Resources/Graphics/Fly/Fly2.png').convert_alpha()
        self.fly = [fly_frame_1, fly_frame_2]
        self.fly_index = 0
        self.list = []

    def add_obstacle(self, score):
        if randint(0, 1) and score > 2500:
            self.list.append(self.fly[self.fly_index].get_rect(bottomleft=(randint(900, 1100), 210 + (45 * randint(0, 1)))))
        else:
            self.list.append(self.snail[self.snail_index].get_rect(bottomleft=(randint(900, 1100), 300)))

    def move(self, screen, speed):
        if self.list:
            for item in self.list:
                item.x -= speed
                if item.bottom == 300:
                    screen.blit(self.snail[self.snail_index], item)
                else:
                    screen.blit(self.fly[self.fly_index], item)
            self.list = [item for item in self.list if item.x > -100]

    def reset(self):
        self.list.clear()

    def get_obstacles(self):
        return self.list

    def fly_move(self):
        self.fly_index = (self.fly_index + 1) % 2

    def snail_move(self):
        self.snail_index = (self.snail_index + 1) % 2

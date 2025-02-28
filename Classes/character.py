import pygame

class Character:
    def __init__(self):
        self.gravity = 0
        player_walk_1 = pygame.image.load('Resources/Graphics/Char/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('Resources/Graphics/Char/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('Resources/Graphics/Char/jump.png').convert_alpha()
        self.player_rect = self.player_walk[self.player_index].get_rect(midbottom = (80, 300))
        self.jump_sound = pygame.mixer.Sound('Resources/Audio/jump.mp3')
        self.jump_sound.set_volume(0.05)

    def jump(self, event):
        if self.player_rect.bottom >= 300:
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                self.gravity = -20
                self.jump_sound.play()

    def restart(self):
        self.player_rect.bottom = 300
        self.gravity = 0

    def run(self, screen):
        self.gravity += 1
        self.player_rect.y += self.gravity
        if self.player_rect.bottom >= 300:
            self.player_rect.bottom = 300

        if self.player_rect.bottom < 300:
            player = self.player_jump
        else:
            self.player_index = (self.player_index + 0.1) % 2
            player = self.player_walk[int(self.player_index)]

        screen.blit(player, self.player_rect)

    def col_check(self, list):
        if list:
            for item in list:
                if self.player_rect.colliderect(item):
                    return True
        return False
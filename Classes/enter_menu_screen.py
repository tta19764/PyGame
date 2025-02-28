import pygame

class Enter_menu_screen:
    def __init__(self):
        self.font = pygame.font.Font('Resources/Font/Pixeltype.ttf', 50)
        player_scale = 84 / 68
        player_width = 150
        player_height = int(player_width * player_scale)
        self.player_stand = pygame.image.load('Resources/Graphics/Char/player_stand.png').convert_alpha()
        self.player_stand_scaled = pygame.transform.scale(self.player_stand, (player_width, player_height))
        self.player_stand_rectangle = self.player_stand_scaled.get_rect(center=(400, 200))

        self.game_name = self.font.render('My Offline Runner', False, (111, 196, 169))
        self.game_name_rect = self.game_name.get_rect(center=(400, 70))

        self.game_message = self.font.render('Press space to run', False, (111, 196, 169))
        self.game_message_rect = self.game_message.get_rect(center=(400, 350))

    def menu_screen(self, screen, score):
        screen.fill((94, 129, 162))
        screen.blit(self.player_stand_scaled, self.player_stand_rectangle)
        score_message = self.font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(self.game_name, (self.game_name_rect))
        if score == 0:
            screen.blit(self.game_message, (self.game_message_rect))
        else:
            screen.blit(score_message, score_message_rect)
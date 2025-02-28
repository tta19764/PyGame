import pygame
from sys import exit
from Classes.character import Character
from Classes.background import Background
from Classes.enter_menu_screen import Enter_menu_screen
from Classes.obstacles import Obstacles

def display_score():
    global speed_obstacle, speed_bg
    time = pygame.time.get_ticks() - start_time
    points = int(time * frames / 1000)
    points += (points // 500)
    score = font.render(f'Score: {points}', False, (64, 64, 64))
    score_rect = score.get_rect(midleft = (470, 50))
    screen.blit(score, score_rect)
    if speed_obstacle < 30: speed_obstacle = 5 + (points//250)
    if speed_bg < 20: speed_bg = 1 + (points // 500)
    return points

def display_record(record, points):
    if points > record: record = points
    record_board = font.render(f'Highest: {record}', False, (64, 64, 64))
    record_rect = record_board.get_rect(midleft = (150, 50))
    screen.blit(record_board, record_rect)


pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('My Runner')
clock = pygame.time.Clock()
font = pygame.font.Font('Resources/Font/Pixeltype.ttf', 50)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)
fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)
game_music = pygame.mixer.Sound('Resources/Audio/music.wav')
game_music.set_volume(0.05)



game_active = False
start_time = 0
frames = 60
score = 0
music_playing = False
record = 0

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1600)

character = Character()
bg = Background()
menu_screen = Enter_menu_screen()
obstacles = Obstacles()
speed_obstacle = 20
speed_bg = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            character.jump(event)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                game_active = True
                start_time = pygame.time.get_ticks()
        if game_active:
            if event.type == obstacle_timer:
                obstacles.add_obstacle(score)
            if event.type == snail_animation_timer:
                obstacles.snail_move()
            if event.type == fly_animation_timer:
                obstacles.fly_move()


    if game_active:
        if music_playing == False:
            game_music.play(loops=-1)
            music_playing = True

        #background movement
        bg.move(screen, speed_bg)

        #showing score
        score = display_score()
        display_record(record, score)

        #obstacles movement
        obstacles.move(screen, speed_obstacle)

        #character movement
        character.run(screen)

        if character.col_check(obstacles.get_obstacles()):
            game_active = False
    else:
        if score > record: record = score
        menu_screen.menu_screen(screen, score)
        obstacles.reset()
        character.restart()
        game_music.stop()
        music_playing = False
        speed_obstacle = 5
        speed_bg = 1

    pygame.display.update()
    clock.tick(frames)
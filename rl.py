# import sys
# sys.path.append("./game/")
# import wrapped_flappy_bird as game
# import flappy_bird_utils
# import pygame
#
# FPS = 30
# SCREENWIDTH  = 288
# SCREENHEIGHT = 512
#
# pygame.init()
# FPSCLOCK = pygame.time.Clock()
# SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
# pygame.display.set_caption('Flappy Bird')
#
# IMAGES, SOUNDS, HITMASKS = flappy_bird_utils.load()
# image_test = pygame.image.load('assets/sprites/bird-test.png')
#
#
# def it():
#     yield 0, 1
#
# # open up a game state to communicate with emulator
# game_state = game.GameState()
# while True:
#     print(image_test)
#     print(image_test.convert_alpha())
#     SCREEN.blit(image_test.convert_alpha(), (0,0))
#     pygame.display.flip()
# # while True:
# #     x_t1_colored, r_t, terminal = game_state.frame_step(it())
# #     print(r_t)

import pygame

position = [100, 200]
velocity = [7, 17]
radius = 50

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
background = pygame.Surface(screen.get_size())
screen.blit(background, (0,0))

ball = pygame.Surface(2*[radius*2])
pygame.draw.circle(ball, (0, 255, 0), 2*(radius,), radius)
bounds = (screen.get_size()[0] - 2 * radius,
          screen.get_size()[1] - 2 * radius)
rect = ball.get_rect()
rect.x = position[0]
rect.y = position[1]

done = False
while not done:
    for event in pygame.event.get():
        if event.type in [pygame.QUIT, pygame.KEYDOWN]:
            done = True

    for i in [0, 1]:
        position[i] += velocity[i]
        if position[i] < 0 or position[i] > bounds[i]:
            velocity[i] *= -1

    screen.blit(background, rect)
    rect.x = position[0]
    rect.y = position[1]
    screen.blit(ball, rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
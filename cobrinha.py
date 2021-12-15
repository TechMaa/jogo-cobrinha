import pygame, random
from pygame.locals import *


def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return x // 10 * 10, y // 10 * 10


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Cobrinha')

cobrinha = [(300, 300), (310, 300), (320, 300)]
cobrinha_skin = pygame.Surface((10, 10))
cobrinha_skin.fill((0, 255, 255))

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 255, 255))

my_direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                my_direction = DOWN
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                my_direction = LEFT
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(cobrinha[0], apple_pos):
        apple_pos = on_grid_random()
        cobrinha.append((0, 0))

    for i in range(len(cobrinha) - 1, 0, -1):
        cobrinha[i] = (cobrinha[i - 1][0], cobrinha[i - 1][1])

    if my_direction == UP:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] - 10)
    if my_direction == DOWN:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] + 10)
    if my_direction == RIGHT:
        cobrinha[0] = (cobrinha[0][0] + 10, cobrinha[0][1])
    if my_direction == LEFT:
        cobrinha[0] = (cobrinha[0][0] - 10, cobrinha[0][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    for pos in cobrinha:
        screen.blit(cobrinha_skin, pos)

    pygame.display.update()

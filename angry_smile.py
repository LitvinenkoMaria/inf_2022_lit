import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
bg_color = (255, 255, 210)
screen.fill(bg_color)

circle(screen, (255, 255, 0), (200, 175), 90)
circle(screen, (0, 0, 0), (200, 175), 90, 1)

circle(screen, (255, 0, 0), (155, 150), 20)
circle(screen, (0, 0, 0), (155, 150), 20, 1)

circle(screen, (0, 0, 0), (155, 150), 7)
circle(screen, (0, 0, 0), (155, 150), 7, 1)

circle(screen, (255, 0, 0), (245, 150), 15)
circle(screen, (0, 0, 0), (245, 150), 15, 1)

circle(screen, (0, 0, 0), (245, 150), 5)
circle(screen, (0, 0, 0), (245, 150), 5, 1)

pygame.draw.line(screen, (0,0,0), 
                 [100, 100], 
                 [180, 140], 7)

pygame.draw.line(screen, (0,0,0), 
                 [300, 110], 
                 [220, 140], 7)

polygon(screen, (0, 0, 0), [(150,200), (150,210),
                               (250,210), (250,200)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

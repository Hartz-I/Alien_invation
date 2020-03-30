import pygame
import sys

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ship.moving_right=True

            if event.key==pygame.K_LEFT:
                ship.moving_left=True
                #ship.rect.centerx+=1

        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                ship.moving_right=False

            if event.key==pygame.K_LEFT:
                ship.moving_left=False

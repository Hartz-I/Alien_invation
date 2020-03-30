import pygame
import sys

def keydown_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        # ship.rect.centerx+=1

def keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            keydown_events(event,ship)

        elif event.type==pygame.KEYUP:
            keyup_events(event,ship)

def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)

    ship.blitme()

    pygame.display.flip()

import pygame
from settings import Settings
import game_function as gf
from ship import Ship
import sys

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invation'.title())
    ship=Ship(screen)

    while True:
        gf.check_events()

        screen.fill(ai_settings.bg_color)

        ship.blitme()

        pygame.display.flip()

run_game()

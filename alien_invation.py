import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():	
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('Alien invation'.title())
	ship=Ship(ai_settings,screen)

	alien_hit=pygame.mixer.Sound('audio/alien_hit.wav')
	ship1_hit=pygame.mixer.Sound('audio/ship_hit.wav')
	ship_last_hit=pygame.mixer.Sound('audio/ship_last_hit.wav')
	bullet=pygame.mixer.Sound('audio/bullet.wav')
	pygame.mixer.music.load('audio/warning.mp3')
	pygame.mixer.music.play()

	#alien=Alien(screen)
	bullets=Group()
	aliens=Group()
	stats=GameStats(ai_settings)
	
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	while True:
		gf.check_events(ai_settings,screen,ship,bullets,bullet)
		
		bullets.update()

		if stats.game_active:
			ship.update()

			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets,ship1_hit)

			gf.update_bullets(ai_settings,screen,ship,bullets,aliens,alien_hit)
		
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
		
run_game()

7.33

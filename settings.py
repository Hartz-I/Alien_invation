import pygame
class Settings():
	
	def __init__(self):
		self.screen_width=1000
		self.screen_height=625
		self.bg_color_1=(238,221,130)
		self.bg_color_2=(0,255,0)
		self.bg_color_3=(0,0,255)
		self.bg_image=pygame.image.load('images/bg_5.jpg')
		self.ship_speed_factor=5
		
		self.bullet_speed_factor=8
		self.bullet_width=3
		self.bullet_height=15
		self.bullet_color=255,255,255
		self.bullets_allowed=3

		self.alien_speed_factor=1
		self.fleet_drop_speed=10
		self.fleet_direction=1

		self.ship_limit=3

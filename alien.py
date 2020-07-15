import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	
	def __init__(self,screen,ai_settings):
		
		super(Alien,self).__init__()
		self.ai_settings=ai_settings
		
		self.screen=screen
		self.image=pygame.image.load('images/alien.png')
		
		self.rect=self.image.get_rect()
		#self.screen_rect=screen.get_rect()
		
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def check_edges(self):
		self.screen_rect=self.screen.get_rect()

		if self.rect.right>=self.screen_rect.right:
			return True
		elif self.rect.left<=0:
			return True


	def update(self):
		self.check_edges()
		self.x+=self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
		self.rect.x=self.x

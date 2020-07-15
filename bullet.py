import pygame
from pygame.sprite import Sprite
import math

class Bullet(Sprite):
	
	def __init__(self,ai_settings,screen,ship):
		super(Bullet,self).__init__()
		self.screen=screen
		
		self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx=ship.rect.centerx
		#self.rect.centery=ship.rect.centery
		self.rect.top=ship.rect.top
		
		self.y=float(self.rect.y)
		#self.x=float(self.rect.x)
		
		self.color=ai_settings.bullet_color
		self.speed_factor=ai_settings.bullet_speed_factor
		
	def update(self):
		self.y-=self.speed_factor
		self.rect.y=self.y
		#self.x=math.sin(self.y)
		#self.rect.x=self.x
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)

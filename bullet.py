from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,screen):
        super(Bullet,self).__init__()

        self.screen=screen



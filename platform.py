import pygame as pg
from settings import *

class Platform(pg.sprite.Sprite):
    
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        img = pg.image.load("images/Ground/grass.png").convert_alpha()
        self.image = pg.transform.scale(img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        pass
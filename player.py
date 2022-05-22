import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    
    def __init__(self, game): 
        pg.sprite.Sprite.__init__(self)
        self.game = game
        img = pg.image.load(PLAYER_IMAGES_FOLDER + PLAYER_STAND_IMAGE).convert_alpha()
        self.image = pg.transform.scale(img, (60,80))
        self.rect = self.image.get_rect()
        self.rect.center = (SC_WIDTH/2, SC_HEIGHT/2)
        self.pos = vec(SC_WIDTH/2, SC_HEIGHT/2)
        self.speed = vec(0, 0)
        self.acc = vec(0, 0)
    
    def update(self):
        self.acc = vec(0, GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC_X
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC_X
        if keys[pg.K_SPACE]:
            self.jump()
        self.acc.x += self.speed * PLAYER_FRICTION
        self.speed += self.acc
        self.pos += self.speed + 0.5 * self.acc
        if self.pos.x > SC_WIDTH:
            self.pos.x = 0
        elif self.pos.x < 0:
            self.pos.x = SC_WIDTH 
        self.rect.midbottom = self.pos
        
        def jump(self):
            self.rect.y += 1
            hits = pg.sprite.spritecollide(self, self.game.platforms, False)
            self.rect.y -=1
            if hits:
                self.speed.y = -17
        
        
        
        
        
        
        
        
        
        
        
            
        
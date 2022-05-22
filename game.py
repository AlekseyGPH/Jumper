import pygame as pg
import random
import sys
from settings import *
from player import Player
from platform import Platform

class Game:

    def __init__(self):
        self.screen = pg.display.set_mode((SC_WIDTH, SC_HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True

    def play(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.check_events()
            self.update()
            self.draw()

    def new_game(self):
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        p1 = Platform(0, SC_HEIGHT - 64, SC_WIDTH, 64)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        self.play()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.speed.y = 0
            self.player.pos.y = hits[0].rect.top
            

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()




        
                









        
        

import pygame
import touhou_Nikita
class Enemy_hero(pygame.sprite.Sprite, Character):
    def __init__(self,im_file):
##        self.health = 7
##        self.projects = []
##        self.image = pygame.image.load(im_file)
##        self.pos = [screen.get_width()//2 - self.image.get_width() // 2, \
##                    0 - self.image.get_height()]
##        self.rect = self.image.get_rect()
##        self.rect.left = self.pos[0]
##        self.rect.top = self.pos[1]
##        self.vel = [0,0]
##        self.makep = False
        Character.__init__()
        self.pos = [300,50]
        self.projects = self.bombs
##    def update(self):
##        self.rect.top += self.vel[1]
##        self.rect.left += self.vel[0]
##
##        if self.rect.left < 0:
##            self.rect.left = 0
##        if self.rect.left > screen.get_width() - self.image.get_width():
##            self.rect.left = screen.get_width() - self.image.get_width()
##        if self.rect.top < 0:
##            self.rect.top = 0
##        if self.rect.top > screen.get_height() - self.image.get_height():
##            self.rect.top = screen.get_height() - self.image.get_height()
    def shoot(self):
        for pr in range(7):
            bolet = Projectiles(bfly, (self.rect.left + self.image.get_width() // 2 , self.rect.top),pr)
            bolet.rect.left -= bolet.bfly.get_width() // 2
            self.projects.append(bolet)

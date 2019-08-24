import pygame
import random
import time
import math
import os, sys
#from enemy import *

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([0,0,0])
#bfly = "images\plr_boolet.png"
bfly = "images\p_bfly.png"
bfly2 = "images\p_bfly2.png"
image_list = []
image = "images\hero.png"
port = "images\\"+"red_touhou.png"
#main hero class
class Character(pygame.sprite.Sprite):
    def __init__(self,im_file):
        self.health = 7
        self.bombs = 5
        self.projects = []
        self.image = pygame.image.load(im_file).convert()
        #self.image.set_alpha(100)
        self.portrait = pygame.image.load(port).convert()
        self.portrait = pygame.transform.scale(self.portrait,(200,380))
        self.alpha = 100
        self.pos = [screen.get_width()//2 - self.image.get_width() // 2, \
                    screen.get_height() - self.image.get_height()]
        self.rect = self.image.get_rect()
        self.rect.left = self.pos[0]
        self.rect.top = self.pos[1]
        self.vel = [0,0]
        self.makep = False
        self.shoot_number = 0
        self.attack_way = 1
    def show_portrait(self):
        if self.alpha:
            self.alpha -= 0.5
            self.portrait.set_alpha(self.alpha)
            self.port_rect = self.portrait.get_rect()
            self.port_rect.center = (screen.get_width()//2,screen.get_height()//2)
            screen.blit(self.portrait,self.port_rect)

    def update(self):
        self.rect.top += self.vel[1]
        self.rect.left += self.vel[0]

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.left > screen.get_width() - self.image.get_width():
            self.rect.left = screen.get_width() - self.image.get_width()
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.top > screen.get_height() - self.image.get_height():
            self.rect.top = screen.get_height() - self.image.get_height()
     
    def shoot(self):
        self.shoot_number = (self.shoot_number +1) % 360
        for pr in range(7):
            bolet = Projectiles("images\p_bfly"+"2"*(pr%2)+".png", \
                                (self.rect.left + self.image.get_width()//2  , self.rect.top + self.image.get_height() // 2),pr)
            if self.attack_way == 1:
                bolet.speed = 10
                bolet.size_of_illusion = 5
            elif self.attack_way == 2:
                bolet.speed = 1
                bolet.size_of_illusion = 1
                #bolet.bfly = pygame.transform.rotate(pygame.image.load(bfly), 360 / 7 + (360 / 7)*pr)
                bolet.rect = bolet.bfly.get_rect()
                bolet.rect.center = bolet.pos
            bolet.rect.left -= bolet.bfly.get_width() // 2
            self.projects.append(bolet)

    def bullet_attack(self):
        global bullet_list
        bullet = Bullet(self.rect.x, self.rect.y, random.randrange(640), random.randrange(480))
        bullet_list.add(bullet)
##projectiles class
class Enemy_hero(Character):
    def __init__(self,im_file):
        Character.__init__(self,im_file)
        self.pos = [300,50]
        self.projects = self.bombs
##        self.health = 7
##        self.projects = []
##        self.image = pygame.image.load(im_file)
##        self.pos = [screen.get_width()//2 - self.image.get_width() // 2, \
##                    0 + self.image.get_height()]
##        self.rect = self.image.get_rect()
##        self.rect.left = self.pos[0]
##        self.rect.top = self.pos[1]
##        self.vel = [0,0]
##        self.makep = False
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
##    def shoot(self):
##        for pr in range(7):
##            bolet = Projectiles(bfly, (self.rect.left + self.image.get_width() // 2 , self.rect.top),pr)
##            bolet.rect.left -= bolet.bfly.get_width() // 2
##            self.projects.append(bolet)

class Projectiles(pygame.sprite.Sprite):
    
    def __init__(self,im_file,pos,num):
        self.pos = pos
        self.bfly = pygame.image.load(im_file)
                   
        self.vel = [0,0]
        self.size_of_illusion = 1
        if hero.attack_way != 3:
            self.angle = 360 // 20 + (360 // 20)*num + hero.shoot_number*self.size_of_illusion
        else:
            self.angle = round(360 / 7 + (360 / 7)*num+ hero.shoot_number*self.size_of_illusion)
        #self.speed = random.randrange(5,28)
        
        #self.bfly = pygame.transform.rotate(self.bfly, 360 // 7//7 + (360 // 7//7)*num)
        self.bfly = pygame.transform.rotate(self.bfly, (math.degrees(self.angle) + 360)* (-1) )
        self.rect = self.bfly.get_rect()
        self.rect.center = self.pos

        
        self.speed = 3
        self.how_fast = 0.5
        self.num_list = num
        self.radius = 0.1
        self.x = 1

##        def scalar(x1, y1, z1, x2, y2, z2):
##            return x1*x2 + y1*y2 + z1*z2
##         
##        def module(x, y, z):
##            return sqrt(x ** 2 + y ** 2 + z ** 2)
##         
##        cos = scalar(x1, y1, z1, x2, y2, z2)/(module(x1,y1,z1)*module(x2,y2,z2))
##        ang = acos(cos)
##        
##    def count_angle(self):
##        cos = scalar(self.rect.left,self.rect.top,hero.rect.left,hero.rect.top)/\
##              (module(self.rect.left,self.rect.top)*module(hero.rect.left,hero.rect.top))
##        return math.acos(cos)
    def __str__(self):
        s = ''
        #s += str(self.angle)
        s += str(self.rect.top) +' ' +str(self.how_fast)
        return s
    def move(self):
        global heros
        self.speed += self.how_fast
        self.rect.left += round(math.sin(self.angle)*self.speed)
        self.rect.top += round(math.cos(self.angle)*self.speed)
##        if self.speed == 4:
##            self.pos = self.rect.center
##            ind = hero.projects.index(self)
##            self.bfly = pygame.transform.rotate(self.bfly, ind * 20 )
##            self.rect = self.bfly.get_rect()
##
##            self.rect.center = self.pos
        
        
##    def move_spiral(self):
##
##        self.rect.left += 1
##        self.rect.top = math.sqrt(self.radius ** 2 - (self.rect.left - )
    def move_crazy(self):
        #self.speed += self.how_fast
        self.radius *= 0.1
        self.rect.left += round(math.sin(self.angle)*self.speed +self.radius)
        self.rect.top += round(math.cos(self.angle)*self.speed+self.radius)
    def move_up(self):
        self.rect.top += self.vel[1]
        self.rect.top -= self.speed

    def move_to_hero(self, pos):
        #self.x += 1
        self.rect.top = self.rect.top + (pos[1] - self.rect.top)/(pos[0] - self.rect.left)*(self.x - self.rect.left)#уравнение прямой
##        if not self.rect.collidepoint(self.mouse_pos):
##            angle = math.atan2( (self.mouse_pos[1] - self.rect.y), (self.mouse_pos[0] - self.rect.x)
##            self.rect.x += self.speed * math.cos(angle) #расчет угла между точками
##            self.rect.y += self.speed * math.sin(angle)
    def spiral(self):
        self.speed += 10
        self.angle = (self.angle + 0.1)% 360
        self.rect.left += round(math.sin(self.angle)*self.speed)
        self.rect.top += round(math.cos(self.angle)*self.speed)

    def move_circle(self):
        self.angle = (self.angle + 0.1)% 360
        self.rect.left += round(math.sin(self.angle)*10)
        self.rect.top += round(math.cos(self.angle)*10)
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet. """
 
    def __init__(self, start_x, start_y, dest_x, dest_y):
        """ Constructor.
        It takes in the starting x and y location.
        It also takes in the destination x and y position.
        """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Set up the image for the bullet
##        self.image = pygame.Surface([4, 10])
##        self.image.fill((255, 255, 255))
        self.image = pygame.image.load("images\knife.png")
        
        self.rect = self.image.get_rect()
 
        # Move the bullet to our starting location
        self.rect.x = start_x
        self.rect.y = start_y
 
        # Because rect.x and rect.y are automatically converted
        # to integers, we need to create different variables that
        # store the location as floating point numbers. Integers
        # are not accurate enough for aiming.
        self.floating_point_x = start_x
        self.floating_point_y = start_y
 
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff);
        
        self.image = pygame.transform.rotate(self.image,(math.degrees(angle) + 360 )*(-1))
    
        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        velocity = 5
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity
        
 
    def update(self):
        """ Move the bullet. """
 
        # The floating point x and y hold our more accurate location.
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x
 
        # The rect.x and rect.y are converted to integers.
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)
 
        # If the bullet flies of the screen, get rid of it.
        if self.rect.x < 0 or self.rect.x > screen.get_width() or self.rect.y < 0 or self.rect.y > screen.get_height():
            self.kill()


#creating hero instance
hero = Character(image)
#enemy1 = Enemy_hero("images\enemy_tou.png")
screen.blit(hero.image, hero.pos)
#screen.blit(enemy1.image, enemy1.pos)
pygame.display.flip()

bullet_list = pygame.sprite.Group()
running = True
clock = pygame.time.Clock()
make_bullet = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
            
                hero.vel[1] -= 3

            if event.key == pygame.K_DOWN:
                hero.vel[1] += 3

            if event.key == pygame.K_LEFT:

                hero.vel[0] -= 3

            if event.key == pygame.K_RIGHT:

                hero.vel[0] += 3
            if event.key == pygame.K_z:
                hero.makep = True
                hero.attack_way = 1
                #enemy1.shoot()
            if event.key == pygame.K_a:
                #hero.makep = True
                hero.shoot()
                hero.attack_way = 2
            if event.key == pygame.K_s:#spiral
                hero.makep = True
                hero.shoot()
                hero.bombs -= 1

                start_ticks = pygame.time.get_ticks()
                
                hero.attack_way = 3
                print(hero.bombs)
            if event.key == pygame.K_c:
                hero.attack_way = 4
                hero.makep = True
                hero.shoot()
            if event.key == pygame.K_p:
                for pr in hero.projects:
                    print(pr, end = ',')
            if event.key == pygame.K_b:
                make_bullet =  True
                hero.bullet_attack()
        elif event.type == pygame.KEYUP:
            hero.vel[1] = 0
            hero.vel[0] = 0
            if event.key == pygame.K_z:
                hero.makep = False
            if event.key == pygame.K_a:
                hero.makep = False
            if event.key == pygame.K_s:
                hero.makep = False
            if event.key == pygame.K_c:
                hero.makep = False
            if event.key == pygame.K_b:
                make_bullet = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
 
            # Get the mouse position
            pos = pygame.mouse.get_pos()
 
            mouse_x = pos[0]
            mouse_y = pos[1]
 
            # Create the bullet based on where we are, and where we want to go.
            bullet = Bullet(hero.rect.x, hero.rect.y, mouse_x, mouse_y)
            bullet_list.add(bullet)
        if event.type == pygame.QUIT:
            running = False
            

    screen.blit(hero.image,hero.rect)
    #screen.blit(enemy1.image, enemy1.rect)
    clock.tick(50)
    #hero shoot
    if hero.makep == True:
        hero.shoot()
    elif make_bullet:
        hero.bullet_attack()
    if hero.attack_way == 1:
        for b in hero.projects:
            screen.blit(b.bfly, b.rect)
            #b.move_up()
            b.move()
    elif hero.attack_way == 3 and hero.bombs > 0:
        
        for b in hero.projects:
            screen.blit(b.bfly, b.rect)
            
            seconds=(pygame.time.get_ticks()-start_ticks)/1000
            if seconds < 2:
                b.move_circle()
            else:
                b.move()
    elif hero.attack_way == 3 and hero.bombs == 0:
        hero.show_portrait()
    
    elif hero.attack_way == 4:
        for b in hero.projects:
            screen.blit(b.bfly, b.rect)
            b.move_crazy()
    else:
        for b in hero.projects:
            screen.blit(b.bfly, b.rect)
            
            b.move()
    bullet_list.draw(screen)#drawing bullets
    bullet_list.update()#moving a group of bullets
    
    #deleting projectiles
    for b in hero.projects:
        if b.rect.top < 0 or b.rect.left < 0 or b.rect.left > screen.get_width() or b.rect.top > screen.get_height():
            n = hero.projects.index(b)
            hero.projects.pop(n)

##    for b in hero.projects:# Замедление выше половины экрана
##        if b.rect.top < 240:
##            b.how_fast = 0.01
##            b.speed = 3
##
##    #enemy shoot
##    enemy1.shoot()
##    for b in enemy1.projects:
##        screen.blit(b.bfly, b.rect)
##        #b.move_up()
##        b.move_to_hero(hero.rect)
##    #deleting projectiles
##    for b in enemy1.projects:
##        if b.rect.top < 0 or b.rect.left < 0 or b.rect.left > screen.get_width() or b.rect.top > screen.get_height():
##            n = enemy1.projects.index(b)
##            enemy1.projects.pop(n)

        
    pygame.display.flip()
    screen.fill([0,0,0])
    hero.update()


import pygame
import random
import time
import enemy
import math
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([0,0,0])
image = "images\hero.png"
enemy_image = "enemy_tou.png"
circles_images = ["gray_circle.png","cherry_circle.png","red_circle.png","purple_circle.png",\
                  "blue_circle.png","lightblue_circle.png","sky_circle.png","lightsky_circle.png",\
                  "green_circle.png","greenish_circle.png","salad_circle.png","lightsalad_circle.png",\
                  "yellow_circle.png","gold_circle.png","white_circle.png"]
class Character(pygame.sprite.Sprite):
    def __init__(self,im_file):
        self.health = 7
        self.bombs = []
        self.image = pygame.image.load(im_file)
        self.pos = [screen.get_width()//2 - self.image.get_width() // 2, \
                    screen.get_height() - self.image.get_height()]
        self.rect = self.image.get_rect()
        self.rect.left = self.pos[0]
        self.rect.top = self.pos[1]
        self.vel = [0,0]
        self.accel = [0,0]
        self.make_projectile = False
    def update(self):
        
        if self.rect.left < 0:
            self.rect.left = 0
   
        if self.rect.left > screen.get_width() - self.image.get_width():
            self.rect.left = screen.get_width() - self.image.get_width()
            
        if self.rect.top < 0:
            self.rect.top = 0            

        if self.rect.top > screen.get_height() - self.image.get_height():
            self.rect.top = screen.get_height() - self.image.get_height()

        self.rect.left += self.vel[0]
        self.rect.top += self.vel[1]
        self.vel[0] += self.accel[0]
        self.vel[1] += self.accel[1]
        self.pos = [self.rect.left, self.rect.top]

##        for b in self.bombs:
##            #b.move_spiral()
##            b.move_radial()


    def shot(self):
        #self.bombs = []
        bomb_num = random.randrange(8,20)

        for i in range(bomb_num):
            bullet = Bubble((self.rect.left + self.image.get_width()//2,self.rect.top),i)

            print()
            self.bombs.append(bullet)
            
        
        

class Bubble(pygame.sprite.Sprite):
    def __init__(self, pos,number):
##        self.pos = pos
##        self.radius = radius
        self.vel = [0,0]
        self.image = pygame.image.load('images' + "\\"+circles_images[random.randrange(len(circles_images))])
        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]
        self.angle = random.randrange(360)
        self.speed = random.randrange(7,15)
        self.num_in_list = number

        self.k = 1
        self.h = 0.005
        self.a = 5
        self.b = 3      
        self.r = self.a * math.exp(self.k * self.b);
##        
##    def draw(self):
##        pygame.draw.circle(screen, aqua, self.pos, self.radius,2)
        
    def move_radial(self):
        global hero
        self.speed += 0.1
        self.rect.left += round(math.cos(self.angle//0.017)* self.speed )
        self.rect.top += round(math.sin(self.angle//0.017)* self.speed)

        if self.rect.left < 0:
            hero.bombs.pop()
   
        elif self.rect.left > screen.get_width() - self.image.get_width():
            hero.bombs.pop()
            
        elif self.rect.top < 0:
            hero.bombs.pop()           

        elif self.rect.top > screen.get_height() - self.image.get_height():
            hero.bombs.pop()
    def move_up(self):
        global hero
        #self.rect.top += self.vel[1]
        self.rect.top -= self.speed
        
    def move_spiral(self):
        self.k += 1 
        self.a += 0.1;
        self.b += 1;

        self.rect.left += round(self.r * math.cos(self.k/0.017));
        self.rect.top += round(-self.r * math.sin(self.k/0.017));
        self.k = self.k + self.h;
##        self.rect.left += round(self.r * math.cos(self.k));
##        self.rect.top += round(-self.r * math.sin(self.k));
##        if self.k < 6 * math.pi:
##            self.k = self.k + self.h;
        
        
        
    def get_pos(self):
        return self.pos
    
##    def get_radius(self):
##        return self.radius

    
hero = Character(image)
enemy1 = enemy.Enemy_hero(enemy_image)
screen.blit(hero.image, hero.pos)
screen.blit(enemy1.image, enemy1.pos)
pygame.display.flip()

running = True
clock = pygame.time.Clock()
while running:
    screen.fill([0,0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
         # check for key presses
            
            if event.key == pygame.K_UP:
                hero.vel[1] -= 1
                hero.accel[1] = -1

            elif event.key == pygame.K_DOWN:
                hero.vel[1] += 1
                hero.accel[1] = 1
            elif event.key == pygame.K_LEFT:
                hero.vel[0] -= 1
                hero.accel[0] = -1

            elif event.key == pygame.K_RIGHT:
                hero.vel[0] += 1
                hero.accel[0] = 1
            elif event.key == pygame.K_z:
                hero.make_projectile = True
                
                
        elif event.type == pygame.KEYUP:
            hero.accel = [0,0]
            hero.vel = [0,0]
            if event.key == pygame.K_z:
                hero.make_projectile = False

    
    hero.update()
    if hero.make_projectile:
        hero.shot()
    #time.sleep(0.05)
    for b in hero.bombs:
        #b.move_up()
        b.move_up()
       
        screen.blit(b.image, b.rect)

    for b in hero.bombs:
        if b.rect.top < 0:
            n = hero.bombs.index(b)
            hero.bombs.pop(n)
    clock.tick(50)
    screen.blit(hero.image, hero.rect)
    pygame.display.flip()
    
pygame.quit()

import pygame 
import random


# activate the pygame library .   
# initiate pygame and give permission   
# to use pygame's functionality.

pygame.init() 

# create the display surface object   
# of specific dimension..e(500, 500).

win = pygame.display.set_mode((500, 500)) 
clock = pygame.time.Clock()
   
# Indicates pygame is running

run = True

# lives

L = [5]

# time delay factor

td = 6

# set initial score

sc = 0

# define colours in advance

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# sound effects

beep_sound = pygame.mixer.Sound("beep.wav")
explosion_sound = pygame.mixer.Sound("Explosion.wav")

# create sprite groups

all_sprites = pygame.sprite.Group()
bats = pygame.sprite.Group()
wall = pygame.sprite.Group()
balls = pygame.sprite.Group()


# create classes

class Ball(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((12, 12))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = 6
            pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.x = random.randrange(100, 300)
            self.rect.y = random.randrange(200, 300)
            self.xdir = 1
            self.ydir = 1

        def update(self):
            self.rect.x += self.xdir
            self.rect.y += self.ydir
            if self.rect.x >= 500 or self.rect.x <=0:
                self.xdir = -self.xdir
            if self.rect.y <=0:
                self.ydir = -self.ydir
            if self.rect.y >=500:
                self.rect.x = 350
                self.rect.y = 250
                L[0] = L[0] - 1

ball = [0,0]          

for i in range(2):
    ball[i] = Ball()
    all_sprites.add(ball[i])
    balls.add(ball[i])


class Bat(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 10))
            self.image.fill(GREEN)
            self.rect = self.image.get_rect()
            self.rect.x = 250
            self.rect.y = 450
            self.batvel = 2

        def update(self):
           keys = pygame.key.get_pressed() 
           if keys[pygame.K_LEFT] and self.rect.x>0:
                self.rect.x -= self.batvel
           if keys[pygame.K_RIGHT] and self.rect.x<450: 
                self.rect.x += self.batvel 


bat = Bat()
bats.add(bat)
all_sprites.add(bat)

class Wall(pygame.sprite.Sprite):
        def __init__(self, x, y, col):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 10))
            self.image.fill(col)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


def buildwall():
    for j in range(5):
        for i in range(10):
            if j%2 ==0:
                if i%2==0:
                    col = BLUE
                else:
                    col = GREEN
            else:
                if i%2==0:
                    col = GREEN
                else:
                    col = BLUE
            brick = Wall(i*50,50 + j*10, col)
            wall.add(brick)
            all_sprites.add(brick)

buildwall()


# infinite loop

while run:

    # display score

    pygame.display.set_caption("Score= "+str(sc))
    
    # creates time delay 
    
    pygame.time.delay(td) 
      
    # iterate over the list of Event objects   
    # that was returned by pygame.event.get() method.
    
    for event in pygame.event.get(): 
          
        # if event object type is QUIT   
        # then quitting the pygame   
        
        if event.type == pygame.QUIT: 
            run = False

    # update all sprites 

    all_sprites.update()

    # check for enough lives left

    if L[0] == 0:
        print(sc)
        run = False

    # code for when ball hits bat
    
    for i in range(2):
        hits = pygame.sprite.spritecollide(ball[i], bats, False)
        if hits and ball[i].ydir ==1:
            ball[i].ydir = -ball[i].ydir
            pygame.mixer.Sound.play(beep_sound)

        
    # code for when ball hits wall

    for i in range(2):
        hits = pygame.sprite.spritecollide(ball[i], wall, True)
        if hits:
            ball[i].ydir = -ball[i].ydir
            pygame.mixer.Sound.play(explosion_sound)
        for hit in hits:
            sc = sc + 10

    
    # completely fill the surface object   
    # with black colour
    
    win.fill(BLACK)

    # draw all sprites

    all_sprites.draw(win)

    # check is wall is fully destroyed and redraw

    if len(wall) == 0:
        buildwall()
      
    # it refreshes the window
    
    pygame.display.update()  
  
# closes the pygame window

pygame.quit() 


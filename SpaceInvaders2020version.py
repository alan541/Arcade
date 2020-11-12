import pygame 
import random
import os

# activate the pygame library .   
# initiate pygame and give permission   
# to use pygame's functionality.

pygame.init() 

# create the display surface object   
# of specific dimension..e(500, 500).

win = pygame.display.set_mode((500, 500)) 
clock = pygame.time.Clock()

# display title

pygame.display.set_caption("Space Invaders 2020!")

# Indicates pygame is running

run = True

# lives

L = 5

# time delay factor

td = 40

# set initial score

sc = 0

# screen number

screen = 1

# initial speed of player

vel = 4


# define colours in advance

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# sound effects

explosion_sound = pygame.mixer.Sound("Explosion.wav")

# create sprite groups

all_sprites = pygame.sprite.Group()
sides = pygame.sprite.Group()
aliens = pygame.sprite.Group()
playerparts = pygame.sprite.Group()
bullets = pygame.sprite.Group()
alienfire = pygame.sprite.Group()
defences = pygame.sprite.Group()
bonusalien = pygame.sprite.Group()



# alien & bullet figures

game_folder = os.path.dirname(__file__)
bullet_img = pygame.image.load(os.path.join(game_folder, "laserRed16.png")).convert()
alien_img = pygame.image.load(os.path.join(game_folder, "enemyBlue5.png")).convert()
background = pygame.image.load(os.path.join(game_folder, 'starfield.png')).convert()
background_rect = background.get_rect()
alienbonus_img = pygame.image.load(os.path.join(game_folder, "ufoRed.png")).convert()



# drawing on screen function

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



# create classes

af = []

class Aliens(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(alien_img, (30, 30))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.xdir = 1

        def update(self):
            hits = pygame.sprite.spritecollide(rs, aliens, False)
            if hits and self.xdir == 1:
                self.rect.y += 20
                self.xdir = -self.xdir
            hits1 = pygame.sprite.spritecollide(ls, aliens, False)
            if hits1 and self.xdir == -1:
                self.rect.y += 20
                self.xdir = -self.xdir
            self.rect.x += self.xdir
            ran = random.randrange(1, 400)
            if ran == 50:
                af.append(Alienfire(self.rect.centerx, self.rect.bottom))
                alienfire.add(af[len(af) - 1])
                all_sprites.add(af[len(af) - 1])
              
def drawaliens():
    for j in range(5):       
        for i in range(10):
            a = Aliens(15 + 35*i,50 + 35*j)
            aliens.add(a)
            all_sprites.add(a)

drawaliens()


class Bonusalien(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(alienbonus_img, (20, 20))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 20

        def update(self):
            self.rect.x += 5
            if self.rect.left >500:
                self.kill()
            
                
                
class Sides(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((10, 500))
            self.image.fill(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


ls = Sides(0 ,0)
sides.add(ls)
all_sprites.add(ls)

rs = Sides(490 ,0)
sides.add(rs)
all_sprites.add(rs)


class Player(pygame.sprite.Sprite):
        def __init__(self, a, b, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((a, b))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

def playerpart1():
    p1 = Player(50,10,250,460)
    playerparts.add(p1)
    all_sprites.add(p1)
    return p1

def playerpart2():
    p2 = Player(5,5, 274,455)
    playerparts.add(p2)
    all_sprites.add(p2)
    return p2

p1 = playerpart1()
p2 = playerpart2()


class Bullets(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(bullet_img, (5, 20))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def update(self):
            self.rect.y -= 6
            if self.rect.bottom < 0:
                self.kill()
            
            
def shoot():
    b = Bullets(p2.rect.x, 435)
    bullets.add(b)
    all_sprites.add(b)


class Alienfire(pygame.sprite.Sprite):
        def __init__(self,x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((3, 10))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def update(self):
            self.rect.y += 3
            if self.rect.top > 500:
                self.kill()


class Defences(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((10, 10))
            self.image.fill(GREEN)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


def builddefences():
    for k in range(4):
        for j in range(4):
            for i in range(5):
                d = Defences(70+i*10 + k*100,400 + j*10)
                defences.add(d)
                all_sprites.add(d)

builddefences()


# infinite loop

while run:
    
    # creates time delay 
    
    pygame.time.delay(td) 
      
    # iterate over the list of Event objects   
    # that was returned by pygame.event.get() method.
    
    for event in pygame.event.get(): 
          
        # if event object type is QUIT   
        # then quitting the pygame   
        # if space bar shoot
        
        if event.type == pygame.QUIT: 
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot()


    # update all sprites 

    all_sprites.update()

    # player movement
    
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and p1.rect.x> 10:
        p1.rect.x -= vel
        p2.rect.x -= vel
    if keys[pygame.K_RIGHT] and p1.rect.x< 440: 
        p1.rect.x += vel
        p2.rect.x += vel

        
    # check for enough lives left

    if L == 0:
        print(sc)
        run = False

    # check for collisions

    hits = pygame.sprite.groupcollide(aliens, bullets, True, True)
    if hits:
        pygame.mixer.Sound.play(explosion_sound)
        sc += 10

    hits = pygame.sprite.spritecollide(p1,aliens, True)
    if hits:
        pygame.mixer.Sound.play(explosion_sound)
        run = False

    hits = pygame.sprite.spritecollide(p1, alienfire, True)
    if hits:
        pygame.mixer.Sound.play(explosion_sound)
        L -= 1
        p1.kill()
        p2.kill()
        for i in range(3):
            clock.tick(1)
        p1 = playerpart1()
        p2 = playerpart2()
        for i in range(len(af)):
            af[i].kill()
        af = []


    hits = pygame.sprite.groupcollide(defences, bullets, True, True)

    hits = pygame.sprite.groupcollide(defences, alienfire, True, True)
    
    hits = pygame.sprite.groupcollide(defences, aliens, True, True)

    hits = pygame.sprite.groupcollide(bonusalien, bullets, True, True)
    if hits:
        rand = random.choice([50,100,150])
        sc += rand

    
    # completely fill the surface object   
    # with black colour & then chosen background
    
    win.fill(BLACK)

    win.blit(background, background_rect)

    # draw all sprites and score etc

    all_sprites.draw(win)

    draw_text(win, "Score " +str(sc), 18, 230, 10)
    draw_text(win, "Lives=" +str(L), 18, 30, 10)

    # draw any bonus aliens

    ran = random.randrange(1, 500)
    if ran == 5:
        ba = Bonusalien()
        bonusalien.add(ba)
        all_sprites.add(ba)


    # check is wall is fully destroyed and redraw and speed up

    if len(aliens) == 0:
        drawaliens()
        builddefences()
        td = 40 - screen*5
        if td < 5:
            td = 5
        screen +=1

    # speed up during screeen

    if len(aliens) == 30:
        td = 35 - screen*5
    if len(aliens) == 10:
        td = 30 - screen*5
    if td <= 5:
        td = 5
    if td > 20:
        vel = 4
    if td <= 20 and td > 10:
        vel = 3
    if td <= 10:
        vel = 2

    # refresh the window
    
    pygame.display.update()  
  
# closes the pygame window

pygame.quit() 


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

pygame.display.set_caption("Sramble2020!")

# Indicates pygame is running

run = True

# lives

L = 10

# time delay factor

td = 20

# set initial score

sc = 0

# game counter

counter = 0

# initial speed of player

vel = 4

# booster counter for extra speed

booster = 150

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
landscape = pygame.sprite.Group()
player = pygame.sprite.Group()
defenders = pygame.sprite.Group()
bullets = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
wallb = pygame.sprite.Group()
wallt = pygame.sprite.Group()
earth = pygame.sprite.Group()


# alien & bullet figures

game_folder = os.path.dirname(__file__)
defender_img = pygame.image.load(os.path.join(game_folder, "laserRed16.png")).convert()
background = pygame.image.load(os.path.join(game_folder, 'starfield.png')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(os.path.join(game_folder, "ufoRed.png")).convert()


# drawing on screen function

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



# create classes and related functions

class Wallb(pygame.sprite.Sprite):
        def __init__(self,x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((1, y))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = 500 - y

        def update(self):
            self.rect.x -= 1
            if self.rect.x < -20:
                self.kill()



class Wallt(pygame.sprite.Sprite):
        def __init__(self,x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((1, y))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = 0

        def update(self):
            self.rect.x -= 1
            if self.rect.x < -20:
                self.kill()


class Earth(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((200, 200))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = 100
            pygame.draw.circle(self.image, BLUE, self.rect.center, self.radius)
            self.rect.x = 510
            self.rect.y = 100


class Asteroid(pygame.sprite.Sprite):
        def __init__(self,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((24, 24))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = 12
            pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.x = 510
            self.rect.y = random.randrange(0, y)
            self.xdir = -2

        def update(self):
            self.rect.x += self.xdir
            if self.rect.right < 0:
                self.kill()


def createasteroids(a,b):
    ran = random.randrange(1, a)
    if ran == 4:
        AL.append(Asteroid(b))
        asteroids.add(AL[len(AL)-1])
        all_sprites.add(AL[len(AL)-1])


class Defenders(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(defender_img, (5, 20))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = 480 - y
            self.diry = 0

        def update(self):
             self.rect.x -= 1
             self.rect.y -= self.diry
             if self.rect.bottom < 0:
                 self.kill()
             if self.rect.x < -10:
                 self.kill()
             ran = random.randrange(1, 400)
             if ran == 50 and self.rect.x > 0 and self.rect.x < 500:
                 self.diry = 2


class Bullets(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((10, 3))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def update(self):
            self.rect.x += 6
            if self.rect.left > 500:
                self.kill()
        
     
def shoot():
    b = Bullets(p.rect.right, p.rect.y + 10)
    bullets.add(b)
    all_sprites.add(b)



class Landscape(pygame.sprite.Sprite):
        def __init__(self,x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((10, y))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = 500 - y

        def update(self):
            self.rect.x -= 1
            if self.rect.x < -10:
                self.kill()


class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(player_img, (20, 20))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = 200
            self.rect.y = 30

        def update(self):
            if self.rect.left > 480:
                self.rect.left = 480
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > 500:
                self.rect.bottom = 500
                
            
def playerreset():            
    p = Player()
    player.add(p)
    all_sprites.add(p)
    return p

p = playerreset()


# create rolling landscape and random defenders for phase one

y = 50
total = 0

while total < 600:

    rand1 = random.randrange(10,40)
    rand2 = random.randrange(10,40)
    rand3 = random.randrange(10,40)



    for i in range(total, total + rand1):
        increment = random.randrange(0,5)
        ls = Landscape(i*10, y)
        landscape.add(ls)
        all_sprites.add(ls)
        y += increment
        if y > 400:
            y = 400
        ran = random.randrange(1, 10)
        if ran == 5:
            d = Defenders(i*10, y)
            defenders.add(d)
            all_sprites.add(d)
    
    total += rand1
    

    for i in range(total, total + rand2):
        increment = random.randrange(0,5)
        ls = Landscape(i*10, y)
        landscape.add(ls)
        all_sprites.add(ls)
        direction = random.choice([1,2])
        if direction ==1:
            y += increment
        else:
            y -= increment
        if y < 50:
            y = 50
        if y > 400:
            y = 400
        ran = random.randrange(1, 10)
        if ran == 5:
            d = Defenders(i*10, y)
            defenders.add(d)
            all_sprites.add(d)
    
    total += rand2



    for i in range(total, total + rand3):
        increment = random.randrange(0,5)
        ls = Landscape(i*10, y)
        landscape.add(ls)
        all_sprites.add(ls)
        y -= increment
        if y < 50:
            y = 50
        ran = random.randrange(1, 10)
        if ran == 5:
            d = Defenders(i*10, y)
            defenders.add(d)
            all_sprites.add(d)
        
    total += rand3

# keep asteroid list

AL = []


# infinite game loop

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
            if event.key == pygame.K_SPACE and counter <= 6000:
                shoot()

    #update counter

    counter += 1

    # player movement
    
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]:
        p.rect.x -= vel
    if keys[pygame.K_RIGHT]: 
        p.rect.x += vel
    if keys[pygame.K_UP]:
        p.rect.y -= vel
    if keys[pygame.K_DOWN]: 
        p.rect.y += vel

     # emergency speed

    if keys[pygame.K_SPACE] and booster >0 and counter > 11000 : 
        p.rect.x += 3
        booster -= 1

    # create asteroids on random basis for part of phase one, and for phase two

    if counter > 1500 and counter <=3750:
        createasteroids(100,350)

    if counter > 3750 and counter <= 6500:
        createasteroids(50,350)

    if counter > 6500 and counter < 8500:
        createasteroids(25,480)

    if counter > 8500 and counter < 10500:
        createasteroids(12,480)

    # creating third phase of game set up

    if counter == 11000:

        total = 500
        ext = 0
        exb = 0
        tb = 0
        tt = 0
        c = 1
        wb = []
        wt = []
        td = 20

        ranb = random.randrange(50, 350)
        rant = 500 - ranb - random.randrange(25, 60)

        memoryt = []
        memoryb = []

        memoryt.append(rant)
        memoryb.append(ranb)

        while total < 4500:

            rand = random.randrange(50,300)
                    
            ranb = random.randrange(50, 350)
            rant = 500 - ranb - random.randrange(25, 60)

            memoryt.append(rant)
            memoryb.append(ranb)

            if memoryt[c] > memoryt[c-1]:
                ext = random.choice([30,40])
                exb = 0
            else:
                exb = random.choice([30,40])
                ext = 0
                        
            for i in range(total + tb, total + rand + exb):
                wb.append(Wallb(i, memoryb[c-1]))
                wallb.add(wb[len(wb) - 1])
                all_sprites.add(wb[len(wb) - 1])


            for i in range(total + tt, total + rand + ext):
                wt.append(Wallt(i, memoryt[c-1]))
                wallt.add(wt[len(wt) - 1])
                all_sprites.add(wt[len(wt) - 1])

            total += rand
            c += 1
            tb = exb
            tt = ext

            

    # update all sprites 

    all_sprites.update()
 
    # check for enough lives left

    if L == 0:
        print(sc)
        run = False

    # game speed resets
    
    if counter == 2000:
        td = 10
        vel = 2

    if counter == 4000:
        td = 5
        vel = 1

    if counter > 13500:
        td = 10 

    # check for collisions

    hits = pygame.sprite.spritecollide(p,defenders, True)
    if hits:
        pygame.mixer.Sound.play(explosion_sound)
        L -= 1
        p.kill()
        for i in range(3):
            clock.tick(1)
        p = playerreset()
        for i in range(len(AL)):
            AL[i].kill()
        AL = []


    hits = pygame.sprite.spritecollide(p,asteroids, True)
    if hits:
        pygame.mixer.Sound.play(explosion_sound)
        L -= 1
        p.kill()
        for i in range(3):
            clock.tick(1)
        p = playerreset()
        for i in range(len(AL)):
            AL[i].kill()
        AL = []
        

    hits = pygame.sprite.spritecollide(p,landscape, False)
    if hits:
        pygame.mixer.Sound.play(explosion_sound)
        L -= 1
        p.kill()
        for i in range(3):
            clock.tick(1)
        p = playerreset()
        for i in range(len(AL)):
            AL[i].kill()
        AL = []
        


    hits = pygame.sprite.groupcollide(bullets,defenders, True, True)
    if hits:
        sc += 10


    hits = pygame.sprite.groupcollide(asteroids,landscape, True, False)


    hits = pygame.sprite.spritecollide(p,wallb, False)
    if hits:
        pygame.mixer.Sound.play(explosion_sound)
        L -= 1
        for i in range(3):
            clock.tick(1)
        if counter - 11500 + p.rect.x + 20 <= 20:
            p.rect.x -= 30
        else:
            p.rect.x = wb[counter - 11500 + p.rect.x + 20].rect.x
            p.rect.y = wb[counter - 11500 + p.rect.x + 20].rect.y - 25


    hits = pygame.sprite.spritecollide(p,wallt, False)
    if hits:
        pygame.mixer.Sound.play(explosion_sound)
        L -= 1
        for i in range(3):
            clock.tick(1)
        if counter - 11500 + p.rect.x + 20 <= 20:
            p.rect.x -= 30
        else:
            p.rect.x = wb[counter - 11500 + p.rect.x + 20].rect.x
            p.rect.y = wb[counter - 11500 + p.rect.x + 20].rect.y - 25


    hits = pygame.sprite.spritecollide(p,earth, False)
    if hits:
        sc += L*100
        print("Congratualtions! - You made it home. Your final score is:")
        print(sc)
        run = False


    # arrive home and miss sequence

    if counter == 16000:
        e = Earth()
        earth.add(e)
        all_sprites.add(e)

    if counter > 16000:
        e.rect.x -= 1
        if e.rect.right <0:
            print("You are stranded in space! - Your final score is:")
            if sc <=200:
                sc = 200
            print(sc - 200)
            run = False

    
    # scores during second and third phase

    if counter > 6000 and counter < 10500 and counter%10 ==0:
        sc += 2 

    if counter > 11000 and counter < 15450 and counter%100 == 0:
        sc += 10

    
    # completely fill the surface object   
    # with black colour & then chosen background
    
    win.fill(BLACK)

    win.blit(background, background_rect)

    # draw all sprites and score etc

    all_sprites.draw(win)

    draw_text(win, "Score " +str(sc), 18, 230, 10)
    draw_text(win, "Lives=" +str(L), 18, 30, 10)
    if counter > 11000:
        draw_text(win, "Booster Fuel=" +str(booster), 18, 400, 10)

    # refresh the window
    
    pygame.display.update()  
  
# closes the pygame window

pygame.quit() 


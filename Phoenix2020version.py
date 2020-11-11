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

pygame.display.set_caption("Phoenix 2020!")
    
# lives

L = 3

# initial round of game

round = 0

# set initial score

sc = [0]


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
balls = pygame.sprite.Group()
wall = pygame.sprite.Group()
queenalien = pygame.sprite.Group()


# alien & bullet figures

game_folder = os.path.dirname(__file__)
alien_img = pygame.image.load(os.path.join(game_folder, "enemyBlue5.png")).convert()
queenalien_img = pygame.image.load(os.path.join(game_folder, "ufoRed.png")).convert()
bullet_img = pygame.image.load(os.path.join(game_folder, "laserRed16.png")).convert()
player_img = pygame.image.load(os.path.join(game_folder, "enemyBlue5.png")).convert()
background = pygame.image.load(os.path.join(game_folder, 'starfield.png')).convert()
background_rect = background.get_rect()



# drawing on screen function

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



# create classes and related functions etc

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
            self.ydir = 0

        def update(self):
            hits = pygame.sprite.spritecollide(rs, aliens, False)
            if hits and self.xdir ==1:
                self.xdir = -self.xdir
            hits1 = pygame.sprite.spritecollide(ls, aliens, False)
            if hits1 and self.xdir == -1 :
                self.xdir = -self.xdir
            self.rect.x += self.xdir
            self.rect.y += self.ydir
            ran = random.randrange(1, 400)
            if ran == 50:
                af.append(Alienfire(self.rect.centerx, self.rect.bottom))
                alienfire.add(af[len(af) - 1])
                all_sprites.add(af[len(af) - 1])
            ran1 = random.randrange(1, 500)
            if ran1 == 250:
                self.xdir = random.choice([2,3,-2,-3])
                self.ydir = random.randrange(1, 3)
            if self.rect.top > 500:
                self.rect.bottom = 1
            if self.rect.left > 500:
                self.rect.right = 1
            if self.rect.right < 0:
                self.rect.left = 499




def drawaliens(rows, level):
    for j in range(rows):       
        for i in range(10):
            a.append(Aliens(15 + 35*i,level + 35*j))
            aliens.add(a)
            all_sprites.add(a)


def redraw(rows, level):
    count = 0
    for j in range(rows):       
        for i in range(10):
            a[count].rect.x = 15 + 35*i
            a[count].rect.y = level + 35*j
            count += 1

    for i in range(len(a)):
        a[i].xdir = 1
        a[i].ydir = 0

                                
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
            
b = []
     
def shoot():
    b.append(Bullets(p2.rect.x, 435))
    bullets.add(b[len(b) - 1])
    all_sprites.add(b[len(b) - 1])



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
                

class Ball(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((24, 24))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = 12
            pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.x = random.choice([35,455])
            self.rect.y = random.randrange(0, 300)
            self.xdir = random.choice([1,2,3])
            self.ydir = random.choice([1,2,3])

        def update(self):    
            self.rect.x += self.xdir
            self.rect.y += self.ydir
            if self.rect.top > 500:
                self.rect.bottom = 1
    

ball = [0 for _ in range(40)]          


def drawball(n):
    for i in range(n):
        ball[i] = Ball()
        all_sprites.add(ball[i])
        balls.add(ball[i])


def redrawball(n):  
    for i in range(n):
        ball[i].rect.x = random.choice([35,455])
        ball[i].rect.y = random.randrange(0, 300)
                        


class Wall(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 10))
            self.image.fill(GREEN)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

brick = []

def drawwall():
    for k in range(16):
        for i in range(15-(k*2)):
            brick.append(Wall(50 + i*25 + 25*k,200 + k*10))
            wall.add(brick)
            all_sprites.add(brick)
    for k in range(2):
        for i in range(15):
            brick.append(Wall(50 + i*25,150 + k*10))
            wall.add(brick)
            all_sprites.add(brick)
    for k in range(3):
        for i in range(6):
            brick.append(Wall(50 + i*25,170 + k*10))
            wall.add(brick)
            all_sprites.add(brick)
    for k in range(3):
        for i in range(6):
            brick.append(Wall(275 + i*25,170 + k*10))
            wall.add(brick)
            all_sprites.add(brick)
    
                
class Queenalien(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(queenalien_img, (20, 20))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = 240
            self.rect.y = 175

        def update(self):
            ran = random.randrange(1, 50)
            if ran == 40:
                af.append(Alienfire(self.rect.centerx, self.rect.bottom))
                alienfire.add(af[len(af) - 1])
                all_sprites.add(af[len(af) - 1])
            
            

# controlling overall loop

while L >0:

    # bonus lives per round

    L += 2

    # Indicates pygame is running

    run = True

    # first part of game - aliens

    a = []

    drawaliens(3,50)

    # time delay factor

    td = 20 - round*5

    # screen number

    screen = 1

    # internal infinite loop

    while run:

        # creates time delay 
        
        pygame.time.delay(td) 

        def eventkeys():
        
        # iterate over the list of Event objects   
        # that was returned by pygame.event.get() method.
                
            for event in pygame.event.get(): 
                      
                # if event object type is QUIT   
                # then quitting the pygame   
                # if space bar shoot
                    
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        shoot()

        eventkeys()

        # update all sprites 

        all_sprites.update()


        def movement():
        
        # player movement
        
            keys = pygame.key.get_pressed() 
            if keys[pygame.K_LEFT] and p1.rect.x> 10:
                p1.rect.x -= vel
                p2.rect.x -= vel
            if keys[pygame.K_RIGHT] and p1.rect.x< 440: 
                p1.rect.x += vel
                p2.rect.x += vel
            
        movement()


        # check for enough lives left

        def lives():
        
            lives = L
            status = run
            
            if lives == 0:
                print(sc[0])
                status = False

            return status

        run = lives()
            

        def collisions(a,b):

        # check for collisions

            cp1 = p1
            cp2 = p2
            lives = L

            hits = pygame.sprite.groupcollide(aliens, bullets, True, True)
            if hits:
                pygame.mixer.Sound.play(explosion_sound)
                sc[0] += 10

            hits = pygame.sprite.spritecollide(cp1,aliens, True)
            if hits:
                pygame.mixer.Sound.play(explosion_sound)
                lives -= 1
                cp1.kill()
                cp2.kill()
                for i in range(3):
                    clock.tick(1)
                cp1 = playerpart1()
                cp2 = playerpart2()
                # to send aliens back to base and remove stray fire
                redraw(a,b)
                for i in range(len(af)):
                    af[i].kill()


            hits = pygame.sprite.spritecollide(cp1, alienfire, True)
            if hits:
                pygame.mixer.Sound.play(explosion_sound)
                lives -= 1
                cp1.kill()
                cp2.kill()
                for i in range(3):
                    clock.tick(1)
                cp1 = playerpart1()
                cp2 = playerpart2()
                # to send aliens back to base and remove stray fire
                redraw(a,b)
                for i in range(len(af)):
                    af[i].kill()


            return lives, cp1, cp2

        L, p1, p2 = collisions(3,50)

        def drawscreen():
            
            # completely fill the surface object   
            # with black colour & then chosen background
            
            win.fill(BLACK)

            win.blit(background, background_rect)

            # draw all sprites and score etc

            all_sprites.draw(win)

            draw_text(win, "Score " +str(sc[0]), 18, 230, 10)
            draw_text(win, "Lives=" +str(L), 18, 30, 10)

        drawscreen()


        # check is wall is fully destroyed and redraw and speed up

        if len(aliens) == 0:
            screen +=1
            if screen == 3:
                run = False
                for i in range(len(af)):
                    af[i].kill()
                for i in range(len(b)):
                    b[i].kill()
                af = []
                b =[]
            if screen < 3:
                a = []
                drawaliens(3, 50)
            td = td - 5
            if td <= 5:
                td = 5
            

        # refresh the window
        
        pygame.display.update()  


    # reset variables for second part of game - balls 
    
    td = 20
    counter = 0
    screen = 1
    
    for i in range(3):
        clock.tick(i)

    if L > 0:
        run = True
        drawball(10 + round*5)


    # internal infinite loop

    while run:
        
        # creates time delay 
        
        pygame.time.delay(td) 
          
        # quit and shoot functions
        
        eventkeys()

        # update all sprites 

        all_sprites.update()

        # player movement
        
        movement()
            
        # check for enough lives left

        run = lives()

        # check for collisions

        for i in range(10 + round*5 + counter):
            hits = pygame.sprite.spritecollide(ball[i], sides, False)
            if hits:
                ball[i].xdir = -ball[i].xdir


        hits = pygame.sprite.spritecollide(p1, balls, True)
        if hits:
            pygame.mixer.Sound.play(explosion_sound)
            L -= 1
            p1.kill()
            p2.kill()
            for i in range(3):
                clock.tick(1)
            p1 = playerpart1()
            p2 = playerpart2()
            redrawball(counter + 9 + round*5)


        hits = pygame.sprite.groupcollide(balls, bullets, True, True)
        if hits:
            pygame.mixer.Sound.play(explosion_sound)
            sc[0] += 10
            if counter <15:
                counter += 1
                ball[counter + 9 + round*5] = Ball()
                all_sprites.add(ball[counter + 9 + round*5])
                balls.add(ball[counter + 9 + round*5])

        
        # draw screens and scores etc
        
        drawscreen()

        # check is balls are fully destroyed and redraw and speed up

        if len(balls) == 0:
            screen +=1
            if screen == 3:
                run = False
                for i in range(len(b)):
                    b[i].kill()
                b =[]
            if screen < 3:
                counter = 0
                drawball(10 + round*5)
            td = td - 5

        # refresh the window
        
        pygame.display.update()  


    # reset variables for third part of game - kill queen

    td = 15
    for i in range(3):
        clock.tick(i)

    if L > 0:
        run = True
        drawwall()
        qa = Queenalien()
        queenalien.add(qa)
        all_sprites.add(qa)
        a = []
        drawaliens(1 + round, 175)

    while run:

        # creates time delay 
        
        pygame.time.delay(td) 
        
        # quit and shoot functions
        
        eventkeys()

        # update all sprites 

        all_sprites.update()
        
        # player movement
        
        movement()

        # check for enough lives left

        run = lives()

        # check for collisions

        hits = pygame.sprite.groupcollide(wall, bullets, True, True)
            
        hits = pygame.sprite.spritecollide(qa, bullets, True)
        if hits:
            pygame.mixer.Sound.play(explosion_sound)
            qa.kill()
            sc[0] += 100
            run = False
            for i in range(len(af)):
                af[i].kill()
            for i in range(len(b)):
                b[i].kill()
            af = []
            b = []

        L, p1, p2 = collisions(1 + round, 175)
        

        # draw screens and scores etc

        drawscreen()
            
        # refresh the window
        
        pygame.display.update()

    # create delay, clear sprites and then return to first part of game at higher level of difficulty 

    for i in range(3):
        clock.tick(i)

    for i in range(len(brick)):
        brick[i].kill()

    for i in range(len(a)):
        a[i].kill()


    round += 1
    if round == 4:
        round = 3

# closes the pygame window

pygame.quit() 


import pygame 
import random


# activate the pygame library .   
# initiate pygame and give permission   
# to use pygame's functionality.

pygame.init() 

# create the display surface object   
# of specific dimension(500, 500).

win = pygame.display.set_mode((500, 500)) 
   
# bat start co-ordinates

x = 400
y = 450

# ball start co-ordinates

a = 150
b = 150
  
# dimensions of the bat

width = 50
height = 10

# ball directions

c = 1
d = 1

# velocity / speed of movement of bat

vel = 2
  
# Indicates pygame is running

run = True

# lives

lives = 10

# time delay factor

td = 8

# list for bricks in wall

w = [1 for _ in range(1800)]


# set initial score
sc = 0


# set starting position of wall and counter for moving walls down

sp = 110
mdc = 0

# variable for end of game if wall encroaches on base

end = 0

# sound effects

beep_sound = pygame.mixer.Sound("beep.wav")
beep_sound2 = pygame.mixer.Sound("beep2.wav")
beep_sound3 = pygame.mixer.Sound("beep3.wav")

# functions for drawing bricks in wall 

def gwall(l,r):
         pygame.draw.rect(win,(0, 255, 0), (l, r, width, height))

def bwall(l,r):
         pygame.draw.rect(win,(0, 0, 255), (l, r, width, height))    

def cwall(q,r,s):
    e = 0
    dir = d
    score = sc
    for i in range (10):
            # if wall reaches bat end game
            if w[i+s] == 1 and r >= 450:
                e = 1  
            if w[i+s] == 1:
                if i%2 == q:
                    gwall(i*50,r)
                else:
                    bwall(i*50,r)
                if b <= r + 10 and b > r and a >=(i*50) and a <= (i*50 + 49):
                    w[i+s] = 0
                    pygame.mixer.Sound.play(beep_sound2)
                    score = score + 10
                    dir = -dir
                    break
    return dir, score, e


# infinite loop

while run:

    # display score

    pygame.display.set_caption(str(sc))
    
    # creates time delay 
    
    pygame.time.delay(td) 
      
    # iterate over the list of Event objects   
    # that was returned by pygame.event.get() method.
    
    for event in pygame.event.get(): 
          
        # if event object type is QUIT   
        # then quitting the pygame   
        # and program both.
        
        if event.type == pygame.QUIT: 
              
            # it will make exit the while loop
            
            run = False
            
    # stores keys pressed
    
    keys = pygame.key.get_pressed() 
      
    # if left arrow key is pressed
    
    if keys[pygame.K_LEFT] and x>0: 
          
        # decrement in x co-ordinate
        
        x -= vel 
          
    # if right arrow key is pressed
    
    if keys[pygame.K_RIGHT] and x<500-width: 
          
        # increment in x co-ordinate
        
        x += vel 

    # movement of ball code
    
    a += c
        
    b += d

    if b >= 500:
        lives -= 1
        if lives == 0:
            print(sc)
            run = False 
        a = random.randint(100,400)
        b = random.randint(250,260)
        c=1

    if b <= 0:
        d = -d
 

    if b >= 440 and b <= 450 and d ==1 and a >=(x+25) and a <= (x+40):
        d = -d
        c = 1
        mdc += 1.5
        pygame.mixer.Sound.play(beep_sound3)

    if b >= 440 and b <= 450 and d ==1 and a >(x+40) and a <= (x+55):
        d = -d
        c = 3
        mdc += 1.5
        pygame.mixer.Sound.play(beep_sound)
    elif a > 500:
        c = - c

    if b >= 440 and b <=450 and d ==1 and a >=(x-5) and a < (x+10):
        d = -d
        c = -3
        mdc += 1.5
        pygame.mixer.Sound.play(beep_sound)
    elif a <= 0:
        c = -c 

    if b >= 440 and b <= 450 and d ==1 and a >=(x+10) and a <= (x+25):
        d = -d
        c = -1
        mdc += 1.5
        pygame.mixer.Sound.play(beep_sound3)

            
    # completely fill the surface object   
    # with black colour
    
    win.fill((0, 0, 0)) 
      
    # drawing bat and ball
    
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

    pygame.draw.circle(win, (255, 0, 0), (a, b), 5, 1)

    # construct wall

    LC = int((mdc -5)/30)

    for j in range(1,7):
        if mdc >= 5*j and mdc < (5*j) + 5:
            sp = 110 + j*20
            for i in range(j):
                d, sc, end = cwall(i%2,sp - 120 - 10*i,10*i + 60)
                if end == 1:
                    run = False
                # next line not strictly required but helps with graphics 
                cwall(i%2,sp - 120 - 10*i,10*i + 60)
                

    for j in range(7 +(LC-1)*6, 13+(LC - 1)*6):
        if mdc >= 5*j and mdc < (5*j) + 5:
            sp = 110 + j*20
            for i in range(j- LC*6):
                d, sc, end = cwall(i%2,sp - ((LC+1)*120) - 10*i,10*i + ((LC+1)*60))
                if end == 1:
                    run = False
                # next line not strictly required but helps with graphics 
                cwall(i%2,sp - ((LC+1)*120) - 10*i,10*i + ((LC+1)*60)) 

            for k in range(1, LC+1):
                for i in range (6):
                    d, sc, end = cwall(i%2,sp - (120*k) - 10*i,10*i + (60*k))
                    if end == 1:
                        run = False
                    # next line not strictly required but helps with graphics 
                    cwall(i%2,sp - (120*k) - 10*i,10*i + (60*k))
        
     
    for i in range (6):
        d, sc, end = cwall(i%2,sp - 10*i,10*i)
        if end == 1:
            run = False
        # next line not strictly required but helps with graphics 
        cwall(i%2,sp - 10*i,10*i)
        

    # speeding up game at certain score intervals

    if sc == 1000:
        td = 6
    if sc == 2000:
        td = 4
    
    pygame.display.update()  
  
# closes the pygame window

pygame.quit() 


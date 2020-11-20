import pygame 
import random
import os

# activate the pygame library .   
# initiate pygame and give permission   
# to use pygame's functionality.

pygame.init() 

# create the display surface object   
# of specific dimension(500, 500).

win = pygame.display.set_mode((500, 500)) 
   
# head start co-ordinates

a = 150
b = 150
  
# initial head directions

c = 1
d = 0

# Indicates pygame is running

run = True

# time delay factor

td = 8

# set initial score

sc = 0

# set radius of snake head

r = 5

# sound effects

beep_sound = pygame.mixer.Sound("beep3.wav")

# start position of food

x = 250
y = 250

e = 300
f = 300

# lists and counters for number and positions of snake parts

newa = [0]
newb = [0]
co = 1
pn = 0

# lists for colour combinations for snake

c1 = [0,255,255,255,0,0,0]
c2 = [0,0,255,255,255,255,0]
c3 = [0,255,0,255,255,0,255]

for i in range(7, 250001):
    c1.append(c1[i-6])
    c2.append(c2[i-6])
    c3.append(c3[i-6])

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

    # movement of ball code to choose direction
      
    # if left arrow key is pressed
    
    if keys[pygame.K_LEFT]: 
          
        # decrement in a co-ordinate
        if c == 0:
            c = -1
            d = 0
          
    # if right arrow key is pressed
    
    if keys[pygame.K_RIGHT]: 
          
        # increment in a co-ordinate
        if c == 0:
            c = 1
            d = 0

    # if up arrow key is pressed
    
    if keys[pygame.K_UP]: 
          
        # decrement in b co-ordinate
        if d == 0:
            d = -1
            c = 0

    # if down arrow key is pressed
    
    if keys[pygame.K_DOWN]: 
          
        # increment in b co-ordinate
        if d == 0:
            d = 1
            c = 0

    # keep memory of past movements
    
    newa.append(a)
    newb.append(b)

    # movement of ball code after direction chosen
    
    a += c
        
    b += d

    co += 1

    if b >= 500 - r:
        run = False
        print(sc)

    if b <= 0 + r:
        run = False
        print(sc) 

    if a >= 500 - r:
        run = False
        print(sc)

    if a <= 0 + r:
        run = False
        print(sc)
            
    # completely fill the surface object   
    # with black colour
    
    win.fill((0, 0, 0)) 
      
    # drawing snake head

    pygame.draw.circle(win, (255, 0, 0), (a, b), r*2 , 4)

    # drawing food pills code
    
    pygame.draw.rect(win, (255, 0, 0), (x,y, 15, 15))

    if a >= x+1and a <= x+14 and b >= y+1 and b <= y+14:
        pn += 1
        x = random.randint(0,485)
        y = random.randint(0,485)
        sc = sc + 10
        pygame.mixer.Sound.play(beep_sound)

    pygame.draw.rect(win, (255, 0, 0), (e,f, 15, 15))

    if a >= e+1 and a <= e+14 and b >= f+1 and b <= f+14:
        pn += 1
        f = random.randint(0,485)
        e = random.randint(0,485)
        sc = sc + 10
        pygame.mixer.Sound.play(beep_sound)

    # drawing additional snake parts when food eaten 
    
    for i in range(1, pn + 1):
        if newa[co-(15*i)] > 0:
            col1 = c1[i]
            col2 = c2[i]
            col3 = c3[i]
            pygame.draw.circle(win, (col1, col2, col3), (newa[co-(15*i)], newb[co-(15*i)]), r*2 , 4)

    # checking for snake collisions with itself

    for i in range(1, pn + 1):
        if a >= newa[co - 15 - i*15] -5 and a <= newa[co - 15 - i*15] +5 and b >= newb[co - 15 - i*15] -5 and b <= newb[co - 15 - i*15] +5:
            run = False
            print(sc)
        
    # speeding up game at certain score intervals

    if sc == 150:
        td = 6
    if sc == 300:
        td = 4
    if sc == 450:
        td = 3

    # updating screen
    
    pygame.display.update()  
  
# closes the pygame window

pygame.quit() 


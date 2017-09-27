#Snake game 
import pygame
import sys
import random
import time

check_error= pygame.init()
if(check_error[1])>0:
    print("Had {0} initializing errors , so exiting ".format(check_error[1]))
    sys.exit(-1)
else:
    print("Snake game initialized successfully")
    
#Play Surface
playSurface = pygame.display.set_mode((640,560))
pygame.display.set_caption("Snake Game")

#Colors

red= pygame.Color(255,0,0) #Game over
green= pygame.Color(0,255,0) #Snake color
blue = pygame.Color(0,0,255) #Score
white = pygame.Color(255,255,255)#Background
yellow = pygame.Color(255,255,0) #Food

#FPS Controller

fps=pygame.time.Clock()

#Variables

snake_pos=[100,50]
snake_body=[[100,50],[90,50],[80,50]]

#Food position

food_pos=[random.randrange(1,64)*10,random.randrange(1,56)*10]
food_spawn = True
direction ='RIGHT'
changeto= direction

#Game over func

def game_over():
    myFont= pygame.font.SysFont('monoco',72)
    gSurf=myFont.render('Game Over!',True,red)
    gRect=gSurf.get_rect()
    gRect.midtop=(300,10)
    playSurface.blit(gSurf,gRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit(-1)
    

#Game Events - Keys hit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type== pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT or event.key==ord('d'):
                changeto='RIGHT'
            if event.key==pygame.K_LEFT or event.key==ord('a'):
                changeto='LEFT'
            if event.key==pygame.K_UP or event.key==ord('w'):
                changeto='UP'
            if event.key==pygame.K_DOWN or event.key==ord('s'):
                changeto='DOWN'
            if event.key==pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            

 #direction validation
        if changeto=='RIGHT' and not direction=='LEFT':
            direction='RIGHT'
        if changeto=='LEFT' and not direction=='RIGHT':
            direction='LEFT'
        if changeto=='UP' and not direction=='DOWN':
            direction='UP'
        if changeto=='DOWN' and not direction=='UP':
            direction='DOWN'
        
# set position
        if direction=='RIGHT':
            snake_pos[0]=snake_pos[0]+10
        if direction == 'LEFT':
            snake_pos[0]=snake_pos[0]-10
        if direction == 'UP':
            snake_pos[1]=snake_pos[1]-10
        if direction == 'DOWN':
            snake_pos[1]+=10

#snake body definition
        snake_body.insert(0,list(snake_pos))
    #check if snake ate the food
        if snake_pos[0]==food_pos[0] and snake_pos[1]==food_pos[1]:
            food_spawn = False #disappear food 
        else:
            snake_body.pop() #reduce body size
    
        if food_spawn==False :
            food_pos=[random.randrange(1,64)*10,random.randrange(1,56)*10]#create new food
        food_spawn = True
    
    #drawings
    
    playSurface.fill(white)
    for pos in snake_body:
        pygame.draw.rect(playSurface,green,pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(playSurface,yellow,pygame.Rect(food_pos[0],food_pos[1],10,10))
        #pygame.draw.circle(playSurface,yellow,(food_pos[0],food_pos[1]),5,0)
    
    if snake_pos[0]>630 or snake_pos[0]<0:
        game_over()
    if snake_pos[1]>550 or snake_pos[1]<0:
        game_over()
    
    for block in snake_body[1:]:
        if snake_pos[0]==block[0] and snake_pos[1]==block[1]:
            game_over()
    
    pygame.display.flip()
    fps.tick(50)

    



import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)



gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('ya porfin')

clock = pygame.time.Clock()
bulletImg=pygame.image.load('C:/Users/57310/Downloads/bullet.png')
tankImg=pygame.image.load('C:/Users/57310/Downloads/tanque.png')
alienImg=pygame.image.load('C:/Users/57310/Downloads/alli.png')
background=pygame.image.load('C:/Users/57310/Downloads/space.jpg')
car_width=230
def tank(x,y):
    gameDisplay.blit(tankImg,(x,y))
def bullet(x1,y1):
    gameDisplay.blit(bulletImg,(x1,y1))
def alien(x2,y2):
    gameDisplay.blit(alienImg,(x2,y2))
def alien2(x3,y3):
    gameDisplay.blit(alienImg,(x3,y3))
def back(x,y):
    gameDisplay.blit(background,(x,y))

def text_objects(text,font):
    textSurface= font.render(text,True,red)
    return textSurface,textSurface.get_rect()

def message_displayb(text):
    texto = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text,texto)
    TextRect.center = ((50),(20))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    
def message_displayl(text):
    texto = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text,texto)
    TextRect.center = ((43),(45))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update() 


def message_display(text):
    texto = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = text_objects(text,texto)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
    
def crash():
    gameDisplay.fill(white)
    message_display('Game Over')
def game_loop():

    bullets=3
    x= (display_width * 0.3)
    y= (display_width * 0.6-20)
    x1= (x+175)
    y1= (y)
    x2=150
    y2=0
    yal_change=0.2
    xal_change=1
    x_change=0
    k=1
    level=1
    gameExit = False
    back(display_width/2, display_height/2)
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change=-5
                elif event.key == pygame.K_RIGHT:
                    x_change=5
                elif event.key == pygame.K_SPACE:
                    x1= (x+175)
                    
                    while(y1>10):
                        y1=y1-20
                        bullet(x1,y1)
                        pygame.display.update()
                    time.sleep(0.02)
                    bullets=bullets-1
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                    x_change=0
                    y1=y
            
        x=x+x_change
        
        
        if(x2>display_width):
            xal_change=-xal_change
            x2=display_width
        elif(x2<0):
            xal_change=-xal_change
            x2=1
        if(abs(x2-x1+20)<40 and y1<y2):
            x2=random.randint(0,display_width)
            dir=random.randint(1,2)
            y2=0
            xal_change=pow(-1,dir)*k
            yal_change=0.05*(1+k)
            k=k+1
            bullets=3
            level=level+1
            
            
        y1=y
        x2=x2+xal_change
        y2=y2+yal_change
        gameDisplay.fill(white)
        back(0, 0)
        tank(x,y)
        alien(x2,y2)
        te=['Bullets: ',str(bullets)]
        t="".join(te)
        le=['Level: ',str(level)]
        l="".join(le)
        message_displayb(t)
        message_displayl(l)
        if x > display_width-car_width or x < -140 or abs(y2-y)<10 or bullets==0:
           crash()
        pygame.display.update()
        
        clock.tick(60)
game_loop()
pygame.quit()
quit()

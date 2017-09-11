import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600
bright_red=(255,0,0)
bright_green=(0,255,0)
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0, 200, 0)
car_width = 92
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText=pygame.font.Font('freesansbold.ttf',95)
        TextSurf, TextRect = text_objects("racey", largeText)
        TextRect.center = (display_width * 0.5, display_height * 0.5)
        gameDisplay.blit(TextSurf, TextRect)
        #buttons
        mouse = pygame.mouse.get_pos()#get mouse position
        #print(mouse)
        if (150+100) > mouse[0] > 150 and (450+50) > mouse[1] > 450:
             pygame.draw.rect(gameDisplay,red,(150,450,100,50))
        pygame.draw.rect(gameDisplay,green,(150,450,100,50))
        pygame.draw.rect(gameDisplay,red,(550,450,100,50))        
        

        pygame.display.update()
        clock.tick(15)
        
def crash():
    message_display('You Crashed')
    
def car(x,y):
    gameDisplay.blit(carImg,(x,y))
    
def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (display_width * 0.5, display_height * 0.5)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(4)
    game_loop()

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things_dodged(count):
    font=pygame.font.SysFont(None, 25)
    text=font.render("Dodged "+ str(count), True, black)
    gameDisplay.blit(text, (0,0))
    
def game_loop():
    x=(display_width * 0.45)
    y=(display_height * 0.8)
    x_change=0
    
    thing_startx = random.randrange(0,display_width)
    thing_starty = -300
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    dodged=0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change=0
        x += x_change
                    
        gameDisplay.fill(white)
        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        
        if x > display_width - car_width or x < 0:
          crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx=random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
        
        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()
            
        
        pygame.display.update()#pygame.display.flip()
        clock.tick(60)#frames per second
game_intro()
game_loop()        
pygame.quit()
quit()

input()
        

    



    

    

    


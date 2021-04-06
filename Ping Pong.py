#Justin Hoang & Anh Ha
#September 3rd, 2020

#import python libraries
import pygame
import pygame.mixer
from pygame import *

#Initializing pygame and sounds function
pygame.init()
sounds = pygame.mixer
sounds.init()

exit = False #keep the game open
fps = 60
clock = pygame.time.Clock() #Initiated the second counter for (frame per second (fps))
FPS = clock.tick(fps) #frame per second (DO NOT MOVE or CHANGE THIS LINE)
font = pygame.font.SysFont("candara",50) #font to render scores
font2 = pygame.font.SysFont("candara",70) #font to render Win/Lose
font3 = pygame.font.SysFont("candara",30) #font to render 'How to restart/quit'

#Sounds 
sound1 = sounds.Sound("whoos.wav") #bounces off
sound2 = sounds.Sound("tick.wav") 

#Activate sound functions
def play_s1 ():
    sound1.play()
    
def play_s2 ():
    sound2.play()

#set up the colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

#Game's window
pygame.display.set_caption('Ping Pong Py') #window's name
size = (800,600) #input window size (x/y)
screen = pygame.display.set_mode(size) # "run" the window
background = screen.convert()
background.fill(BLACK)


#create players
player = pygame.Surface((10,90)) #"draw" the bar

p1 = player.convert() #put pixel unit of the bar same as the screen
p1.fill(WHITE) #colour

p2 = player.convert()
p2.fill(WHITE)


#creat ball
the_circ= pygame.Surface((15,15))
circ = pygame.draw.circle(the_circ,(WHITE),(7,7),7)
circle = the_circ.convert()


# positions of players
p1_x = 10  #bar 1's position
p1_y = 270

p2_x = 780 #bar 2's position
p2_y = 270


#bar's initial movement
p1_move = 0 
p2_move = 0


# positions of the ball
circle_x = 393
circle_y = 300


#ball's speed
speed_x = 110
speed_y = 110
speed_circ = 110

#Scores
p1_score = -1
p2_score = -1
p3_score = 0
p4_score = 0


#Players' speed
z1 = 1.0


while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit = True
            pygame.quit()
            
        if event.type == KEYDOWN:          
            #restart button
            if event.key == K_RETURN: 
                fps = 50
                p1_score = 0
                p2_score = 0
                circle_x, circle_y = 393, 300  #reset ball's position
                p1_y,p2_y = 270, 270  #reset bar's position
             
            #quit button    
            elif event.key == K_ESCAPE:
                exit = True
                pygame.quit()
                
            #keybind for players
            if event.key == K_s:
                p1_move = +z1
            elif event.key == K_w:
                p1_move = -z1
            if event.key == K_DOWN:
                p2_move = +z1               
            elif event.key == K_UP:
                p2_move = -z1
                
        elif event.type == KEYUP:
            if event.key == K_s:
                p1_move = 0
            elif event.key == K_w:
                p1_move = 0
            if event.key == K_DOWN:
                p2_move = 0
            elif event.key == K_UP:
                p2_move = 0
              
              
    #print out scores on the screen          
    score1 = font.render(str(p1_score), True, WHITE) 
    score2 = font.render(str(p2_score), True, WHITE)
    score3 = font.render(str(p3_score), True, WHITE) 
    score4 = font.render(str(p4_score), True, WHITE)
 
 
    #set up the play ground
    screen.blit(background,(0,0))
    border = pygame.draw.rect(screen,(WHITE),Rect((5,5),(790,590)),3)
    middle_border = pygame.draw.aaline(screen,(WHITE),(400,5),(400,595))
 
    #draw player and ball onto the screen
    screen.blit(p1,(p1_x,p1_y))
    screen.blit(p2,(p2_x,p2_y))
    screen.blit(circle,(circle_x,circle_y))
    if p1_score and p2_score == -1:
        screen.blit(score3,(310,280))
        screen.blit(score4,(460,280))
    else:
        screen.blit(score1,(310,280))
        screen.blit(score2,(460,280))

    p1_y += p1_move
    p2_y += p2_move
        
    
    #ball's speed base on fps
    z2 = 450 #Increse the number to make the ball slower and opposite
    circle_x += speed_x /z2
    circle_y += speed_y /z2
    
    
    #keep bars in the screen
    if p1_y <= 10:
        p1_y = 10
    elif p1_y >= 495:
        p1_y = 495
    if p2_y <= 10:
        p2_y = 10
    elif p2_y >= 495:
        p2_y = 495
        
    
    #when ball hit the borders and bounches off
    if circle_x <= 10:
        speed_x = -speed_x
        circle_x = 10
    elif circle_x >= 790:
        speed_x = -speed_x
        circle_x = 790
    if circle_y <= 10:
        speed_y = -speed_y
        circle_y = 10
    elif circle_y >= 580:
        speed_y = -speed_y
        circle_y = 580
    
    
    #when ball hit the bars and bounches off
    if circle_x <= p1_x + 10:
        if circle_y >= p1_y - 7.8 and circle_y <= p1_y + 84.5:
            play_s1()
            circle_x = 20
            speed_x = -speed_x

            
    if circle_x >= p2_x - 15:
        if circle_y >= p2_y - 7.8 and circle_y <= p2_y + 84.5:
            play_s1()
            circle_x = 765
            speed_x = -speed_x

    #when ball hit the borders and +1 point
    if circle_x <= 10:
        p2_score += 1
        play_s2 ()
        #circle_x, circle_y = 393, 300  #reset ball's position after score
        #p1_y,p2_y = 270, 270  #reset bar's position after score
    elif circle_x >= 790:
        p1_score += 1
        play_s2 ()
        #circle_x, circle_y = 393, 300  #reset ball's position after score
        #p1_y, p2_y = 270, 270  #reset bar's position after score
        
    #Best of --- 3
    NumOfRounds = 3; #Change this to increase of decrease number of rounds (default 3)
    if p1_score == -1:
        circle_x, circle_y = 393, 300 
        p1_y,p2_y = 270, 270
        fps = 0
        resl3 = font3.render(str("Press 'Enter' to start"), True, WHITE)
        screen.blit(resl3,(255,500))
        
    elif p1_score >= NumOfRounds:
        resl1 = font2.render(str("Win"), True, YELLOW) 
        resl2 = font2.render(str("Lose"), True, WHITE)
        resl3 = font3.render(str("Press 'Enter' to restart"), True, WHITE)
        resl4 = font3.render(str("Press 'Esc' to quit"), True, RED)
        circle_x, circle_y = 393, 300  #reset ball's position after score
        p1_y,p2_y = 270, 270  #reset bar's position after score
        fps = 0
        screen.blit(resl1,(170,280))
        screen.blit(resl2,(550,280))
        screen.blit(resl3,(240,500))
        screen.blit(resl4,(265,550))
        
    elif p2_score >= NumOfRounds:
        resl1 = font2.render(str("Lose"), True, YELLOW) 
        resl2 = font2.render(str("Win"), True, WHITE)
        resl3 = font3.render(str("Press 'Enter' to restart"), True, WHITE)
        resl4 = font3.render(str("Press 'Esc' to quit"), True, RED)
        circle_x, circle_y = 393, 300  #reset ball's position after score
        p1_y,p2_y = 270, 270  #reset bar's position after score
        fps = 0
        screen.blit(resl1,(170,280))
        screen.blit(resl2,(550,280))
        screen.blit(resl3,(240,500))
        screen.blit(resl4,(265,550))
    
    pygame.display.flip() 

    #extensive code comments due to the fact no many people can understanding coding
    #For all the programmers out there (these comments aren't meant for you, and you know
    # who they are for)

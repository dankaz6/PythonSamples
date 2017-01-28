'''
Created on Sep 10, 2016

@author: kazsoft
'''

import pygame 
import sys
from pygame.locals import *

def main():
    
    HOME_X = 20
    HOME_Y = 20

    pygame.init()
    screen = pygame.display.set_mode((400,400)) 

    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    PURPLE = (255,0,255)
    CYAN = (0,255,255)
    YELLOW = (255,255,0)
    
    circle_color = RED
    
    x = HOME_X
    y = HOME_Y

    font = pygame.font.SysFont("verdana", 20)
    label = font.render("Move the circle!", True, GREEN)
    pygame.draw.circle(screen, circle_color, (x,y), 10)
    screen.blit(label, (x,y+20))
    pygame.display.update()
    

    keep_looping = True
    while keep_looping:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                keep_looping = False
                
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT):
                    x -= 10
                elif (event.key == pygame.K_RIGHT):
                    x += 10
                elif (event.key == pygame.K_UP):
                    y -= 10
                elif (event.key == pygame.K_DOWN):
                    y += 10
                elif (event.key == pygame.K_HOME):
                    x = HOME_X
                    y = HOME_Y
                elif (event.key == pygame.K_PAGEDOWN):
                    x += 10
                    y += 10
                elif (event.key == pygame.K_PAGEUP):
                    x -= 10
                    y -= 10
                elif (event.key == pygame.K_b):
                    circle_color = BLUE
                elif (event.key == pygame.K_g):
                    circle_color = GREEN
                elif (event.key == pygame.K_r):
                    circle_color = RED
                elif (event.key == pygame.K_p):
                    circle_color = PURPLE
                elif (event.key == pygame.K_c):
                    circle_color = CYAN
                elif (event.key == pygame.K_m):
                    circle_color = YELLOW

        screen.fill(BLACK)
        pygame.draw.circle(screen, circle_color, (x,y), 10)
        screen.blit(label, (x,y+20))
        pygame.display.update()

    pygame.display.quit()
    pygame.quit()
    sys.exit(0)     




if (__name__ == "__main__"):
    main()
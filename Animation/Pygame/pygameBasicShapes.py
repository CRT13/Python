"""
A basic-shapes-plot program using pygame
"""
################################ Import Libraries ##############################
import pygame, sys
from pygame.locals import *
############################## Function Description ############################
def pygameBasicShapes():
    flag = True
    #Colour Calues
    black = (0,0,0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0,255, 0)
    #User-I/P Display
    print('==========================================')
    print('=========== PyGame:Basic Shapes ==========')
    print('==========================================')
    print('1. Line')
    print('2. Rectangle')
    print('3. Ellipse')
    print('4. Circle')
    print('5. Polygon')
    print('==========================================')
    usrInput = int(input('Please Select: '))
    while flag:
        pygame.init()
        canvas = pygame.display.set_mode((300,400))
        pygame.display.set_caption('Basic Shapes')
        canvas.fill(black)
        if usrInput == 1:
            pygame.draw.line(canvas,white,(100,100),(200,200),2)
        elif usrInput == 2:
            pygame.draw.rect(canvas,white,(100,100,100,200),2)
        elif usrInput == 3:
            pygame.draw.ellipse(canvas,white,(100,100,100,200),2)
        elif usrInput == 4:
            pygame.draw.line(canvas,white,(100,100),2)
        elif usrInput == 5:
            pygame.draw.polygon(canvas, white, ((100,100), (200,200), (100,200), (200, 100)), 2)
        else:
            print('Incorrect Input!')
            flag = False
        pygame.display.update()
        break
##################################################################################
################################## Main Program ##################################
try:
    check = True
    while check:
        pygameBasicShapes()
        check = int(input('Redraw?(1/0)'))
except:
    print('Error! Try Again')
##################################################################################


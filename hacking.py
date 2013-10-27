# -*- coding: utf-8 -*-
import pygame
import random
import sys
import os
import webbrowser
import time
import sqlite3 as lite

sys.path.append('./package')

# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)

class Computer(pygame.sprite.Sprite):
    posx = 0
    posy = 0

    def __init__(self, color, posx, posy, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        
        self.image = pygame.image.load("image/computer.png")

        self.posx = posx
        self.posy = posy

        self.rect = self.image.get_rect()

        self.rect.x = posx
        self.rect.y = posy
        

class Visor(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        # Set a transparent color
        self.image = pygame.Surface([width, height])
        self.image.fill((255,0,255))
        self.image.set_colorkey((255,0,255))
        self.image.set_alpha(50)

        self.rect = self.image.get_rect()

def drawVisor(screen,x,y):
    pygame.draw.circle(screen, black, [x, y], 20, 1)
    pygame.draw.circle(screen, black, [x, y], 15, 1)
    pygame.draw.circle(screen, black, [x, y], 10, 1)
    pygame.draw.circle(screen, black, [x, y], 1, 1)
       
    pygame.draw.line(screen, black, [x-20, y], [x+20,y], 1)
    pygame.draw.line(screen, black, [x, y-20], [x,y+20], 1)
    

def main():
    print "Hacking"

    pygame.init()

    screen_width = 1280
    screen_height = 800
    screen=pygame.display.set_mode([screen_width,screen_height])

    icon = pygame.image.load("computer.bmp").convert_alpha()        
    pygame.display.set_icon(icon)


    pygame.display.set_caption("Hacking")

    done = False

    clock=pygame.time.Clock()

    pygame.mouse.set_visible(0)

    # Background imagea
        
    worldmapImage = pygame.image.load("image/worldmap.png").convert()

    font = pygame.font.Font(None, 25)

    computer_list = pygame.sprite.RenderPlain()
    all_sprites_list = pygame.sprite.RenderPlain()

    score = 0

    visor = Visor(red, 4, 4)
    all_sprites_list.add(visor)

    for i in range(20):
        computer = Computer(black, random.randrange(1280-20), random.randrange(635-15), 20, 15)
        computer_list.add(computer)
        all_sprites_list.add(computer)

    x_speed = 0
    y_speed = 0

    x_coord = 10
    y_coord = 10

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    done = True
                if event.key == pygame.K_LEFT:
                    x_speed=-3
                elif event.key == pygame.K_RIGHT:
                    x_speed=3
                elif event.key == pygame.K_UP:
                    y_speed=-3
                elif event.key == pygame.K_DOWN:
                    y_speed=3

                elif event.key == pygame.K_s:
                    print "Shoot!"
                    print str(pos[0]) + " " + str(pos[1])
                    for computer in computer_list:
                        if( pos[0] > computer.posx and  pos[0] < computer.posx+20 and pos[1] > computer.posy and pos[1] < computer.posy+15):
                            print "Hack!"
                            computer_list.remove(computer)
                            all_sprites_list.remove(computer)
                            score = score + 1
   
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_speed=0
                elif event.key == pygame.K_RIGHT:
                    x_speed=0
                elif event.key == pygame.K_UP:
                    y_speed=0
                elif event.key == pygame.K_DOWN:
                    y_speed=0
        

            # Left mouse click
            if pygame.mouse.get_pressed()[0] == True:
                mousex = pygame.mouse.get_pos()[0]
                mousey = pygame.mouse.get_pos()[1]
                print "Shoot!"
                for computer in computer_list:
                    if( mousex > computer.posx and  mousex < computer.posx+20 and mousey > computer.posy and mousey < computer.posy+15):
                        print "Hack!"
                        computer_list.remove(computer)
                        all_sprites_list.remove(computer)
                        score = score + 1
           


        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed

        screen.fill(black)

        pos = pygame.mouse.get_pos()

        screen.blit(worldmapImage, [0,0])
        


        text = font.render("Localisation: " + str(pos[0]) + " " + str(pos[1]), True, black)
        screen.blit(text, [10, 10])

        scoreText = font.render("Hacked Computer: " + str(score), True, black)
        screen.blit(scoreText, [10, 30])

        all_sprites_list.draw(screen)

        visor.rect.x= pos[0] - 2 
        visor.rect.y= pos[1] - 2
        drawVisor(screen, pos[0], pos[1])


        pygame.display.flip()
        clock.tick(20)

    pygame.quit()

#Run the script if executed
if __name__ == "__main__":
    main()

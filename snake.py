#!/usr/bin/env python3

#################################################
#   FILE:       snake.py                        #
#                                               #
#   AUTHORS:    Zach Barnes Gabi Chavez         #
#                                               #
#   DATA:       3/11/20                         #
#################################################

import tkinter as tk
import pygame
import sys
import random
from datetime import datetime


#*******************************************#
#                BOARD CLASS                #
#*******************************************#
class Board(object):
    def __init__(self, w: int = 500, h: int = 500, r: int = 20):
        self.__width = w
        self.__height = h
        self.__rows = r
        self.__gap = w // r
    
    def draw(self, window) -> None:
        gap = self.__width // self.__rows
        window.fill((225,225,225))
        x=0
        y=0
        for line in range(self.__rows):
            x=x+gap
            y=y+gap
            pygame.draw.line( window, (0,0,0), (x,0),(x,self.__width))
            pygame.draw.line( window,(0,0,0), (0,y), (self.__width,y))
        pygame.display.flip()
#############################################


#*******************************************#
#                SNAKE CLASS                #
#*******************************************#
class Snake(object):
    def __init__(self, x: int = 10, y: int = 10) -> None:
        self.__xV = 1    # x velocity
        self.__yV = 0    # y velocity
        self.__size = 3  # size of snake
        start_x = 10     # starting x coordinate
        start_y = 10     # starting y coordinate
        self.__head = Square(start_x, start_y) 
        self.__body = []
        self.__food = Square(15,15)
        for i in range(self.__size):
            start_x -= 1
            self.__body.append(Square(start_x, start_y))

    def update_pos(self):
        # Update head of snake according to velocities,
        # and body according to square in front of it
        if self.__head.x == self.__food.x and self.__head.y == self.__food.y:
            self.eat_food()
            self.grow()
        for i in range(self.__size - 1, -1, -1):
            if i == 0:
                self.__body[i].x = self.__head.x
                self.__body[i].y = self.__head.y
            else:
                self.__body[i].x = self.__body[i-1].x
                self.__body[i].y = self.__body[i-1].y

        self.__head.x += self.__xV # update x pos according to x velocity
        self.__head.y += self.__yV # update y pos according to y velocity


        if self.__head.x > 19:    # If snake has gone off right side of board:
            self.__head.x = 0     # Place snake left side of board
        if self.__head.x < 0:     # If snake has gone off of left side of board:
            self.__head.x = 19    # Place snake on right side of board

        if self.__head.y > 19:
            self.__head.y = 0
        if self.__head.y < 0:
            self.__head.y = 19

    def dir_up(self):
        # If not going down, change direction to up.
        if self.__yV != 1:   # if not going down
            self.__yV = -1   # go up
            self.__xV = 0    # don't move horizontally

    def dir_right(self):
        # If  not going left, change direction to right.
        if self.__xV != -1:  # if not going left
            self.__xV = 1    # go right
            self.__yV = 0    # don't move vertically

    def dir_left(self):
        # If not going right, change direction to left.
        if self.__xV != 1:  # if not going right
            self.__xV = -1  # go left
            self.__yV  = 0  # dont move horizontally

    def dir_down(self):
        # If not going up, change direction to down.
        if self.__yV != -1: # if not going up
            self.__yV = 1   # go down
            self.__xV = 0   # dont move vertically

    def eat_food(self):
        self.__food.x = random.randint(0,19)
        self.__food.y = random.randint(0,19)

    def grow(self):
        self.__size += 1
        self.__body.append(Square(1,1))

    def draw(self, window):
        self.__food.draw(window)
        self.__head.draw(window)
        for i in range(self.__size):
            self.__body[i].draw(window)

    # GETTERS
    def get__x(self):
        return self.__x
    def get__y(self):
        return self.__y
######################################


#**************************************#
#                Square                #
#**************************************#
class Square(object):
    def __init__(self, start_x, start_y):
        self.x = start_x # x coordinate
        self.y = start_y # y coordinate
        self.__gap = 500 // 20

    def draw(self, window):
         square = pygame.Surface((self.__gap - 1,self.__gap - 1))
         square.fill((255,0,0))
         window.blit(square, (self.x * self.__gap + 1 ,self.y * self.__gap + 1))
########################################


#************************************#
#                MAIN                #
#************************************#
def main():
    pygame.init()                               # Initialize pygame
    board = Board()                             # create board object
    snake  = Snake()
    window = pygame.display.set_mode((500,500)) # create window 500x500
    pygame.display.set_caption("Snake")         # Window title is Snake
    fps = pygame.time.Clock()                   # create clock object 
    running = True                              # boolean for game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()         # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.
        if keys[pygame.K_LEFT]:                 # Left pushed
            snake.dir_left()                    # Go left
        if keys[pygame.K_RIGHT]:                # Right pushed
            snake.dir_right()                   # Go right
        if keys[pygame.K_UP]:                   # Left pushed
            snake.dir_up()                      # Go up
        if keys[pygame.K_DOWN]:                 # Down pushed
            snake.dir_down()                    # Go down
        snake.update_pos()                      # update snake position
        board.draw(window)                      # draw board to window
        snake.draw(window)                      # draw snake to window
        pygame.display.flip()                   # update the window
        fps.tick(8)                            # max fps
        

# call main
if __name__ == "__main__":
    main()

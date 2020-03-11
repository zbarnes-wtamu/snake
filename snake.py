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


#*******************************************#
#                BOARD CLASS                #
#*******************************************#
class Board(object):
    def __init__(self, w: int = 500, h: int = 500, r: int = 20):
        self._width = w
        self._height = h
        self._rows = r
        self._gap = w // r
    
    def draw(self, window) -> None:
        gap = self._width // self._rows
        window.fill((225,225,225))
        x=0
        y=0
        for line in range(self._rows):
            x=x+gap
            y=y+gap
            pygame.draw.line( window, (255,0,0), (x,0),(x,self._width))
            pygame.draw.line( window,(255,0,0), (0,y), (self._width,y))


        pygame.display.flip()

    def draw_square(self, window, snake):
        square = pygame.Surface((self._gap,self._gap))
        square.fill((255,0,0))
        window.blit(square, (snake.get_x() * self._gap ,snake.get_y()*self._gap))
#############################################


#*******************************************#
#                SNAKE CLASS                #
#*******************************************#
class Snake(object):
    def __init__(self, x: int = 10, y: int = 10) -> None:
        self._x = x     # x pos
        self._y = y     # y pos
        self._xV = 1    # x velocity
        self._yV = 0    # y velocity
        self._size = 3  # size of snake
        self._body = [(int,int)*100]

    def update_pos(self):
        self._x += self._xV # update x pos according to x velocity
        self._y += self._yV # update y pos according to y velocity

        if self._x > 19:    # If snake has gone off right side of board:
            self._x = 0     # Place snake left side of board
        if self._x < 0:     # If snake has gone off of left side of board:
            self._x = 19    # Place snake on right side of board

        if self._y > 19:
            self._y = 0
        if self._y < 0:
            self._y = 19

    def dir_up(self):
        # If not going down, change direction to up.
        if self._yV != 1:   # if not going down
            self._yV = -1   # go up
            self._xV = 0    # don't move horizontally

    def dir_right(self):
        # If  not going left, change direction to right.
        if self._xV != -1:  # if not going left
            self._xV = 1    # go right
            self._yV = 0    # don't move vertically

    # GETTERS
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y

######################################


#************************************#
#                MAIN                #
#************************************#
def main():
    pygame.init()                               # Initialize pygame
    board = Board()                             # create board object
    window = pygame.display.set_mode((500,500)) # create window 500x500
    pygame.display.set_caption("Snake")         # Window title is Snake
    fps = pygame.time.Clock()                   # create clock object 
    snake = Snake()                             # create snake object
    running = True                              # boolean for game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()         # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.
        if keys[pygame.K_LEFT]:                 # We can check if a key is pressed like this
            pass
        if keys[pygame.K_RIGHT]:                # Right pushed
            snake.dir_right()                   # Go right
        if keys[pygame.K_UP]:                   # Left pushed
            snake.dir_up()                      # Go up
        if keys[pygame.K_DOWN]:
            pass
        snake.update_pos()                      # update snake position
        board.draw(window)                      # draw board to window
        board.draw_square(window, snake)        # draw snake to window
        pygame.display.flip()                   # update the window
        fps.tick(10)                            # max fps
        

# call main
if __name__ == "__main__":
    main()

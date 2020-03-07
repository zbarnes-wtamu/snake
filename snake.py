import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


WIDTH = 500
HEIGHT = 500
ROWS = 20


class cube( object ):
    rows = 0
    w = 0
    def __init__( self, start, dir_x=1, dir_y=0, color=( 255,0,0 ) ):
        pass

    def move( self, dir_x, dir_y ):
        pass

    def draw( self, surface, e_yes=False ):
        pass

class snake( object ):
    def __init__( self, color, pos ):
        pass

    def move( self ):
        pass

    def reset( self, pos ):
        pass

    def addCube( self ):
        pass

    def draw( self, surface ):
        pass


def draw_grid( w, rows, surface ):
    size_btwn = w // rows

    x = 0
    y = 0
    for l in range( rows ):
        x = x + size_btwn
        y = y + size_btwn

        # pygame.draw.line( surface, (255,0,0), (x,0), (x,w) )
        pygame.draw.line( surface, (255,0,0), (0,y), (w,y) )


def redraw_window( surface ):
    surface.fill(( 0, 0, 0 ))
    draw_grid( WIDTH, ROWS, surface )
    pygame.display.update()


def random_snack( rows, items ):
    pass

def message_box( subject, content ):
    pass

def main():
    rows = 20
    win = pygame.display.set_mode(( WIDTH, HEIGHT ))
    snakee = snake(( 255,0,0 ), ( 10, 10 ))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(100)
        clock.tick(10)

        redraw_window( win )



if __name__ == "__main__":
    main()

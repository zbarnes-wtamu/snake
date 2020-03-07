#!/usr/bin/env python3

import tkinter as tk
import pygame
import sys


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

class Snake(object):
    def __init__(self, x: int = 10, y: int = 10) -> None:
        self._x = x     # x pos
        self._y = y     # y pos
        self._xV = 1    # x velocity
        self._yV = 0    # y velocity
        self._size = 3  # size of snake
        self._body = [(int,int)*100]

    def update_pos(self):
        self._x += self._xV
        self._y += self._yV

        if self._x >= 20:
            self._x = 0
        if self._x <= 0:
            self._x = 20

        if self._y > 20:
            self._y = 1
        if self._y < 0:
            self._y = 20

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y

def main():
    pygame.init()
    board = Board()
    window = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Snake")
    fps = pygame.time.Clock()
    snake = Snake()
    running = True
    x=0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        board.draw(window)
        board.draw_square(window, snake)
        snake.update_pos()
        x+=1
        if x > 20:
            x = 1
        pygame.display.flip()
        fps.tick(14)
        

if __name__ == "__main__":
    main()

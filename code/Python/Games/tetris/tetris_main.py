import pygame
from pygame.locals import *
from random import randint

colors = [
    (48, 199, 239),
    (65, 182, 65),
    (238, 33, 43),
    (88, 102, 175),
    (240, 121, 34),
    (173, 78, 158),
    (245, 213, 7)
]

class Figure:
    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 2, 4, 5], [1, 5, 6, 10]],
        [[0, 1, 5, 6], [2, 5, 6, 9]]
        [[1, 2, 5, 9], [4, 5, 6, 10], [1, 5, 8, 9], [0, 4, 5, 6]],
        [[0, 1, 5, 9], [2, 4, 5, 6], [1, 5, 9, 10], [4, 5, 6, 8]],
        [[1, 4, 5, 6], [1, 5, 6, 9], [4, 5, 6, 9], [1, 4, 5, 9]],
        [[0, 1, 4, 5]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = randint(0, len(Figure.figures))
        self.rotation = 0
    
    @property
    def bitmap(self):
        return Figure.figures[self.type][rotation]

    def rotate(self, direction):
        self.rotation = (self.rotation + 1) % len(Figure.figures[self.type])

class Tetris:
    figure = None

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.figure = [[0 for i in range(width)] for j in range(height)]
    
    def new_figure(self):
        self.figure = Figure(self.width // 2 - 2, 0)
    
    def intersects(self):
        for px in self.figure.bitmap:
            x = self.figure.x + px // 4
            y = self.figure.y + px % 4
            if x < 0:
                return 'left'
            elif x > self.width:
                return 'right'
            elif y < 0:
                return 'down'
            elif y > self.height:
                return 'up'
            if self.field[y][x]:
                
        return False
    
    def drop(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()
    
    def down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()
    
    def move_x(self, dx):
        self.figure.x += dx
        if self.intersects():
            self.figure.x -= dx
            self.freeze()
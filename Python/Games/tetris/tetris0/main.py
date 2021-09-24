from random import shuffle
from math import log
from pickle import load, dump
from functools import partial
import sys
import pygame

# pylint: disable=no-member

pygame.init()

# Block colors ------------------------------------------ #
# COLORS = [
#     (48, 199, 239),
#     (88, 102, 175),
#     (240, 121, 34),
#     (245, 213, 7),
#     (65, 182, 65),
#     (173, 78, 158),
#     (238, 33, 43)
# ]

# Colors & constants ------------------------------------ #
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLOCK = 36
RES = (720, 720)
FALL = pygame.USEREVENT + 1
FONT = pygame.font.SysFont(pygame.font.get_default_font(), 32)

# Variables --------------------------------------------- #
buttons = []

# Display block ----------------------------------------- #
def block(surface, block_type, x, y, transclucent=False):
    image = pygame.image.load(f'images/{block_type}.png').convert()
    image = pygame.transform.scale2x(image)
    if transclucent:
        image.set_alpha(192)
    surface.blit(image, (x * BLOCK + 2, y * BLOCK + 2))

class Figure:
    # Figure shapes [I, J, L, O, S, T, Z] --------------- #
    FIGURES = [
        [[4, 5, 6, 7], [2, 6, 10, 14], [8, 9 ,10, 11], [1, 5, 9, 13]],
        [[0, 4, 5, 6], [1, 2, 5,  9 ], [4, 5, 6,  10], [1, 5, 8, 9]],
        [[2, 4, 5, 6], [1, 5, 9,  10], [4, 5, 6,  8 ], [0, 1, 5, 9]],
        [[0, 1, 4, 5]],
        [[1, 2, 4, 5], [1, 5, 6,  10], [5, 6, 8,  9 ], [0, 4, 5, 9]],
        [[1, 4, 5, 6], [1, 5, 6,  9 ], [4, 5, 6,  9 ], [1, 4, 5, 9]],
        [[0, 1, 5, 6], [2, 5, 6,  9 ], [4, 5, 9,  10], [1, 4, 5, 8]]
    ]
    bag = []

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.rotation = 0
        if len(Figure.bag):
            self.type = Figure.bag.pop()
        else:
            Figure.bag = list(range(7))
            shuffle(Figure.bag)
            self.type = Figure.bag.pop()

    def rotate(self, direction):
        self.rotation = (self.rotation + direction) % len(self.shape())
    
    def bitmap(self):
        return self.shape()[self.rotation]
    
    def shape(self):
        return Figure.FIGURES[self.type]

class Tetris:
    state = 'start'
    score = 0
    lines = 0
    level = 1

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.field = [[0 for i in range(width)] for j in range(height)]
        rect = (self.width * BLOCK, self.height * BLOCK)
        self.field_image = pygame.Surface(rect)
        self.new_figure()
        self.update()
    
    @property
    def highscore(self):
        try:
            with open('data.pkl', 'rb') as f:
                return load(f)
        except:
            return 0
    
    @highscore.setter
    def highscore(self, hscore):
        with open('data.pkl', 'wb') as f:
            dump(hscore, f)
    
    def update(self):
        image = self.field_image
        image.fill(GRAY)
        for y, row in enumerate(self.field):
            for x, px in enumerate(row):
                if px:
                    block(image, px - 1, x, y)
                else:
                    rect = (x * BLOCK + 2, y * BLOCK + 2, BLOCK - 4, BLOCK - 4)
                    pygame.draw.rect(image, WHITE, rect)
    
    def image(self):
        image = self.field_image.copy()
        figure = self.figure
        old_y = figure.y
        while not self.intersects():
            figure.y += 1
        figure.y -= 1
        dy = figure.y - old_y
        figure.y = old_y
        for px in figure.bitmap():
            x = figure.x + (px // 4)
            y = figure.y + (px % 4)
            pygame.draw.rect(image, GRAY, (x * BLOCK, y * BLOCK, BLOCK, BLOCK))
            block(image, figure.type, x, y)
            block(image, figure.type, x, y + dy, True)
        return image

    # Spawn a new piece --------------------------------- #
    def new_figure(self):
        self.figure = Figure(self.width // 2 - 2, 0)
    
    # Check for intersections --------------------------- #
    def intersects(self):
        intersections = 0
        bitmap = self.figure.bitmap()
        for px in bitmap:
            x = self.figure.x + px // 4
            y = self.figure.y + px % 4
            if (not -1 < x < self.width) or \
                y >= self.height or \
                    self.field[y][x]:
                    for px2 in bitmap:
                        dif = abs(px - px2)
                        if dif == 1 or dif == 4:
                            intersections += 1
        return intersections
    
    # Get call when a piece land ------------------------ #
    def land(self):
        for px in self.figure.bitmap():
            x = self.figure.x + px // 4
            y = self.figure.y + px % 4
            if y < 0:
                self.state = 'gameover'
                return
            self.field[y][x] = self.figure.type + 1
        self.clear_lines()
        self.update()
        self.new_figure()
    
    # Check for line clears ----------------------------- #
    def clear_lines(self):
        lines = 0
        for i, row in enumerate(self.field):
            if all(row):
                self.field.pop(i)
                self.field.insert(0, [0 for j in range(self.width)])
                lines += 1
        self.lines += lines
        if not lines: return
        self.level = lines // 8 + 1
        added_score = 800 if lines == 4 else (200 * lines - 100)
        self.score += added_score * self.level

    # Hard drop on space key ---------------------------- #
    def drop(self):
        old_y = self.figure.y
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.score += (self.figure.y - old_y) * 2 * self.level
        self.land()
    
    # Soft drop on down key ----------------------------- #
    def down(self, key=False):
        self.figure.y += 1
        self.score += self.level * key
        if self.intersects():
            self.figure.y -= 1
            self.land()
    
    # Move side ----------------------------------------- #
    def move_x(self, dx):
        self.figure.x += dx
        if self.intersects():
            self.figure.x -= dx

    # Rotate with wall push ----------------------------- #
    def rotate(self, dt):
        self.figure.rotate(dt)
        inter = self.intersects()
        old_x = self.figure.x
        while self.intersects():
            self.figure.x -= 1
            new_inter = self.intersects()
            if not new_inter: return
            elif new_inter < inter: continue
            else: break
        self.figure.x = old_x
        while self.intersects():
            self.figure.x += 1
            new_inter = self.intersects()
            if not new_inter: return
            elif new_inter < inter: continue
            else: break
        self.figure.x = old_x

# Base class for ui elements ---------------------------- #
class Widget(pygame.Surface):
    def __init__(self, rect, **kwargs):
        super().__init__(rect[2:])
        self.fill(WHITE)
        self.rect = rect
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def __setattr__(self, attr, value):
        self.__dict__[attr] = value
        if attr == 'color': self.fill(value)
        elif attr == 'text':
            text = FONT.render(value, True, BLACK)
            text_pos = ((self.get_width() - text.get_width()) // 2,\
                (self.get_height() - text.get_height()) // 2)
            self.blit(text, text_pos)
        elif attr == 'border':
            pygame.draw.rect(self, BLACK, self.get_rect(), value * 2, 12)

class Button(Widget):
    buttons = []
    def __init__(self, rect, command: callable, **kwargs):
        super().__init__(rect, **kwargs)
        self.call = command
        Button.buttons.append(self)
        
    @classmethod
    def check_click(cls, pos):
        for i in cls.buttons:
            if i.rect.collidepoint(pos): i.call()

# Main game --------------------------------------------- #
def main(window):
    pygame.key.set_repeat(150, 50)
    pygame.time.set_timer(FALL, 500, 1)

    game = Tetris(10, 20)
    hscore_text = FONT.render(f'High score: {game.highscore}', True, BLACK)

    # Gameloop ------------------------------------------ #
    while True:
        if game.state == 'gameover':
            window.blit(FONT.render('Game Over!', True, BLACK), (0, 0))
        # Events ---------------------------------------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if game.score > game.highscore:
                    game.highscore = game.score
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_DOWN: game.down(True)
                elif key == pygame.K_LEFT: game.move_x(-1)
                elif key == pygame.K_RIGHT: game.move_x(1)
                elif key == pygame.K_UP: game.rotate(-1)
                elif key == pygame.K_z: game.rotate(1)
                elif key == pygame.K_SPACE: game.drop()
            elif event.type == FALL:
                game.down()
                pygame.time.set_timer(FALL, int(500 / log(game.level + 1, 4)), 1)
        
        # Display --------------------------------------- #
        window.fill(WHITE)
        window.blit(game.image(), (0, 0))
        score_text = FONT.render(f'Score: {game.score}', True, BLACK)
        rect = window.blit(score_text, (game.width * BLOCK, 0))
        window.blit(hscore_text, (rect.x, rect.h))
        pygame.display.update()

def menu(window):
    title = FONT.render('Tetris', True, BLACK)
    play_button = Button(pygame.Rect(RES[0] // 2 - 50, 100, 100, 50), \
        partial(main, window), text='Play', border=2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                Button.check_click(event.pos)
        window.fill(WHITE)
        window.blit(title, ((RES[0] - title.get_width()) // 2, 60))
        window.blit(play_button, play_button.rect[:2])
        pygame.display.update()

if __name__ == '__main__':
    window = pygame.display.set_mode(RES)
    pygame.display.set_icon(pygame.image.load('images/icon.png'))
    pygame.display.set_caption('Tetris')
    menu(window)

# TODO
# - Menu
# - UI
# - Hold
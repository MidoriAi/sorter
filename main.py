import pygame as pg, sys
from pygame.locals import *
import random

pg.init()

s = pg.display.set_mode((500, 500))
pg.display.set_caption("Sorta")
clock = pg.time.Clock()

COLORS = [(255, 100, 100), (255, 255, 100), (100, 255, 100), (100, 255, 255), (255, 200, 255)]
BLACK = (50, 50, 50)

bar_list = []
bar_pos = 20
index = 0

class Bar:
    def __init__(self, color, x, y, h):
        self.color = color
        self.x = x
        self.y = y
        self.h = h

    def draw(self):
        # FLASHING AWESOME COLORS!!!
        # pg.draw.rect(s, random.choice(colors), (self.x, self.y, 20, self.h))
        pg.draw.rect(s, self.color, (self.x, self.y, 20, self.h))

def sort_heights():
    heights = []
    for b in bar_list:
        heights.append(b.h)
    heights.sort()
    return heights


while True:
    s.fill(BLACK)

    for e in pg.event.get():
        if e.type == QUIT:
            pg.quit()
            sys.exit()
        if e.type == KEYDOWN:
            if e.key == K_UP and bar_pos < 490:
                bar = Bar(random.choice(COLORS), bar_pos, 10, random.randint(10, 400))
                bar_list.append(bar)
                bar_pos += 40
            if e.key == K_DOWN and len(bar_list) > 0:
                bar_list.pop()
                bar_pos -= 40
            if e.key == K_SPACE:
                print(index)
                sorted_heights = sort_heights()
                for bar in bar_list:
                    bar.h = sorted_heights[index]
                    index += 1
                    print(index)
                index = 0
            if e.key == K_d:
                s.fill(BLACK)
                bar_pos = 20
                bar_list = []
                index = 0
    for bar in bar_list: bar.draw()

    clock.tick(60)
    pg.display.update()










import pygame
import math
from collections import deque
from Spot import *

WIDTH = 1200
HEIGHT = 720
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("A* Path Finding")

def heuristc(p1:Spot,p2:Spot) -> (int):
    x1,y1 = p1.get_pos_grid()
    x2,y2 = p2.get_pos_grid()
    return abs(x1-x2) + abs(y1-y2)

def make_grid(rows,cols,width=WIDTH,height=HEIGHT):
    grid = [];
    gap_col = width//cols
    gap_rows = height//rows
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(Spot(i,j,height,width,rows))
            #print(f"x: {i*gap_rows}, y: {j*gap_col}") # Debugging
        print()

    return grid

def draw_grid(window,rows,cols,width=WIDTH,height=HEIGHT):
    gap_col = width//cols
    gap_rows = height//rows

    for i in range(rows):
        pygame.draw.line(window,GREY, start_pos=(0,i*gap_rows),end_pos=(width,i*gap_rows))

    for j in range(cols):
        pygame.draw.line(window,GREY, start_pos=(j*gap_col,0),end_pos=(j*gap_col,height))


def draw(win,grid,rows,cols,width=WIDTH,height=HEIGHT):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win,rows=rows,cols=cols,width=width,height=height)
    pygame.display.update()

def get_clicked_pos(pos,rows,cols):
    gap_row = WIDTH//rows
    gap_col = HEIGHT/cols

    y,x = pos

    row,col = x//gap_row,y//gap_col

    return row,col


pygame.init()
clock = pygame.time.Clock()
running = True

const = WIDTH/HEIGHT
print(const)
ROWS = 60
COLS = 60 #int(5/3 * ROWS)

init_grid = make_grid(ROWS,COLS)

def print_grid(grid):
    for i in range(ROWS):
        for j in range(COLS):
            print(init_grid[i][j])
    


draw(WINDOW,init_grid,ROWS,COLS)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("fechou")
            running = False

    

    clock.tick(60)  # limits FPS to 60

pygame.quit()


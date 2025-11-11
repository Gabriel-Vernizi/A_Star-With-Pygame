import pygame
import math
import heapq as hq
from Spot import *

WIDTH = 1200
HEIGHT = 720
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("A* Path Finding")

def heuristc(p1:Spot,p2:Spot) -> (int):
    x1,y1 = p1.get_pos_grid()
    x2,y2 = p2.get_pos_grid()
    return abs(x1-x2) + abs(y1-y2)

def algorithm(draw,grid,start,end):
    pass

def make_grid(rows,cols,width=WIDTH,height=HEIGHT):
    grid = []
    gap_col = width//cols
    gap_rows = height//rows

    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(Spot(i,j,gap_rows,gap_col,rows,cols))
            # print(f"spot[{i}][{j}] -> x: {i*gap_rows}, y: {j*gap_col}") # Debugging
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

    I = 0
    for row in grid:
        for spot in row:
            
            # if I % 3 == 0:
            #     I += 1
            #     spot.color = BLUE
            #     # print(f"Color: {spot.color}")
            # if I % 3 == 1:
            #     I += 1
            #     spot.color = RED
            #     # print(f"Color: {spot.color}")
            # if I % 3 == 2:
            #     I += 1
            #     spot.color = ORANGE
            #     # print(f"Color: {spot.color}")

            spot.draw(win)

    draw_grid(win,rows=rows,cols=cols,width=width,height=height)
    pygame.display.update()

def get_clicked_pos(pos,rows,cols):


    gap_row = HEIGHT//rows
    gap_col = WIDTH//cols

    y,x = pos
    row,col = x//gap_col, y//gap_row
 
    return row,col


# Debugging
def print_grid(grid,ROWS,COLS):
    for i in range(ROWS):
        for j in range(COLS):
            print(grid[i][j].get_pos())


def main():
    ROWS = 60
    COLS = math.floor(5/3 * ROWS)

    start = None
    end = None

    started = False

    grid = make_grid(ROWS,COLS)  
    
    pygame.init()
    clock = pygame.time.Clock()
    running = True




    while running:
        draw(WINDOW,grid,rows=ROWS,cols=COLS,width=WIDTH,height=HEIGHT)
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        #draw(WINDOW,grid,ROWS,COLS)


        for event in pygame.event.get():
            

            if event.type == pygame.QUIT:
                print("fechou")
                running = False

            if started:
                # A* Algorithm
                continue
            
            # Left mouse click
            if pygame.mouse.get_pressed()[0]:
                row,col = get_clicked_pos(pygame.mouse.get_pos(),ROWS,COLS)
                try:
                    spot = grid[row][col]
                except IndexError as e:
                    print(f"row: {row}, col: {col}")
                    running=False
                    raise(e)
                
                if not start:
                    start = spot
                    start.make_start()
                
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                else:
                    if spot != start and spot != end:
                        spot.make_barrier()

            # Scroll Click
            if pygame.mouse.get_pressed()[1]: 
                row,col = get_clicked_pos(pygame.mouse.get_pos(),ROWS,COLS)
                try:
                    spot = grid[row][col]
                except IndexError as e:
                    print(f"row: {row}, col: {col}")
                    running=False
                    raise(e)

                spot.update_neighbor(grid)
                spot.color_neighbors(grid,ORANGE)
               
            # Right mouse click
            if pygame.mouse.get_pressed()[2]:
                row,col = get_clicked_pos(pygame.mouse.get_pos(),ROWS,COLS)
                try:
                    spot = grid[row][col]
                except IndexError as e:
                    print(f"row: {row}, col: {col}")
                    running=False
                    raise(e)

                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbor()

                    algorithm(lambda: draw(WINDOW,grid,rows=ROWS,cols=COLS,width=WIDTH,height=HEIGHT),grid,start,end)

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == '__main__':
    main()
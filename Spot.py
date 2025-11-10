import pygame

RED = (255, 0, 0) # Not Path
GREEN = (0, 255, 0) # Path
BLUE = (0, 255, 0) # Start
PURPLE = (128, 0, 128) # End
YELLOW = (255, 255, 0) 
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128) 
TURQUOISE = (64, 224, 208)
WHITE = (255, 255, 255) # Default
BLACK = (0, 0, 0) # Barrier

class Spot:
    def __init__(self,row,col,height,width,total_rows):
        self.row = row;
        self.col = col;

        self.height = height;
        self.width = width;

        self.x = row * width;
        self.y = col * height;

        self.color = RED  
        self.neighbors = [];
        self.total_rows = total_rows;

    def get_pos(self):
        return self.row,self.col;
    
    def get_pos_grid(self):
        return self.x,self.y;

    # Get Status
    def is_closed(self):
        return self.color == RED;

    def is_open(self):
        return self.color == WHITE;

    def is_barrier(self):
        return self.color == BLACK;

    def is_start(self):
        return self.color == BLUE;

    def is_end(self):
        return self.color == PURPLE;

    # Change Status

    def reset(self):
        self.color = WHITE;

    def make_closed(self):
        self.color = RED;

    def make_barrier(self):
        self.color = BLACK;

    def make_start(self):
        self.color = BLUE;

    def make_end(self):
        self.color = PURPLE;

    # Draw 
    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.x,self.y,self.width,self.height))

    # The algorithm doesn't search in diagonal, i.e, we only need to focus on adjacent neighbors
    def update_neighbor(self,grid):
        # spot[x-1][y]
        pass

    def __lt__(self,other):
        return False
    
    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"
    

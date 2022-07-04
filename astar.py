from turtle import width
from matplotlib.pyplot import cla
import pygame
import math
from queue import PriorityQueue

# Setting up the dipslay dimensions
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))

# Caption for the display
pygame.display.set_caption("A* Path Finding Algorithm")

# Some useful color codes
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Lets create a class called spot. We do this cause we need to build a visualisation tool before implementing the algorithm. So we create the class of all the individual grids cause they need to store info like location, row-col position, width, its neighbours etc.
class Spot:
    def __init__(self,row,col,width,total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE # All white cubes at start
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

# Getting position of the grid or spot
def get_pos(self):
    return self.row, self.col

# Black spots are barriers, red spots have been visited already and green ones are open. So we need to update whether a particular spot has been visited or not
# So we define a bunch of methods to get info about the spots and act accordingly

# Is spot closed?
def is_closed(self):
    return self.color == RED

# Is spot open?
def is_open(self):
    return self.color == GREEN

# Is the spot a barrier i.e is it blocked?
def is_barrier(self):
    return self.color == BLACK

# Is it a Starting node? 
def is_start(self):
    return self.color == ORANGE

# Is it an Ending node?
def is_end(self):
    return self.color == TURQUOISE

# Reset the node
def reset(self):
    self.color = WHITE

# Close the node
def make_closed(self):
    self.color = RED

# Open the node
def make_open(self):
    self.color = GREEN

# Barricade the node
def make_barrier(self):
    self.color = BLACK

# Make the node as end node
def make_end(self):
    self.color = TURQUOISE

# Make the node part of the path
def make_path(self):
    self.color = PURPLE

# Drawing the cubes
def draw(self,win):
    pygame.draw.rect(win, self.color,(self.x,self.y,self.width,self.width))

def update_neighbors(self,grid):
    pass

# __lt__ stands for less than which basically used to compare it with the previous instance of the object. Self and other
def __lt__(self,other):
    return False

# Creating the Heuristic function based on which our algorithm will run
def h(p1,p2):
    # p1 and p1 have 2 components
    x1 , y1 = p1
    x2 , y2 = p2
    # we use these components to calculte the absolute distance between p1 and p2 using the built in function abs
    return abs(x1-x2) + abs(y1-y2)



#!/usr/bin/env python3

import random

from window import *
from helpers import *

def main():
    resolution_width,resolution_length = 960,540
    win = Window(resolution_width, resolution_length)

    # Generate two random lines, that fit in the resolution of the window.
    # num_of_lines = 2
    # for i in range(num_of_lines):
    #     pointa = Point(random.randint(0,resolution_width),random.randint(0,resolution_length))
    #     pointb = Point(random.randint(0,resolution_width),random.randint(0,resolution_length))
    
    # Generate two random cells, that fit in the resolution of the window.
    # num_of_cells = 2
    # for i in range(num_of_cells):
    #     x1 = random.randint(0,resolution_width)
    #     y1 = random.randint(0,resolution_length)

    #     x2 = random.randint(0,resolution_width)
    #     y2 = random.randint(0,resolution_length)

    #     print(f"{x1},{y1} | {x2},{y2}")
    #     Cell(x1,x2,y1,y2,win).draw()


    cell = Cell(50,50,250,250,win)
    cell.has_bottom_wall=False
    cell.draw()


    win.wait_for_close()

main()
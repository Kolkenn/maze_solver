#!/usr/bin/env python3

import random

# Relative Imports to ensure file uses local modules.
from .window import *
from .maze import *
from .helpers import Cell

def main():
    resolution_width,resolution_length = 1000,500
    win = Window(resolution_width, resolution_length)

    Maze(25,25,5,5,75,75,win)

    win.wait_for_close()

if __name__ == '__main__':
    main()
import random

# Relative Imports to ensure file uses local modules.
from .window import Window
from .maze import Maze

def main():
    resolution_width,resolution_length = 1000,500
    print(f"Maze Solver is starting! Resolution {resolution_width}x{resolution_length}")
    win = Window(resolution_width, resolution_length)

    Maze(25,25,5,5,75,75,win)

    win.wait_for_close()

if __name__ == '__main__':
    main()
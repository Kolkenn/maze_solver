#!/usr/bin/env python3

import unittest
from src import Maze
# Syntax Exmaple to import from a specific file.
# from src.helpers import Line

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows,num_cols,10,10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
    
    def test_maze_cell_size(self):
        pass
    
if __name__ == "__main__":
    unittest.main()
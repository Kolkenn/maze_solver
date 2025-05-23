import unittest
from src import *
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
    
    def test_maze_entrance(self):
        num_cols = 15
        num_rows = 12
        m1 = Maze(0,0,num_rows,num_cols,10,10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[num_cols-1][num_rows-1].has_bottom_wall,
            False
        )

if __name__ == "__main__":
    unittest.main()
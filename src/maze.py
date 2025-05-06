import time

from .helpers import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                start_x = self._x1 + (i * self._cell_size_x)
                start_y = self._y1 + (j * self._cell_size_y)
                cell = Cell(
                    start_x,
                    start_y,
                    start_x + self._cell_size_x,
                    start_y + self._cell_size_y,
                    self._win
                    )
                self._cells[i].append(cell)
                self._draw_cell(i, j)
        self._break_entrance_and_exit()

    def _draw_cell(self,i,j):
        if not self._win:
            return
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        # Top Left Cell
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)

        # Bottom Right Cell
        column = self._num_cols-1
        row = self._num_rows-1
        self._cells[column][row].has_bottom_wall = False
        self._draw_cell(column,row)
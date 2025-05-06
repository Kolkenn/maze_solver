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


    def _draw_cell(self,i,j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
import time

from cell import *

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = None
        
        if num_cols <= 0 or num_rows <= 0:
            raise ValueError("num_cols and num_rows must be greater than 0")
        if cell_size_x <= 0 or cell_size_y <= 0:
            raise ValueError("cell_size_x and cell_size_y must be greater than 0")
        
        self._create_cells()
        
    def _create_cells(self):
        col_list = [Cell(self.win)] * self.num_rows
        self._cells = [col_list] * self.num_cols
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._draw_cell(i, j)
        
    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell._x1 = self.x1 + self.cell_size_x * j
        cell._y1 = self.y1 + self.cell_size_y * i
        cell._x2 = self.x1 + self.cell_size_x * (j + 1)
        cell._y2 = self.y1 + self.cell_size_y * (i + 1)
        cell.draw(cell._x1, cell._y1, cell._x2, cell._y2)
        self._animate()
        
    def _animate(self):
        if self.win == None:
            return
        time.sleep(0.005)
        self.win.redraw()
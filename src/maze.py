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
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        
        if num_cols <= 0 or num_rows <= 0:
            raise ValueError("num_cols and num_rows must be greater than 0")
        if cell_size_x <= 0 or cell_size_y <= 0:
            raise ValueError("cell_size_x and cell_size_y must be greater than 0")
        
        self._create_cells()
        
    def _create_cells(self):
        for c in range(self.num_cols):
            col_list = []
            for r in range(self.num_rows):
                cell = Cell(self.win)
                cell._x1 = self.x1
                cell._x2 = self.x1 + self.cell_size_x
                cell._y1 = self.y1
                cell._y2 = self.y1 + self.cell_size_y
                col_list.append(cell)
            self._cells.append(col_list)
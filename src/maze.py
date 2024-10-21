import time
import random

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
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        
        if num_cols <= 0 or num_rows <= 0:
            raise ValueError("num_cols and num_rows must be greater than 0")
        if cell_size_x <= 0 or cell_size_y <= 0:
            raise ValueError("cell_size_x and cell_size_y must be greater than 0")
        
        if seed:
            random.seed(seed)
            
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        
    def _create_cells(self):
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
        
    def _draw_cell(self, i, j):
        if self._win == None:
            return
        
        x1 = self.x1 + i * self.cell_size_x
        x2 = x1 + self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
        
    def _animate(self, t = 0.005):
        if self._win == None:
            return
        time.sleep(t)
        self._win.redraw()
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        
        self._cells[self.num_cols-1][self.num_rows-1].has_right_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)
        
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
       
        while True:
            candidates = []
            
            # left
            if i > 0 and not self._cells[i-1][j].visited:
                candidates.append((i-1,j))
            # right
            if i < self.num_cols - 1 and not self._cells[i+1][j].visited: 
                candidates.append((i+1,j))
            # top
            if j > 0 and not self._cells[i][j-1].visited:
                candidates.append((i,j-1))
            # bot
            if j < self.num_rows - 1 and not self._cells[i][j+1].visited:
                candidates.append((i,j+1))
        
            if len(candidates) == 0:
                self._draw_cell(i, j)
                return
            
            next = random.randrange(len(candidates))
            next_cell = candidates[next]
            
            if i + 1 == next_cell[0]:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if i - 1 == next_cell[0]:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            if j + 1 == next_cell[1]:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            if j - 1 == next_cell[1]:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            
            self._break_walls_r(next_cell[0], next_cell[1])
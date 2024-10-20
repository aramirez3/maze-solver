from window import *
from maze import *

def main():
    win_w = 800
    win_h = 600
    
    cell_size = 25
    x1 = cell_size
    y1 = cell_size
    rows = int((win_w - 2 * cell_size) / cell_size)
    cols = int((win_h - 2 * cell_size) / cell_size)
    win = Window(win_w, win_h)
    
    Maze(x1, y1, rows, cols, cell_size, cell_size, win)
    
    win.wait_for_close()
    
main()
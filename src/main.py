from window import *
from maze import *

def main():
    win_x = 800
    win_y = 600
    
    padding = 50
    size = 20
    cols = int((win_x - 2 * padding) / size)
    rows = int((win_y - 2 * padding) / size)
    win = Window(win_x, win_y)
    
    maze = Maze(padding, padding, rows, cols, size, size, win, 10)
    
    win.wait_for_close()
    
main()
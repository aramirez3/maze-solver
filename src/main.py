from window import *
from maze import *

def main():
    win_w = 800
    win_h = 600
    
    win = Window(win_w, win_h)
    
    Maze(50, 50, 14, 10, 50, 50, win)
    
    win.wait_for_close()
    
main()
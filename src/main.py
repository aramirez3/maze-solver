from window import *
from cell import *

def main():
    win = Window(800, 600)
    
    cell_closed = Cell(win)
    cell_closed.draw(10, 10, 20, 20)
    
    cell_open_top = Cell(win)
    cell_open_top.has_top_wall = False
    cell_open_top.draw(50, 50, 100, 100)
    
    
    win.wait_for_close()
    
main()
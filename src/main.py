from window import *
from cell import *

def main():
    win = Window(800, 600)
    
    cell_closed = Cell(win)
    cell_closed.draw(50, 50, 150, 150)
    
    cell_open_left = Cell(win)
    cell_open_left.has_left_wall = False
    cell_open_left.draw(250, 250, 350, 350)
    
    cell_open_top = Cell(win)
    cell_open_top.has_top_wall = False
    cell_open_top.draw(550, 350, 650, 450)
    
    cell_open_bottom = Cell(win)
    cell_open_bottom.has_bottom_wall = False
    cell_open_bottom.draw(150, 350, 250, 450)
    
    win.wait_for_close()
    
main()
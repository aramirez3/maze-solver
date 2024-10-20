from window import *
from cell import *

def main():
    win = Window(800, 600)
    
    cell_closed = Cell(win)
    cell_closed.draw(10, 10, 20, 20)
    
    cell_open_top = Cell(win)
    cell_open_top.has_top_wall = False
    cell_open_top.draw(700, 500, 750, 550)
    
    cell_open_bottom = Cell(win)
    cell_open_bottom.has_bottom_wall = False
    cell_open_bottom.draw(700, 450, 750, 500)
    
    cell_open_bottom.draw_move(cell_open_top)
    
    cell_open_left = Cell(win)
    cell_open_left.has_left_wall = False
    cell_open_left.draw(650, 500, 700, 550)
    
    cell_open_right = Cell(win)
    cell_open_right.has_right_wall = False
    cell_open_right.draw(600, 500, 650, 550)
    cell_open_right.draw_move(cell_open_left, True)
    
    cell_open_left.draw_move(cell_open_top, True)
    cell_open_top.draw_move(cell_closed)
    
    win.wait_for_close()
    
main()
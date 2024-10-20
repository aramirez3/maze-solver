from window import *

def main():
    win = Window(800, 600)
    
    # line = Line(Point(50, 50), Point(50, 550))
    # win.draw_line(line, "white")
    # line = Line(Point(50, 50), Point(750, 50))
    # win.draw_line(line, "white")
    # line = Line(Point(750, 50), Point(750, 550))
    # win.draw_line(line, "white")
    # line = Line(Point(750, 550), Point(50, 550))
    # win.draw_line(line, "white")
    cell_closed = Cell(win, True, True, True, True)
    cell_open_left = Cell(win, False, True, True, True)
    cell_open_top = Cell(win, True, True, False, True)
    cell_open_bottom = Cell(win, True, True, True, False)
    
    cell_closed.draw(Point(50, 50), Point(150, 150))
    cell_open_left.draw(Point(250, 250), Point(350, 350))
    cell_open_top.draw(Point(550, 350), Point(650, 450))
    cell_open_bottom.draw(Point(150, 350), Point(250, 450))
    win.wait_for_close()
    
main()
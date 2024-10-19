from window import *

def main():
    win = Window(800, 600)
    
    line = Line(Point(50, 50), Point(50, 550))
    win.draw_line(line, "white")
    line = Line(Point(50, 50), Point(750, 50))
    win.draw_line(line, "white")
    line = Line(Point(750, 50), Point(750, 550))
    win.draw_line(line, "white")
    line = Line(Point(750, 550), Point(50, 550))
    win.draw_line(line, "white")
    
    win.wait_for_close()
    
main()
from line import *
from point import *

class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win == None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        line_color_default = "white"
        line_color_remove_wall = "black"
        left_wall = line_color_default
        right_wall = line_color_default
        top_wall = line_color_default
        bottom_wall = line_color_default
        
        if self.has_left_wall == False:
            left_wall = line_color_remove_wall
        left = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(left, fill_color=left_wall)
        
        if self.has_right_wall == False:
            right_wall = line_color_remove_wall
        right = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(right, fill_color=right_wall)
        
        if self.has_top_wall == False:
            top_wall = line_color_remove_wall
        top = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(top, fill_color=top_wall)
        
        if self.has_bottom_wall == False:
            bottom_wall = line_color_remove_wall
        bottom = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(bottom, fill_color=bottom_wall)
            
    def draw_move(self, to_cell, undo=False):
        p1 = self.get_mid_point()
        p2 = to_cell.get_mid_point()
        line_color = "red2"
        if undo:
            line_color = "gray25"
        line = Line(p1, p2)
        self._win.draw_line(line, fill_color=line_color)
        
    def get_mid_point(self):
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
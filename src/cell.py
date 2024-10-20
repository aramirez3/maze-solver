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
        
        line_color_remove_wall = "black"
        
        left = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self._win.draw_line(left)
        if self.has_left_wall == False:
            self._win.draw_line(left, fill_color=line_color_remove_wall)
        
        right = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self._win.draw_line(right)
        if self.has_right_wall == False:
            self._win.draw_line(right, fill_color=line_color_remove_wall)
        
        top = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self._win.draw_line(top)
        if self.has_top_wall == False:
            self._win.draw_line(top, fill_color=line_color_remove_wall)
        
        bottom = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self._win.draw_line(bottom)
        if self.has_bottom_wall == False:
            self._win.draw_line(bottom, fill_color=line_color_remove_wall)
            
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
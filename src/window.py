from tkinter import Tk, BOTH, Canvas

class Window():
    
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(self.__root, bg="black",  height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False
        
    def draw_line(self, line, fill_color="white"):
        line.draw(self.__canvas, fill_color)
        
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def draw(self, canvas, fill_color="white"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color)
        
class Cell():
    def __init__(self, win,
        has_left_wall = True,
        has_right_wall = True,
        has_top_wall = True,
        has_bottom_wall = True,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0
        self._win = win

    def draw(self, p1, p2):
        self._x1 = p1.x
        self._y1 = p1.y
        self._x2 = p2.x
        self._y2 = p2.y
        
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
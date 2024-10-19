from tkinter import Tk, BOTH, Canvas

class Window():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.canvas = Canvas(self.root, {"bg": "white"})
        self.active = False
        
    def redraw(self):
        self.root.update_idletasks()
        
    def wait_for_close(self):
        self.active = True
        while self.active:
            self.redraw()
    
    def close(self):
        self.active = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
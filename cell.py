from tkinter import Tk, BOTH, Canvas
from gui import Point , line , Window
class Cell:
    def __init__(self,win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    def draw(self,x1,x2,y1,y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_top_wall:
            self._win.canvas.create_line(x1,y1,x2,y1)
        if self.has_bottom_wall:
            self._win.canvas.create_line(x1,y2,x2,y2)
        if self.has_left_wall:
            self._win.canvas.create_line(x1,y1,x1,y2)
        if self.has_right_wall:
            self._win.canvas.create_line(x2,y1,x2,y2)
            
    def draw_move(self,to_cell,undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_centre = half_length + self._x1
        y_centre = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_centre2 = half_length2 + to_cell._x1
        y_centre2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_centre, y_centre), Point(x_centre2, y_centre2))
        self._win.draw_line(line, fill_color)


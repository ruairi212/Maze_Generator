from tkinter import Tk, BOTH, Canvas
#creating a window class for tkinter whi
class Window:
    def __init__(self,width: int, height: int):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title("Maze Generator")
        self.canvas = Canvas(width=width, height=height)
        self.run = False
        self.canvas.pack()
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.run = True
        while self.run == True:
            self.redraw()

    def close(self):
        self.run = False
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class line:
    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2
        
    def draw(self,canvas,fill_color):
        canvas.create_line(self.point1.x,self.point1.y,self.point2.x,self.point2.y, fill=fill_color, width=2)
    def draw_line(self,canvas,fill_color):
        self.draw(canvas,fill_color)
class cell:
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
    def draw(self)

def main():
    win = Window(800,600)
    point1 = Point(200,300)
    point2 = Point(300,200)
    myline = line(point1,point2)
    myline.draw_line(win.canvas,"black")
    win.wait_for_close()
main()
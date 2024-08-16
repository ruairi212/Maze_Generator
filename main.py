from tkinter import Tk, BOTH, Canvas
from gui import Window , Point , line
from cell import Cell
def main():
    win = Window(800,600)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell1.draw(10, 60, 10, 60)
    cell2.draw(70, 120, 10, 60)
    win.wait_for_close()
main()
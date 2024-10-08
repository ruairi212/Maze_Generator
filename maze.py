import time
from cell import Cell
class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.create_cells()
    def create_cells(self):
        self._cells = [[]]
        new_cell_pos_x1 = self.x1
        new_cell_pos_y1 = self.y1
        for i in range(self.num_cols):
            new_cell_pos_x1 = self.x1
            self._cells.append([])
            for j in range(self.num_rows):
                cell = Cell(new_cell_pos_x1,new_cell_pos_y1)
                self._cells[i].append(cell)
                new_cell_pos_x1 += self.cell_size_x
            new_cell_pos_y1 += self.cell_size_y
    def draw_cell(self,i,j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i[j]].draw(x1,y1,x2,y2)
        self.animate()
    def animate(self):
        self.win.redraw()
        time.sleep(0.05)
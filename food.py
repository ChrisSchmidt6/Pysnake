# variables
import config as cf

class Food:
    width = cf.step
    height = cf.step

    def __init__(self, canvas, x, y):
        self.stepx = x
        self.stepy = y

        coord_x = x * self.width
        coord_y = y * self.height
        self.cref = canvas.create_rectangle(coord_x, coord_y, coord_x + cf.step, coord_y + cf.step, outline="", fill=cf.targer_color)
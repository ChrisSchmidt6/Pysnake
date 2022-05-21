# variables
import config as cf

class SnakeSection:
    width = cf.step
    height = cf.step

    def __init__(self, canvas, section_id, x, y, nx, ny, section_type="body", color=cf.snake_body_color):
        # set current, next, and previous steps
        self.stepx = x
        self.stepy = y
        self.next_stepx = nx
        self.next_stepy = ny
        self.prev_stepx = x
        self.prev_stepy = y - 1
        self.type = section_type
        
        # create instance on canvas and store reference to it
        coord_x = x * self.width
        coord_y = y * self.height
        self.cref = canvas.create_rectangle(coord_x, coord_y, coord_x + self.width, coord_y + self.height, outline="", fill=color)

        # id based on registry length
        self.section_id = section_id

    def move(self, nx, ny):
        self.last_stepx = self.stepx
        self.last_stepy = self.stepy
        self.stepx = self.next_stepx
        self.stepy = self.next_stepy
        self.next_stepx = nx
        self.next_stepy = ny
# variables
import config as cf

def hit(snake, next_x, next_y):
    # detect for collision with self
    for section in snake:
        if(next_x == section.stepx and next_y == section.stepy):
            return True
    
    # detect for collision with game edge
    left_edge = 0
    top_edge = 0
    right_edge = (cf.canvas_width / cf.step) - 1
    bottom_edge = (cf.canvas_height / cf.step) - 1
    if(next_x < left_edge or next_y < top_edge or next_x > right_edge or next_y > bottom_edge):
        return True

    return False

def food(food, next_x, next_y):
    # detect for collision with food
    if(next_x == food.stepx and next_y == food.stepy):
        return True

    return False
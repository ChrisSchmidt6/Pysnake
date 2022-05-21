# python modules
import random
import math

# custom classes
from snake import SnakeSection
from food import Food
from interval import Interval

# variables and methods
import config as cf
import collision

def generate_coords(snake_sections):
    forbidden_coordinates = []
    # put coordinates of all the snake sections in a list
    for section in snake_sections:
        forbidden_coordinates.append([section.stepx, section.stepy])
    # loop through list of forbidden coordinates (it WILL break eventually)
    while True:
        rand_x = math.floor(random.random() * math.floor(cf.canvas_width / cf.step))
        rand_y = math.floor(random.random() * math.floor(cf.canvas_height / cf.step))
        for i in range(len(forbidden_coordinates)):
            f_coord = forbidden_coordinates[i]
            # if randomly generated coordinates are in the forbidden coordinates list
            if(rand_x == f_coord[0] and rand_y == f_coord[1]):
                break

            # end of loop, everything checks out so return coordinates which will also break the while loop
            elif(i == len(forbidden_coordinates) - 1):
                return [rand_x, rand_y]

class Game:
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake = []
        self.food = 0
        self.direction = 0
        self.score = 0
        self.loop = Interval(self.move_snake, cf.game_interval)
        self.can_turn = True
        self.is_paused = True
        self.is_ongoing = False

    def move_snake(self):
        # had to iterate numerically, loop for each section of snake
        for i in reversed(range(len(self.snake))):
            section = self.snake[i]
            # section.stepx, section.stepy = current position
            # section.next_stepx, section.next_stepy = position to move to
            # since we are iterating backwards and higher positions have not been moved:
            # section.higher().next_stepx, section.higher.next_stepy = future position to store
            # move section on canvas to new location
            # initialize next steps but they will be changed
            next_stepx = section.next_stepx
            next_stepy = section.next_stepy
            # if this iteration is for the snake's head
            if(i == 0):
                # check for collision with self or wall, returns true or false
                game_over = collision.hit(self.snake, next_stepx, next_stepy)
                if(game_over):
                    self.end()
                    return 0
                else:
                    # check for collision with food, returns true or false
                    hit_target = collision.food(self.food, next_stepx, next_stepy)
                    if(hit_target):
                        self.score += 1
                        print("Hit target " + str(self.score) + "!")
                        self.add_snake()
                        self.new_food()
                # move snake's head based on direction
                # direction    0 = down, 1 = left, 2 = up, 3 = right
                if(self.direction == 0):
                    next_stepx = next_stepx
                    next_stepy = next_stepy + 1
                elif(self.direction == 1):
                    next_stepx = next_stepx - 1
                    next_stepy = next_stepy
                elif(self.direction == 2):
                    next_stepx = next_stepx
                    next_stepy = next_stepy - 1
                elif(self.direction == 3):
                    next_stepx = next_stepx + 1
                    next_stepy = next_stepy
            else:
                # set next position of snake section to the position of the higher section in section list
                section_ahead = self.snake[section.section_id - 1]
                next_stepx = section_ahead.next_stepx
                next_stepy = section_ahead.next_stepy
            
            # calculate how many pixels to move by
            move_amount_x = (section.next_stepx - section.stepx) * cf.step
            move_amount_y = (section.next_stepy - section.stepy) * cf.step
            self.canvas.move(section.cref, move_amount_x, move_amount_y)
            
            section.move(next_stepx, next_stepy)
        
        # allow player to change direction
        self.can_turn = True

    def change_direction(self, dir):
        self.direction = dir
        # set to false to force at least one movement in new direction
        # which prevents moving in the opposite direction in one loop iteration
        self.can_turn = False
    
    def add_snake(self):
        # get instance of the most recently created snake section
        end_tail = self.snake[len(self.snake) - 1]
        # create new snake section with initial location at end_tail's previous location
        section = SnakeSection(self.canvas, len(self.snake), end_tail.last_stepx, end_tail.last_stepy, end_tail.stepx, end_tail.stepy)
        self.snake.append(section)

    def new_food(self):
        # if food is not default value (will be the case when running self.setup())
        if(self.food != 0):
            # delete food object on canvas and from game object
            self.canvas.delete(self.food.cref)
            del self.food
        # get valid coordinates the new food instance can spawn at, returns [x, y]
        coords = generate_coords(self.snake)
        self.food = Food(self.canvas, coords[0], coords[1])

    def setup(self):
        # create first three sections of snake
        snake_head = SnakeSection(self.canvas, 0, cf.starting_stepx, cf.starting_stepy, cf.starting_stepx, cf.starting_stepy + 1, "head", cf.snake_head_color)
        first_section = SnakeSection(self.canvas, 1, snake_head.stepx, snake_head.stepy - 1, snake_head.stepx, snake_head.stepy)
        second_section = SnakeSection(self.canvas, 2, first_section.stepx, first_section.stepy - 1, first_section.stepx, first_section.stepy)
        # add current registry to self.snake
        self.snake += [snake_head, first_section, second_section]
        # create food
        self.new_food()
    
    def reset(self):
        # delete all snake instances from canvas
        for section in self.snake:
            self.canvas.delete(section.cref)
        # delete food object from game object
        self.canvas.delete(self.food.cref)
        self.snake = []
        self.food = 0
        self.direction = 0
        self.score = 0
        self.loop = Interval(self.move_snake, cf.game_interval)
        self.is_ongoing = False

    def clear_loop(self):
        self.loop.end()
        del self.loop
        self.is_paused = True
    
    def pause(self):
        if(not self.is_paused):
            print("Pausing game ...")
            self.clear_loop()
            self.loop = Interval(self.move_snake, cf.game_interval)

    def start(self):
        print("Starting game ...")
        self.loop.start()
        self.is_paused = False
        self.is_ongoing = True

    def end(self):
        print("Ending game ...")
        self.clear_loop()
        self.is_ongoing = False
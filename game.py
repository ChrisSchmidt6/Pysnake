# custom classes
from engine import Game

def handle_key_press(e):
    if(e.keysym == "s" or e.keysym == "Down"):
        # if direction is not Up
        if(game.direction != 2 and game.can_turn):
            game.change_direction(0)
    elif(e.keysym == "a" or e.keysym == "Left"):
        # if direction is not Right
        if(game.direction != 3 and game.can_turn):
            game.change_direction(1)
    elif(e.keysym == "w" or e.keysym == "Up"):
        # if direction is not Down
        if(game.direction != 0 and game.can_turn):
            game.change_direction(2)
    elif(e.keysym == "d" or e.keysym == "Right"):
        # if direction is not Left
        if(game.direction != 1 and game.can_turn):
            game.change_direction(3)
    elif(e.keysym == "BackSpace"):
        if(not game.is_paused):
            game.pause()
    elif(e.keysym == "space"):
        if(game.is_paused):
            if(game.is_ongoing):
                game.start()
            else:
                game.reset()
                game.setup()
                game.start()

def start_game(canvas):
    global game
    game = Game(canvas)

    game.setup()
    game.start()
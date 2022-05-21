# python modules
import tkinter as tk

# custom classes
import config as cf
from game import start_game, handle_key_press

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

def main():
    root = tk.Tk()
    my_app = App(root)

    # window settings
    my_app.master.title("Pysnake")
    my_app.master.maxsize(cf.canvas_width, cf.canvas_height)
    my_app.master.minsize(cf.canvas_width, cf.canvas_height)
    # size of root object which will contain the canvas
    root.geometry(str(cf.canvas_width) + "x" + str(cf.canvas_height))
    # initialize canvas
    my_canvas = tk.Canvas(root, width=cf.canvas_width, height=cf.canvas_height, bg=cf.canvas_background)
    my_canvas.pack()
    # call method when pressing key
    root.bind("<KeyPress>", handle_key_press)
    # start game
    start_game(my_canvas)
    # start the program
    my_app.mainloop()

if(__name__ == "__main__"):
    main()
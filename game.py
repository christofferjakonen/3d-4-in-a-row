import tkinter as tk
from board import Board
from graphical import Application
from random import choice


class Game:
    def __init__(self):
        self.player = choice([1, 2])
        self.board = Board()

        # Create game window
        root = tk.Tk()
        root.geometry("600x600")
        window = Application(master=root)
        window.mainloop()


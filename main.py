#from game import Game
import tkinter as tk
from graphical import Application


def main():
    #Game()
    root = tk.Tk()
    root.geometry("600x600")
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()

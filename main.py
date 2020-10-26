#from game import Game
import tkinter as tk
from graphical import Application


def main():
    #Game()
    root = tk.Tk()
    root.geometry("560x610+100+100")
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()

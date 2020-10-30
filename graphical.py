# i don't usually import everything, but i think it's ok for tkinter
from tkinter import *
from board import Board


class Application(Frame):
    # create main window
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("4x4x4")
        self.grid(row=0, column=0, sticky=(N, S, E, W))
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.main_buttons = []
        self.board = Board()
        self.player = 1
        self.game_going = 1
        # create everything in the window
        self.create_widgets()

    def create_widgets(self):
        # define a pixel, because otherwise labels use textsize when you set their size
        self.pixelV = PhotoImage(width=1, height=1)
        # create the main frames in the window
        self.main_box = Frame(self, height=400, width=400, bg="#EEFFEE", relief=RAISED, borderwidth=3)
        self.chat_box = Frame(self, height=200, width=400, bg="#F0F0F0", relief=RAISED, borderwidth=3)
        self.overview_box = Frame(self, height=600, width=200, bg="#EEFFEE", relief=RAISED, borderwidth=3)
        # create things in the main frames
        self.chat_text_turn = StringVar()
        self.chat_text_message = StringVar()
        self.turn = Label(self.chat_box, textvariable=self.chat_text_turn)
        self.message = Label(self.chat_box, textvariable=self.chat_text_message)
        self.restart_button = Button(self.chat_box, text="Restart", command=self.restart)
        self.chat_text_turn.set("It's blues turn")
        self.chat_text_message.set("")
        # align everything inside the window
        self.main_box.grid(row=0, column=0, sticky=NSEW, padx=1, pady=1)
        self.chat_box.grid(row=1, column=0, sticky=NSEW, padx=1, pady=1)
        self.chat_box.grid_columnconfigure(0, weight=0)
        self.chat_box.grid_columnconfigure(1, weight=1)
        self.chat_box.grid_rowconfigure(2, weight=1)
        self.turn.grid(row=0, column=0, sticky=W)
        self.message.grid(row=1, column=0, sticky=W)
        self.restart_button.grid(row=2, column=0, sticky=SW, padx=5, pady=5)
        self.overview_box.grid(row=0, column=1, sticky=NSEW, rowspan=2)
        # create the 4x4 button grid
        self.create_button_grid()
        self.create_overview_layers()

    def create_button_grid(self):
        for b in range(16):
            button = Button(self.main_box, image=self.pixelV, width=98, height=98, compound="c", bg="#FFFFFF", activebackground="#EEEEEE", relief=RAISED, borderwidth=1)
            button.grid(row=b//4, column=b%4, padx=1, pady=1)
            button._name = b
            button.bind("<Button-1>", self.schmove)
            self.main_buttons.append(button)

    def schmove(self, event):
        if self.game_going:
            if self.board.place_peg(event.widget._name//4, event.widget._name%4, self.player):
                self.chat_text_message.set("")
                if self.board.top_color(event.widget._name//4, event.widget._name%4) == 1:
                    button = event.widget
                    button.config(bg="#CCCCFF")
                elif self.board.top_color(event.widget._name//4, event.widget._name%4) == 2:
                    button = event.widget
                    button.config(bg="#FFCCCC")
                self.update_overview_layers()
                self.win(self.board.check_for_win())
                if self.game_going:
                    self.switch_player()
            else:
                self.chat_text_message.set("Peg is full, pick another")

    def switch_player(self):
        if self.player == 1:
            self.chat_text_turn.set("It's reds turn")
            self.player = 2
        elif self.player == 2:
            self.chat_text_turn.set("It's blues turn")
            self.player = 1

    def restart(self):
        self.create_widgets()
        self.main_buttons = []
        self.board = Board()
        self.player = 1
        self.game_going = True

    def create_overview_layers(self):
        self.change_overview_button = Button(self.chat_box, text="Change to\n3d overview", command=self.create_overview_3d)
        self.change_overview_button.grid(row=2, column=1, sticky=SE, padx=5, pady=5)
        self.overviewlayers = []
        for i in range(4):
            layer = Frame(self.overview_box, width=120, height=120, relief=SUNKEN)
            layer.grid(row=8-(i*2+1), column=0, padx=5, pady=5)
            layername = Label(self.overview_box, text=f"Layer {int(4-i)}:", bg="#EEFFEE")
            layername.grid(row=i*2, column=0, sticky=W)
            for xy in range(16):
                color = LabelFrame(layer, width=30, height=30, bg="#FFFFFF")
                color.grid(row=xy//4, column=xy%4)
            self.overviewlayers.append(layer)

    def update_overview_layers(self):
        for i in range(4):
            self.overviewlayers[i].destroy()
        self.overviewlayers = []
        for i in range(4):
            layer = Frame(self.overview_box, width=120, height=120, relief=SUNKEN)
            layer.grid(row=8-(i*2+1), column=0, padx=5, pady=5)
            for xy in range(16):
                if self.board.layers[i].coordinates[xy//4][xy%4]:
                    bgcolor = "#CCCCFF" if self.board.layers[i].coordinates[xy//4][xy%4] == 1 else "#FFCCCC"
                    color = LabelFrame(layer, width=30, height=30, bg=bgcolor)
                else:
                    color = LabelFrame(layer, width=30, height=30, bg="#FFFFFF")
                color.grid(row=xy // 4, column=xy % 4)
            self.overviewlayers.append(layer)



    def create_overview_3d(self):
        # todo figure out some way to make a 3d model
        # self.change_overview_button = Button(self.chat_box, text="Change to\n3d overview", command=self.create_overview_3d)
        pass

    def win(self, player):
        if player:
            self.game_going = False
            self.chat_text_turn.set("")
            self.chat_text_message.set(f"Player {player} wins!")
            #  for reference, my friend told me to use this when i asked for a placeholder
            """print("Woah...\n"
                  f"Nice cock player {player}\n"
                  "Thick but not too flaccid\n"
                  "Perfect length\n"
                  "A nice 80 degree angle\n"
                  "Could trim the hair a bit but we'll work on it\n"
                  "Yep...\n"
                  "I'd say that's a pretty good cock\n"
                  "I rate it... 8.5/10\n"
                  f"Good job player {player}")"""

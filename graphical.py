from tkinter import *
from board import Board


class Application(Frame):
    # create main window
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("four")
        self.grid(row=0, column=0, sticky=(N, S, E, W))
        self.main_buttons = []
        self.board = Board()
        self.player = 1
        # create everything in the window
        self.create_widgets()

    def create_widgets(self):
        self.pixelV = PhotoImage(width=1, height=1)
        self.main_box = Frame(self, height=400, width=400, bg="#EEFFEE", relief=RAISED, borderwidth=3)
        self.chat_box = Frame(self, height=200, width=400, bg="#F0F0F0", relief=RAISED, borderwidth=3)
        self.overview_box = Frame(self, height=600, width=200, bg="#EEFFEE", relief=RAISED, borderwidth=3)

        self.chat_text_turn = StringVar()
        self.chat_text_message = StringVar()
        self.turn = Label(self.chat_box, textvariable=self.chat_text_turn)
        self.message = Label(self.chat_box, textvariable=self.chat_text_message)
        self.chat_text_turn.set("It's blues turn")
        self.chat_text_message.set("")

        self.main_box.grid(row=0, column=0, sticky=NSEW, padx=1, pady=1)
        self.chat_box.grid(row=1, column=0, sticky=NSEW)
        self.turn.grid(row=0, column=0, sticky=W)
        self.message.grid(row=1, column=0, sticky=W)
        self.overview_box.grid(row=0, column=1, sticky=NSEW, rowspan=2)

        self.make_button_grid()

    def make_button_grid(self):
        for b in range(16):
            button = Button(self.main_box, image=self.pixelV, width=98, height=98, compound="c", bg="#FFFFFF", activebackground="#EEEEEE", relief=RAISED, borderwidth=1)
            button.grid(row=b//4, column=b%4, padx=1, pady=1)
            button._name = b
            button.bind("<Button-1>", self.schmove)
            self.main_buttons.append(button)

    def schmove(self, event):
        if self.board.place_peg(event.widget._name%4, event.widget._name//4, self.player):
            self.chat_text_message.set("")
            if self.board.top_color(event.widget._name%4, event.widget._name//4) == 1:
                button = event.widget
                button.config(bg="#DDDDFF")
            elif self.board.top_color(event.widget._name%4, event.widget._name//4) == 2:
                button = event.widget
                button.config(bg="#FFDDDD")

            self.win(self.board.check_for_win())
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

    def win(self, player):
        if player:
            print("Woah...\n"
                  f"Nice cock player {player}\n"
                  "Thick but not too flaccid\n"
                  "Perfect lengh\n"
                  "A nice 80 degree angle\n"
                  "Could trim the hair a bit but we'll work on it\n"
                  "Yep...\n"
                  "I'd say that's a pretty good cock\n"
                  "I rate it... 8.5/10\n"
                  f"Good job player {player}")

    def test_print(self):
        print("test")

from tkinter import *
from tkinter import simpledialog
import random

def next_turn(row , column):
    global player 

    if buttons[row][column]['text'] ==  "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]  + ' turn'))

            elif check_winner() is True:
                label.config(text=(players[0]  + " wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+ ' turn'))

            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True

    elif empty_spaces() is False:
        return "Tie"

    else:
        return False

def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def get_player_symbols():
    # Ask Player 1 for their symbol
    p1 = simpledialog.askstring("Player 1", "Enter symbol for Player 1:", initialvalue="X")
    if not p1: 
        p1 = "X"
    
    # Ask Player 2 and check that it's not identical to Player 1
    p2 = simpledialog.askstring("Player 2", f"Enter symbol for Player 2 (cannot be '{p1}'):", initialvalue="O")
    while not p2 or p2 == p1:
        p2 = simpledialog.askstring("Player 2", f"Symbol taken or empty! Enter a different symbol for Player 2:", initialvalue="O")
        if not p2: 
            p2 = "O"
            
    return [p1, p2]

def new_game():
    global player, players
    players = get_player_symbols()
    player = random.choice(players)
    
    label.config(text=(player + " turn"))

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

window = Tk()
window.title("X and O")

# Prompt for custom symbols at startup
players = get_player_symbols()
player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]] 

label = Label(text=(player + " turn"), font=("Arial", 20))
label.pack(side="top")

reset_button = Button(text="restart", font=('Arial', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("Arial", 40), width=5, height=2, 
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()

from tkinter import *
from tkinter import StringVar, ACTIVE, NORMAL, DISABLED
import random
import numpy as np
import time as tm

time = 500
score = 0
game_sequence = []
player_sequence = []

game_font1 = ('Arial', 12)
game_font2 = ('Arial', 8)


def update_score():
    global score
    add = 1 / time * 1000
    add2 = score + add
    score = add2 + score / add
    score = round(score)
    score_label.config(text="Score: " + str(score))


def pick_sequence():
    disable()
    while True:
        value = random.randint(1, 4)
        if len(game_sequence) == 0:
            game_sequence.append(value)
            print(game_sequence)
            break
        elif value != game_sequence[-1]:
            game_sequence.append(value)
            print(game_sequence)
            break

    play_sequence()


def play_sequence():
    change_label("Playing", 'disabled')
    delay = 0
    for value in game_sequence:
        if value == 1:
            root.after(delay, lambda: animate(white_button))
            print('white')
        elif value == 2:
            root.after(delay, lambda: animate(magenta_button))
            print('magenta')
        elif value == 3:
            root.after(delay, lambda: animate(cyan_button))
            print('cyan')
        elif value == 4:
            root.after(delay, lambda: animate(yellow_button))
            print('yellow')
        delay += time
    white_button.config(state='normal')
    magenta_button.config(state='normal')
    cyan_button.config(state='normal')
    yellow_button.config(state='normal')


def animate(button):
    button.config(state=ACTIVE)
    root.after(time, lambda: button.config(state=NORMAL))


def change_label(message, state1):
    start_button.config(text=message, state=state1)


def set_difficulty():
    """Use radio buttons to set difficulty"""
    global time
    if difficulty.get() == "Easy":
        time = 1000
    elif difficulty.get() == "Medium":
        time = 500
    else:
        time = 200


def press(value):
    """Simulate pressing a button for the player"""
    # Add the players press to the players sequence
    player_sequence.append(value)
    # If the current "round" is over, check to see if the player entered the correct sequence of button presses
    if len(player_sequence) == len(game_sequence):
        disable()
        check_round()


def check_round():
    if len(player_sequence) == sum([1 for i, j in zip(player_sequence, game_sequence) if i == j]):
        print("good")
        update_score()
        player_sequence.clear()
        tm.sleep(0.5)
        pick_sequence()
    else:
        print('Fail')
        change_label('New Game', 'normal')


def disable():
    white_button.config(state='disabled')
    magenta_button.config(state='disabled')
    cyan_button.config(state='disabled')
    yellow_button.config(state='disabled')


def enable():
    game_sequence.clear()
    player_sequence.clear()
    global score
    score = 0
    score_label.config(text='Score: ' + str(score))
    pick_sequence()


root = Tk()
root.title("")
root.geometry("400x400")
root_color = 'lightblue'
root.config(bg=root_color)
game_color = 'white'
white = '#F1F1E8'
white_button_light = '#FFFFFF'
magenta = '#BA00AE'
magenta_button_light = '#FF00EF'
cyan = '#389E90'
cyan_button_light = '#00FFDE'
yellow = '#B7BC31'
yellow_button_light = '#F7FF00'

info_frame = Frame(root)
info_frame.pack()

game_frame = Frame(root, bg=game_color)
game_frame.pack()

start_button = Button(info_frame, text="New Game", font=game_font1, bg=game_color, command=enable)
start_button.grid(row=0, column=0)

score_label = Label(info_frame, text='Score: ' + str(score), font=game_font1, bg=root_color)
score_label.grid(row=0, column=1)

white_button = Button(game_frame, bg=white, activebackground=white_button_light, borderwidth=3, state=DISABLED,
                      command=lambda: press(1))

white_button.grid(row=0, column=0, columnspan=2, padx=20, pady=20, ipadx=60, ipady=50)

magenta_button = Button(game_frame, bg=magenta, activebackground=magenta_button_light, borderwidth=3, state=DISABLED,
                        command=lambda: press(2))

magenta_button.grid(row=0, column=2, columnspan=2, padx=20, pady=20, ipadx=60, ipady=50)

cyan_button = Button(game_frame, bg=cyan, activebackground=cyan_button_light, borderwidth=3, state=DISABLED,
                     command=lambda: press(3))

cyan_button.grid(row=1, column=0, columnspan=2, padx=20, pady=10, ipadx=60, ipady=50)

yellow_button = Button(game_frame, bg=yellow, activebackground=yellow_button_light, borderwidth=3, state=DISABLED,
                       command=lambda: press(4))

yellow_button.grid(row=1, column=2, columnspan=2, padx=20, pady=10, ipadx=60, ipady=50)

difficulty = StringVar()
difficulty.set("Medium")
Label(game_frame, text="Difficulty", font=game_font2, bg=game_color).grid(row=2, column=0)

Radiobutton(game_frame, text="Easy", variable=difficulty, value="Easy", font=game_font2, bg=game_color,
            command=set_difficulty).grid(row=2, column=1)

Radiobutton(game_frame, text="Medium", variable=difficulty, value="Medium", font=game_font2, bg=game_color,
            command=set_difficulty).grid(row=2, column=2)

Radiobutton(game_frame, text="Hard", variable=difficulty, value="Hard", font=game_font2, bg=game_color,
            command=set_difficulty).grid(row=2, column=3)

root.mainloop()
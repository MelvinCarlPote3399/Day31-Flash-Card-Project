# Import statements/pre-directives
from tkinter import *
import pandas
import random

# Default code provided
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ------ Button functionality ------ #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    # print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=background)
    flip_timer = window.after(3000, func=flip_card)


# Flipping the cards
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


# Implementing functionality, where words that the user knows (through clicking the checkmark) will not be repeated;
# List will be reduced in size as a result
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)  # words that have yet to be learned are saved here
    next_card()


# Setting up the window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# -----Image set up; background and text ----- #
canvas = Canvas(width=900, height=585, bg=BACKGROUND_COLOR, highlightthickness=0)
background = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(450, 300, image=background)
card_title = canvas.create_text(450, 150, text="", font=("Ariel", 35, "italic"))
card_word = canvas.create_text(450, 285, text="", font=("Ariel", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# X [marks the spot] and checkmark button
x = PhotoImage(file="images/wrong.png")
x_button = Button(window, image=x, borderwidth=0, highlightthickness=0, command=next_card)
x_button.grid(column=0, row=1)

checkmark = PhotoImage(file="images/right.png")
checkmark_button = Button(window, image=checkmark, borderwidth=0, highlightthickness=0, command=is_known)
checkmark_button.grid(column=1, row=1, columnspan=1)

# Card with French words is generated on start
next_card()

window.mainloop()

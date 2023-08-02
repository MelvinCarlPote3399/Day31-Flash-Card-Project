# Import statements/pre-directives
from tkinter import *
from turtle import *

# Default code provided
BACKGROUND_COLOR = "#B1DDC6"

# Setting up the window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# -----Image set up; background and text ----- #
canvas = Canvas(width=900, height=585, bg=BACKGROUND_COLOR, highlightthickness=0)
background = PhotoImage(file="images/card_front.png")
canvas.create_image(450, 300, image=background)
french_start_text = canvas.create_text(450, 150, text="French", font=("Ariel", 35, "italic"))
french_word_start = canvas.create_text(450, 285, text="trouve", font=("Ariel", 50, "bold"))
canvas.grid(column=1, row=0, columnspan=1)

# X [marks the spot] and checkmark button
x = PhotoImage(file="images/wrong.png")
x_button = Button(window, image=x, borderwidth=0)
x_button.grid(column=0, row=1, columnspan=2)

window.mainloop()

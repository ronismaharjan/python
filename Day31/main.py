from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
# ------------------------Functions/Commands--------------
french_word = {}


def next_card():
    with open("Day31/french_words.csv", mode="r") as french_words_csv:
        csv_data = pandas.read_csv(french_words_csv)
        dict_data = csv_data.to_dict(orient="records")
        global french_word
        global timer
        window.after_cancel(timer)
        french_word = random.choice(dict_data)
        card_canvas.itemconfig(card_title, text="French")
        card_canvas.itemconfig(card_word, text=french_word["French"])
        card_canvas.itemconfig(card, image=fcard_path)
        timer = window.after(3000, func=flip_card)


def flip_card():
    global french_word
    print(french_word)
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(
        card_word, text=french_word["English"], fill="white")
    card_canvas.itemconfig(card, image=bcard_path)


# ----------------------UI Section------------------------
# Window code
window = Tk()
window.title("Flashy")
# window.minsize(height=650, width=800)
window.config(bg=BACKGROUND_COLOR, padx=30, pady=30)
timer = window.after(3000, func=flip_card)

# Codes for Card
card_canvas = Canvas(width=800, height=526)
card_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.grid(column=0, row=0, columnspan=2)
bcard_path = PhotoImage(file="Day31/images/card_back.png")
fcard_path = PhotoImage(file="Day31/images/card_front.png")
card = card_canvas.create_image(400, 263, image=fcard_path)

card_title = card_canvas.create_text(
    400, 100, text="Title", font=("Arial", 48, "bold"))
card_word = card_canvas.create_text(
    400, 263, text="Word", font=("Arial", 69, "bold"))

# Codes for Buttons
# Right Button
right_image = PhotoImage(file="Day31/images/right.png")
right_button = Button(
    image=right_image, bg=BACKGROUND_COLOR)
right_button.config(command=next_card)
right_button.grid(row=1, column=1)

# Cross Button
cross_image = PhotoImage(file="Day31/images/wrong.png")
known_button = Button(
    image=cross_image, bg=BACKGROUND_COLOR)
known_button.grid(row=1, column=0, )


window.mainloop()

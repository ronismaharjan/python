import tkinter

# Functions for the button when click


def replace_banner():
    user_text = user_texts.get()
    if user_text != "":
        banner.config(text=user_text)


# Creating the window
window = tkinter.Tk()
window.minsize(width=600, height=500)

# Creating a label in the window
banner = tkinter.Label()
banner.config(text="your banner", font=("sanserif", 12, "bold"))
banner.grid(column=1, row=0)

# Creating a input section in screen
user_texts = tkinter.Entry()
user_texts.config(text="email")
user_texts.grid(column=4, row=3)

# Creating a button
button = tkinter.Button()
button.config(text="cilck", command=replace_banner, pady=20, padx=10)
button.grid(column=2, row=1)

# Creating second button
button = tkinter.Button()
button.config(text="cilck", command=replace_banner)
button.grid(column=3, row=0)

window.mainloop()

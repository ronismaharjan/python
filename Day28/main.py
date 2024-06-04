from tkinter import *
import math
# -------------------Constants-----------------------------------#
PINK = "#E2979C"
RED = "#E7305B"
GREEN = "#9BDEAC"
YELLOW = "#F7F5DD"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
mark = "✔"
timer = None
timer_started = False

# --------------------Timer logics---------------------------------#
# Function to start the timer


def start_timer():
    global rep
    rep += 1
    global timer_started

    converted_worktime_sec = 60 * WORK_MIN
    converted_shortbreak_sec = 60 * SHORT_BREAK_MIN
    converted_longbreak_sec = 60 * LONG_BREAK_MIN
    if not timer_started:
        timer_started = True
        if rep % 8 == 0:
            count_down(converted_longbreak_sec)
            task_label.config(text="Long Break", fg=GREEN,
                              font=(FONT_NAME, 20, "bold"))

        elif rep % 2 == 0:
            count_down(converted_shortbreak_sec)
            task_label.config(text="Short Break", fg=PINK,
                              font=(FONT_NAME, 20, "bold"))

        else:
            count_down(converted_worktime_sec)
            task_label.config(text="Work Time", fg=RED,
                              font=(FONT_NAME, 20, "bold"))


# Function of countdown logic


def count_down(count):

    minute = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        canvas.itemconfig(timer_text, text=f"{minute}:0{sec}")
    else:
        canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:

        if rep < 8:
            if rep % 2 != 0:
                global mark
                completed_task_label.config(
                    text=mark, fg=RED, font=(FONT_NAME, 10, "bold"), bg="black")
                mark += "✔"
            global timer_started
            timer_started = False
            start_timer()


# ---------------------Clear Button Logic-------------------------#


def reset():
    window.after_cancel(timer)
    task_label.config(text="Timer", font=(FONT_NAME, 23, "bold"), fg="#5e61fe")
    canvas.itemconfig(timer_text, text="00:00")
    completed_task_label["text"] = ""
    global rep
    rep = 0
    global timer_started
    timer_started = False


# ---------------------UI Setup-----------------------------------#
# Creating a window
window = Tk()
window.title("pomodora")
window.minsize(width=300, height=300)
# window.maxsize(width=300, height=300)
window.config(padx=20, pady=30, bg="black")

# Creating label for what its time
task_label = Label()
task_label.config(text="Timer", font=(
    FONT_NAME, 23, "bold"), bg="black", fg="#5e61fe")
task_label.grid(row=0, column=1)

# Creating Canvas
canvas = Canvas(width=201, height=224, bg="black", highlightthickness=0)
tomato_img = PhotoImage(file="Day28/python.png")
canvas.create_image(101, 110, image=tomato_img)
timer_text = canvas.create_text(101, 110, text="00:00", font=(
    FONT_NAME, 25, "bold"), fill="whitesmoke")
canvas.grid(row=1, column=1)

# Creating Start button
start_button = Button()
start_button.config(text="Start", command=start_timer,
                    bg=YELLOW, fg="black", font=(FONT_NAME, 10, "bold"))
start_button.grid(row=2, column=0)

# Creating the checkmark label
completed_task_label = Label(bg="black")
completed_task_label.grid(row=3, column=1)

# Creating Reset button
reset_button = Button()
reset_button.config(text="Reset", command=reset,
                    bg=YELLOW, fg="black", font=(FONT_NAME, 10, "bold"))
reset_button.grid(row=2, column=2)

window.mainloop()

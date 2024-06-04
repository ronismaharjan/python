import tkinter
# Function to convert miles to Km


def convert():
    miles = int(user_input_field.get())
    if type(miles) == int:
        km = round(miles * 1.60934)
        output_label.config(text=str(km))


# Creating a window
window = tkinter.Tk()
window.minsize(width=300, height=20)
window.config(padx=20, pady=20)

# Creating a user input field
user_input_field = tkinter.Entry()
user_input_field.grid(column=1, row=0)

# Input label
input_label = tkinter.Label()
input_label.config(text="Miles", font=("bold"))
input_label.grid(column=2, row=0)

# creating label for result in km
result_label = tkinter.Label()
result_label.config(text="is equal to")
result_label.grid(column=0, row=1)

# Creating output label
output_label = tkinter.Label(text="0")
output_label.grid(column=1, row=1)
format_label = tkinter.Label(text="Km")
format_label.grid(column=2, row=1)

# Creating the calculate button
calculate_button = tkinter.Button()
calculate_button.config(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

# Creating a clear button
clear_button = tkinter.Button()
clear_button.config(text="Clear")
clear_button.grid(column=2, row=2)


window.mainloop()

# @password generator gui made by ronish
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------Password Generator---------------------
character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '@', '$', "^", "&", "*", "(", ")", "+"]


def generate_password():
    random_letter_list = [random.choice(character) for _ in range(0, 4)]
    random_number_list = [random.choice(numbers) for _ in range(0, 3)]
    random_symbol_list = [random.choice(symbols) for _ in range(0, 3)]
    password_list = random_letter_list + random_number_list + random_symbol_list

    random.shuffle(password_list)

    password_in_txt = "".join(password_list)

    if password_entry.get() != "":
        password_entry.delete(0, END)
        password_entry.insert(END, password_in_txt)
    else:
        password_entry.insert(END, password_in_txt)
    pyperclip.copy(password_entry.get())


# ---------------------Save Password in file------------------

def save_file():

    website_name = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    data_dict = {
        website_name: {
            "Email/Username": email,
            "Password": password, },
    }
    if website_name == "" or email == "" or password == "":
        messagebox.askretrycancel(title="Oops", message="The field is empty")

    else:
        try:
            with open("Day29/password.json", mode="r") as data_file:
                password_data = json.load(data_file)
        except FileNotFoundError:
            with open("Day29/password.json", mode="w") as data_file:
                json.dump(data_dict, data_file, indent=4)
        else:
            with open("Day29/password.json", mode="w") as data_file:
                if website_name in password_data:
                    want_to_overwrite = messagebox.askyesno(
                        title="Already Exist", message=f"There already exist data with {website_name}.\nDo you want to overwrite?")
                    if want_to_overwrite:
                        password_data.update(data_dict)
                        json.dump(password_data, data_file, indent=4)
                    else:
                        json.dump(password_data, data_file, indent=4)
                else:
                    password_data.update(data_dict)
                    json.dump(password_data, data_file, indent=4)
        finally:
            data_file.close()
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


# -----------------------Search Website Logics------------------------------------


def search():
    website_entered = website_entry.get()
    try:
        with open("Day29/password.json", mode="r") as password_json:
            json_data = json.load(password_json)
            keys = [key for key in json_data]
            if website_entered in keys:
                website_details = f'Email: {json_data[website_entered]["Email/Username"]}\nPassword: {json_data[website_entered]["Password"]}'
                messagebox.showinfo(title="Details", message=website_details)
            else:
                messagebox.showinfo(
                    title="Details", message="No Details available")
        password_json.close()

    except FileNotFoundError:
        messagebox.showinfo(
            title="Details", message="No Datafile found")


# -------------------UI Setup------------------------------------------
# -----------------Window Section UI----------------
# Creating Window
window = Tk()
window.config(padx=20, pady=20)

# ------------------Canvas Section UI--------------------

# Creating a canvas for the image
image_canvas = Canvas(width=200, height=200)
image_path = PhotoImage(file="Day29/logo.png")
image_canvas.create_image((90, 100), image=image_path)
image_canvas.grid(row=0, column=1)

# ----------------Website part UI-------------------
# Label for website
website_label = Label()
website_label.config(text="Website:")
website_label.grid(row=1, column=0)

# Entry for website
website_entry = Entry()
website_entry.focus()
website_entry.config(width=30)
website_entry.grid(row=1, column=1)

# --------------------Username/Email part UI-----------------
# Label for username / email
username_label = Label()
username_label.config(text="Email/Username:")
username_label.grid(row=2, column=0)

# Entry for username/email
username_entry = Entry()
username_entry.config(width=30)
username_entry.grid(row=2, column=1)

# ------------------Password Part UI------------------------
# Creating label for password
password_label = Label()
password_label.config(text="Password:")
password_label.grid(row=3, column=0)

# Entry for password_label
password_entry = Entry()
password_entry.config(width=30)
password_entry.grid(row=3, column=1)

# Generate passsword button
generate_password_button = Button()
generate_password_button.config(
    text="Generate", command=generate_password, width=10)
generate_password_button.grid(row=3, column=2)

# ---------------Add part UI------------------------------------------
add_button = Button()
add_button.config(text="Add", width=36, command=save_file)
add_button.grid(row=4, column=1, columnspan=2)

# ------------------Search Button UI-------------------------------------
search_button = Button()
search_button.config(text="Search", width=10, command=search)
search_button.grid(row=1, column=2)


window.mainloop()

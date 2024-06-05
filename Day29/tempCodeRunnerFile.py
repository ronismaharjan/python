
# Creating a canvas for the image
image_canvas = Canvas(width=200, height=200)
image_path = PhotoImage(file="Day29/logo.png")
image_canvas.create_image((100, 100), image=image_path)
image_canvas.grid(row=0, column=1)

# ----------------Website part UI-------------------
# Label for website
website_label = Label()
website_label.config(text="Website:")
website_label.grid(row=1, column=0)

# Entry for website
website_entry = Entry()
website_entry.config(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

# --------------------Username/Email part UI-----------------
# Label for username / email
username_label = Label()
username_label.config(text="Email/Username:")
username_label.grid(row=2, column=0)

# Entry for username/email
username_entry = Entry()
username_entry.config(width=35)
username_entry.grid(row=2, column=1, columnspan=2)

# ------------------Password Part UI------------------------
# Creating label for password
password_label = Label()
password_label.config(text="Password:")
password_label.grid(row=3, column=0)

# Entry for password_label
password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(row=3, column=1)

# Generate passsword button
generate_password_button = Button()
generate_password_button.config(text="Generate")
generate_password_button.grid(row=3, column=2)

# ---------------Add part UI------------------------------------------
add_button = Button()
add_button.config(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)
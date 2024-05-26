# Getting all the name that we have to send letter
with open("Day24/Input/Names/invited_names.txt") as name_file:
    # Creating a list of name from the names variable so that we can iterate each name
    name_list = name_file.readlines()

# Getting the blueprint of letter and storing it in a variable
with open("Day24/Input/Letters/starting_letter.txt") as letter:
    letter_style = letter.read()


# Iterationg over each name
for name in name_list:
    clean_name = name.strip()
    path = f"Day24/Output/ReadyToSend/letter_for_{clean_name}.txt"
    new_letter = letter_style.replace("[name]", clean_name)

    # Writing and creating a new file with the name on the bluepring
    with open(path, mode="w") as letter:
        letter.write(new_letter)

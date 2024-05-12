def format_name(f_name, l_name):
    formated_name = ""
    formated_name += f_name.title()
    formated_name += " "
    formated_name += l_name.title()
    return formated_name

name = format_name("ronish", "maharjan")
print(name)
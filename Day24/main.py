import os
# We will be learning to read and write the file using python in this day

# We use "open()" function to open the file

# file = open(r"C:\Users\Home\Desktop\python\Day24\my_file.txt")

# contents = file.read()
# print(contents)
# file.close()

# or we can use other way to open
# with open("Day24\my_file.txt", mode="r") as file:
#     contents = file.read()
#     print(contents)
#     file.close()

# How to write in the file we use mode = "w or a" w will delete all the file where as a will not delete the before data

# contents_by_user = input("> ")
# with open("Day24/my_file.txt", mode="a") as file:
#     file.write("\n" + contents_by_user)


# with open("Day24\my_file.txt", mode="r") as file:
#     contents = file.read()
#     print(contents)
#     file.close()
os.system("cls")
with open("./high_score.txt", mode="r") as data:
    high_score = int(data.read())


new_high_score = int(input("> "))

if new_high_score > high_score:
    with open("./high_score.txt", mode="w") as score:
        score.write(str(new_high_score))
print(high_score)

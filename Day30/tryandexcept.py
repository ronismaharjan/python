# Types of Error in python

# KeyError: This error occur when there is no given key in the dictionary

# TypeError: This error occur when we add or do other operation with different data types like string+float

# IndexError: This error occurs when there is no given key in the list.


# try:
#     file = open("hello")
#     print(hell[0])
# except FileNotFoundError as error_message:
#     print(error_message)
# except KeyError:
#     print("keyerror")


# fruits = ["Apple", "Pear", "Orange"]


# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + "pie")


# try:
#     make_pie(4)
# except IndexError as error_message:
#     print(error_message)

# finally:
#     for _ in range(len(fruits)):
#         make_pie(_)

facebook_post = [
    {"Likes": 2, "comment": 3, },
    {"Likes": 2, "comment": 3, },
    {"Likes": 2, "comment": 3, },
    {"comment": 3, },
    {"comment": 3, },
    {"Likes": 2, "comment": 3, }

]
total_likes = 0
for x in facebook_post:
    try:
        total_likes += x["Likes"]
    except KeyError:
        pass


print(total_likes)

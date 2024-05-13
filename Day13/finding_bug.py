#Bugs and fix them 

#First Bug Fixed
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("you got it")
# my_function()

#Second Bug Fixed
# from random import randint
# dice_img = ["1", '3', "2", "4", "5","6"]
# dice_num = randint(0, 5)
# print(dice_img[dice_num])

#Third Bug Fixed
# year = int(input("What's your year of birth: "))
# if year > 1980 and year <= 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")

#Fourth Bug Fixed
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive ate age {age}")

#Fifth Bug Fixed
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#Sixth Bug Fixed
def mutate(a_list):
    b_list =[]
    for item in a_list:
        new_item = item*2
        b_list.append(new_item)
    print(b_list)

mutate([1,2, 3, 5, 8, 13])
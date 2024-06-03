# number = [new_item for item in list] this is the way to create a list using list comprehension

# number = [1, 2, 3]
# new_number = [item +1 for item in number]
# print(new_number)
# names = ['ronish', 'ram', 'shyam']
# number = [name for name in names if len(name) <= 4 ]
# print(number)

# Exercise 1
# numbers = [1, 1, 2, 3, 5, 8,21, 34, 55]
# squared_number = [num * num for num in numbers]
# print(squared_number)

# Exercise 2
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# result = [even_number for even_number in numbers if even_number % 2 == 0]
# print(result)

# Exercise 3
with open('Day26/file1.txt',"r") as file1:
    file1_contents = file1.read().split()
    print(file1_contents)
  

with open("Day26/file2.txt", "r") as file2:
    file2_contents = file2.read().split()


result = [int(number) for number in file1_contents if number in file2_contents]
print(result)
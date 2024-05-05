student_heights = input("Enter the height of students: ").split(" ")
sum_of_height = 0

# we can also use sum()function to sum the list item 

for each_student_height in student_heights:
    sum_of_height += int(each_student_height)


print(sum_of_height)
average_height = round(sum_of_height/len(student_heights))
print("The average height of " + str(len(student_heights)) +" is " + str(average_height))
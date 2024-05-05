student_scores = input("Enter students score: ").split(" ")
highest_score = 0

# we can use max() function to find the max value in the list and like wise we can use min() function to find the min value in the list

for score in student_scores:
    if(highest_score < int(score)):
        highest_score = score

print(highest_score)
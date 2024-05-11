from dictionary_list import student_scores
# Creating an empty dictionary named student_grades
student_grades={}

for key in student_scores:
    if(student_scores[key] <= 70):
        student_grades[key] = "Fail"
    elif(student_scores[key] <= 80):
        student_grades[key] = "Acceptable"
    elif(student_scores[key]<= 90):
        student_grades[key] = "Exceeds Expectations"
    else:
        student_grades[key] = "Out standing"

print(student_grades)
for key in student_grades:
    print(key)
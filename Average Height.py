students_heights=input("Input a list of students heights.\n").split()
for n in range(0, len(students_heights)):
    students_heights[n]=int(students_heights[n])
print(students_heights)

total_height=0
for height in students_heights:
    total_height=total_height+height
print(total_height)   

number_of_students=0
for students in students_heights:
    number_of_students=number_of_students+1
print(number_of_students)    

number_of_students=len(students_heights)
average_height=round(total_height/ number_of_students)
print(average_height)
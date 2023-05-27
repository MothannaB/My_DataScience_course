
total = 0
num_of_grades = 0
average = 0

grades = [20, 78, 45, 55, 62, 97]

for ball in grades:
    if(ball >= 50):
        total = total + ball
        num_of_grades = num_of_grades+1

average = total / num_of_grades
print(average)
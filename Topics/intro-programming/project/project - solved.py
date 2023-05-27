from audioop import avg
from statistics import mean


school_data = {
    "stu_name": ["James" ,"Susan" ,"Laura" ,"Linda" ,"Linda" ,"Elizabeth" ,"David" ,"James" ,"Steven" ,"bob" ,"Elizabeth" ,"Daniel" ,"Laura" ,"David" ,"Michael" ,"Steven" ,"Susan" ,"bob" ,"bob" ,"Daniel" ,"David" ,"Elizabeth" ,"Susan" ,"Daniel" ,"Steven" ,"Linda" ,"Laura" ,"James" ,"Michael" ,"Michael"],
    "subject": ["biology", "math", "math", "biology", "art", "art", "biology", "art", "math", "math", "biology", "math", "biology", "math", "math", "biology", "art", "art", "biology", "biology", "art", "math", "biology", "art", "art", "math", "art", "math", "art", "biology"],
    "grade": [98, 63, 67, 99, 86, 85, 92, 85, 86, 73, 75, 92, 93, 84, 93, 77, 94, 94, 89, 75, 94, 88, 78, 91, 88, 66, 97, 92, 88, 89]
}

###########################
# stu_name subject grade  #

# James    biology  98    #
# Susan    math     63    #
# Laura    math     67    #
#   .       .       .     #
#   .       .       .     #
# Michael  biology  89    #
###########################



#--------------------------------


# how many unique students are there and who are they?
# hint: lookup and use the 'not in' operator and the list 'append()' function 

unique_s = []
counter = 0
for x in school_data['stu_name']:
    if (x  not in unique_s):
        unique_s.append(x)
        counter = counter + 1
print(counter)


#--------------------------------
# 1)put math grades in a separate list.
# 2)what is lowest math grade? 

subject_list = school_data['subject']
grade_list = school_data['grade']
math_list = []
for i in range(30):
    if subject_list[i] == "math":
        math_list.append(grade_list[i])

print(math_list, min(math_list))

#--------------------------------
# 1)put biology grades in a separate list.
# 2)what is lowest biology grade? 

subject_list = school_data['subject']
grade_list = school_data['grade']
biology_list = []
for i in range(30):
    if subject_list[i] == "biology":
        biology_list.append(grade_list[i])

print(biology_list, min(biology_list))
#--------------------------------
# 1)put art grades in a separate list.
# 2)what is lowest art grade? Hint: use the built-in 'min' function

subject_list = school_data['subject']
grade_list = school_data['grade']
art_list = []
for i in range(30):
    if subject_list[i] == "art":
        art_list.append(grade_list[i])

print(art_list, min(art_list))
#--------------------------------


# calculate Susan's GPA. 
# 1)put Susan grades in a separate list.
# 2)what is the average of the grades in the list? Hint: use the built-in 'mean' function

stu_list = school_data['stu_name']
grade_list = school_data['grade']
Susan_grades = []
for i in range(30):
    if stu_list[i] == "Susan":
        Susan_grades.append(grade_list[i])

print(Susan_grades, mean(Susan_grades))
#--------------------------------


# calculate David's GPA. 
stu_list = school_data['stu_name']
grade_list = school_data['grade']
David_grades = []
for i in range(30):
    if stu_list[i] == "David":
        David_grades.append(grade_list[i])

print(David_grades, mean(David_grades))
#--------------------------------


# Which student had the highest math grade?
stu_list = school_data['stu_name']
subject_list = school_data['subject']
grade_list = school_data['grade']
highest_math_grade = 0
highest_math_student = ""

for i in range(30):
    if subject_list[i] == "math":
        if grade_list[i] > highest_math_grade:
            highest_math_grade = grade_list[i]
            highest_math_student = stu_list[i]

print(highest_math_grade, highest_math_student)

# how many students got an 'A' grade?, 'B' grade?, 'C' grade?, 'D' grade?, 'F' grade? (grade scale -> 'A' : 90-100, 'B': 80-89, 'C' : 70-79, 'D' : 60-69, 'F': 0-59)
# fill these information in the below dictionary named 'grade_dict'
grade_dict= {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}

grade_list = school_data['grade']
for grade in grade_list:
    if(grade >=90):
        grade_dict['A'] = grade_dict['A']+1
    elif(grade >= 80 and grade < 90):
        grade_dict['B'] = grade_dict['B']+1
    elif(grade >= 70 and grade < 80):
        grade_dict['C'] = grade_dict['C']+1
    elif(grade >= 60 and grade < 70):
        grade_dict['D'] = grade_dict['D']+1
    else:
        grade_dict['F'] = grade_dict['F']+1

print(grade_dict)
        

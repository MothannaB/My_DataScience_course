from audioop import avg
from statistics import mean



#30 rows X 3 columns 

###########################
# stu_name subject grade  #

# James    biology  98    #
# Susan    math     63    #
# Laura    math     67    #
#   .       .       .     #
#   .       .       .     #
# Michael  biology  89    #
###########################










school_data = {
    "stu_name": ["James" ,"Susan" ,"Laura" ,"Linda" ,"Linda" ,"Elizabeth" ,"David" ,"James" ,"Steven" ,"bob" ,"Elizabeth" ,"Daniel" ,"Laura" ,"David" ,"Michael" ,"Steven" ,"Susan" ,"bob" ,"bob" ,"Daniel" ,"David" ,"Elizabeth" ,"Susan" ,"Daniel" ,"Steven" ,"Linda" ,"Laura" ,"James" ,"Michael" ,"Michael"],
    "subject": ["biology", "math", "math", "biology", "art", "art", "biology", "art", "math", "math", "biology", "math", "biology", "math", "math", "biology", "art", "art", "biology", "biology", "art", "math", "biology", "art", "art", "math", "art", "math", "art", "biology"],
    "grade": [98, 63, 67, 99, 86, 85, 92, 85, 86, 73, 75, 92, 93, 84, 93, 77, 94, 94, 89, 75, 94, 88, 78, 91, 88, 66, 97, 92, 88, 89]
}



#--------------------------------


# how many unique students are there and who are they?
# hint: lookup and use the 'not in' operator and the list 'append()' method 

# create a counter variable

counter = 0

# create empty unique names list for students

u_names_list = []

#  loop through student names 

for x in school_data['stu_name']:


# check if student already exist, if not, add the student to the u_list 
    if(x not in u_names_list):
        # increase counter by 1
        counter = counter + 1
        # add student to u_names_list
        u_names_list.append(x)




# print out the results
# print(counter, "\n", u_names_list)



#--------------------------------
# what is lowest math grade? Hint: use the built-in 'min' function

# get the subjects list
subject_list = school_data['subject']
# get the grades list
grades_list = school_data['grade']

# create an empty math grades list

math_grades = []

# loop through an index_list of 29 elements

for index in range(30):


#  check if the currect item in the subject_list is math
    if subject_list[index] == 'math':

#  if the previous condition was true, add the current grade from the grades_list to  math_grades list
        math_grades.append(grades_list[index])
# print out the results

print(math_grades, '\n', min(math_grades))



#--------------------------------
# what is lowest biology grade?




#--------------------------------
#what is lowest art grade? 




#--------------------------------


# calculate Susan's GPA. 
# what is the average of the grades in the list? Hint: use the built-in 'mean' function


#--------------------------------




# calculate David's GPA. 


#--------------------------------




# Which student had the highest math grade?


#--------------------------------




# how many students got an 'A' grade?, 'B' grade?, 'C' grade?, 'D' grade?, 'F' grade? (grade scale -> 'A' : 90-100, 'B': 80-89, 'C' : 70-79, 'D' : 60-69, 'F': 0-59)
# fill these information in the below dictionary named 'grade_dict'


        

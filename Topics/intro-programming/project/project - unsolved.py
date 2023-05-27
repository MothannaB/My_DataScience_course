from audioop import avg
from statistics import mean


school_data = {
    "stu_name": ["James" ,"Susan" ,"Laura" ,"Linda" ,"Linda" ,"Elizabeth" ,"David" ,"James" ,"Steven" ,"bob" ,"Elizabeth" ,"Daniel" ,"Laura" ,"David" ,"Michael" ,"Steven" ,"Susan" ,"bob" ,"bob" ,"Daniel" ,"David" ,"Elizabeth" ,"Susan" ,"Daniel" ,"Steven" ,"Linda" ,"Laura" ,"James" ,"Michael" ,"Michael"],
    "subject": ["biology", "math", "math", "biology", "art", "art", "biology", "art", "math", "math", "biology", "math", "biology", "math", "math", "biology", "art", "art", "biology", "biology", "art", "math", "biology", "art", "art", "math", "art", "math", "art", "biology"],
    "grade": [98, 63, 67, 99, 86, 85, 92, 85, 86, 73, 75, 92, 93, 84, 93, 77, 94, 94, 89, 75, 94, 88, 78, 91, 88, 66, 97, 92, 88, 89]
}

#Below is a visualization of the school_data dictionary as a table.

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




#--------------------------------
# 1)put math grades in a separate list.
# 2)what is lowest math grade? 






#--------------------------------
# 1)put biology grades in a separate list.
# 2)what is lowest biology grade? 




#--------------------------------
# 1)put art grades in a separate list.
# 2)what is lowest art grade? Hint: use the built-in 'min' function







#--------------------------------
# calculate Susan's GPA. 
# 1)put Susan grades in a separate list.
# 2)what is the average of the grades in the list? Hint: use the built-in 'mean' function






#--------------------------------
# calculate David's GPA. 





#--------------------------------
# Which student had the highest math grade?





# how many students got an 'A' grade?, 'B' grade?, 'C' grade?, 'D' grade?, 'F' grade? (grade scale -> 'A' : 90-100, 'B': 80-89, 'C' : 70-79, 'D' : 60-69, 'F': 0-59)
# hint : lookup and use the 'elif' statement(alongside 'if' and 'else') to test multiple conditions until one of them is met.
# fill these information in the below dictionary named 'grade_dict'(example: {'A':15, 'B':60, 'C':300, 'D':0, 'F':2})
grade_dict= {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
        

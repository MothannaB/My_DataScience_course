# Write two functions(min & max) that return the minimun and the maxiumum value in a list passed as input to the function.

# define a function called "min" and place a list as **input(parameter)**
def min(my_list):

    # create a variable to hold the first number in the list as the minimun.
    current_min = my_list[0]

    # loop through the list 
    for num in my_list:
        # check if the current number in the list is less than the current minimun
        if num < current_min:
            # if it's less, update the current minimun and set it equal to the current list item. Do nothing otherwise.
            current_min = num
    # after the loop is done, return(produce) the current minimun as the output
    return current_min

# create 2 lists of random student grades
alex_grades = [90, 66, 79, 83, 89, 55]
bob_grades = [76, 98, 73, 80, 54, 100]

# call the function twice and pass each student grades as the **input(argument)**. Make sure to create variables to hold the output
alex_min_grade = min(alex_grades)
bob_min_grade = min(bob_grades)

# print the minimun grade of alex and bob
print(alex_min_grade)
print(bob_min_grade)




 

my_list = [30, 12, 43, 22, 19]

# declare two variables to hold the count & sum and set their values to 0 initially.
list_count = 0
list_sum = 0

# loop through the list to calculate the sum and the count.
for item in my_list:

    # increase the list_count variable by 1
    list_count = list_count + 1
    # add the current item to the total
    list_sum = list_sum + item

list_average = list_sum/list_count
print(list_average)

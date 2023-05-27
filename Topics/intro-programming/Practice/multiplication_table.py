
# create 2 lists to multiply them by each other
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# loop through list1 and multiply each number by all the numbers in list2
for x in list1:
    # print a message telling which number we are multiplying by
    print(f"multiples of: {x}")
    # loop through all the numbers in list2
    for y in list2:
        # do the multiplication and store the result in a variable
        result = x * y
        # print the result
        print(result)
        # go to a new line by printing a newline character
    print("\n")

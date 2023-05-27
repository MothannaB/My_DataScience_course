# Write a function called search_item that takes a list and an item as inputs(parameters), and return 'True' if the item was found in the list and 'False' otherwise.


def search_item(my_list, searched_item):
    # create a variable called result and set it equal to False initially.
    result = False

    # loop through the list 
    for item in my_list:
        # check if the current item in the list is equal to search_item
        if item  == searched_item:
            # if it was found, update the 'result' variable to True
            result = True
    #after the loop is done, return(produce) the result as the output
    return result

pets = ["dog", "cat"]
status = search_item(pets, "cawt")

print(status)
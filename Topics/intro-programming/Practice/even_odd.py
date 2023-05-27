
# Write a function named even_odd that takes a number as input(parameter) and prints "even" if the number was even, and odd otherwise.
def even_odd(number):
    # an if statement to check if the number is even using the modulus operator(%)
    if(number % 2 == 0):
        print("The number entered is even")
    else:
        print("The number entered is odd")

        
# test the function on odd and even numbers.
number1 = 3
number2 = 12
number3 = 9237828
even_odd(number1)
even_odd(number2)
even_odd(number3)


# call/use a built-in function that takes a number(input) and return the absolute value of the number. Ex: input:-3.59, output:3.59

x = abs(-7.2)
print(x)

# call/use a built-in function that takes a number(input) and return the number rounded to the nearest integer. Ex: input:12.69, output:13

y = round(2.6485, 2)
print(y)

# call/use a built-in function that takes a list and returns the length of the list(# of items inside it). Ex: input:[1, 5, 12, 19], output:4

z = [1,2,5, 12]
print(len(z))

# call/use a built-in function that takes 2 numbers x & y as input and returns x raised to the power y (xy). Ex: inputs: 2 & 5, output:32

d = pow(2, 8)
print(d)

# call/use a built-in function that takes a list as input and returns(output) the same list but reversed. Store the reversed list inside a variable and then loop through the list to print out its items.
# Ex: input: ['dog', 'cat', 'bird'], output: ['bird', 'cat', 'dog']
k = ['a', 'b', 'c', 'd']
k_reversed = reversed(k)
for letter in k_reversed:
    print(letter)

# call/use a built-in function that takes a number X as input and returns a sequence of numbers that start from 0, increments by 1 and stops at the number X-1.
# Ex: input: 7, output: [0, 1, 2, 3, 4, 5, 6]

r = range(9)
print(r)
for number in r:
    print(number)


# call/use a built-in function that takes a list as input and returns(output) the same list but sorted. Ex: input: [19, 21, 0, 35, -2], output: [-2, 0, 19, 21, 35]
w = [40, 18, -9, -3, 8, 15]
print(sorted(w))
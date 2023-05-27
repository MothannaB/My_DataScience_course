#write a program that swaps the values of 2 variables, x=4, y=12, and then print the variables

#declare variables x and y and assign values to them
x = 4
y = 12

#print the current values of x and y
print(x, y)

#create a temorary variable to hold the value of x
holder = x
# place y in x
x = y

#place the value of 'holder' inside y
y = holder

#print the current values of x and y
print(x, y)
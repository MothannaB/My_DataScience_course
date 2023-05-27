def square(num):
    x = num * num
    return x

def cube(num):
    x = num * num * num
    return x


def my_avg(a, b, c):
    total = a + b + c
    avg = total / 3
    return avg


my_average = my_avg(2, 4, 12)
print(my_average)
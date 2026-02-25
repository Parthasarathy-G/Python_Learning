### Assignment 15: Fibonacci Sequence

# todo - Write a program that prints the first n Fibonacci numbers, where n is input by the user.

n = int(input("Enter the number of Fibonacci numbers to print: "))
a, b = 0, 1
count = 0
while count < n:
    print(a)
    a, b = b, a + b
    count += 1
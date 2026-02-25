### Assignment 12: Factorial Calculation

# todo - Write a program that calculates the factorial of a number input by the user using a while loop.

user = int(input())
sum = 1
while(user!=0):
    sum *= user
    user = user - 1
print(sum)
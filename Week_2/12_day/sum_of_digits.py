### Assignment 13: Sum of Digits

# todo - Write a program that calculates the sum of the digits of a number input by the user using a while loop.

user = int(input())
sum = 0
while user > 0:
    temp = user % 10
    sum += temp
    user = user // 10

print(sum)
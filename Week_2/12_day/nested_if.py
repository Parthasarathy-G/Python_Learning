# Assignment 4: Nested if Statement
 
# todo - Write a program that asks the user to input a number and prints whether the number is positive and even, positive and odd, or negative.

user = int(input())
if(user > 0):
    if(user%2==0):
        print("Positive and even")
    else:
        print("Positive and odd")
else:
    print("Negative")
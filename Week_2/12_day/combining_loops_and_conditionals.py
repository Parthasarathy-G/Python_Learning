### Assignment 11: Combining Loops and Conditionals

# todo - Write a program that asks the user to input a number and prints all the even numbers from 1 to that number using a for loop.

user = int(input())

for i in range(1, user + 1):
    if(i%2==0):
        print(i," ")
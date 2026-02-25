## Assignment 14: Prime Number Check

# todo - Write a program that checks if a number input by the user is a prime number using a for loop.

user = int(input())

if user <= 1:
    print("Not a prime number")
else:
    for i in range(2, int(user ** 0.5) + 1):
        if user % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
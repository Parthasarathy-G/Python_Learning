### Assignment 8: break Statement

#  todo - Write a program that asks the user to input numbers until they input 0. The program should print the sum of all the input numbers.

#  ! With break statement
sum = 0
user = 1
while(sum != -1):
 user = int(input())
 sum += user
 if(user == 0):
        break
print(sum)

#  ! Without break statement
# sum = 0
# user = 1
# while(user != 0):
#  user = int(input())
#  sum += user

# print(sum)
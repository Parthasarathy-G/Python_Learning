# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You can vote.")
# else:
#     print("You are too young to vote.")


# mark = int(input("Enter your mark: "))
# if mark >=90:
#     print("Grade A")
# elif mark >=80:
#     print("Grade B")
# else:
#     print("Grade C")


# age = 15
# has_license = 'yes'
# if age >= 18:
#     if has_license == 'yes':
#         print("You can drive.")
#     else:
#         print("You need a license to drive.")
# else:
#     print("You are too young to drive.")


# recharge_amount = 200
# data_balance = 1.5
# if recharge_amount >= 390 or data_balance >= 1:
#     print("You are eligible")
# else:
#     print("You are not eligible")


order_amount = 1000
day = 'mon'
Memembership = 'Gold'

if (order_amount >= 1000 and day in ['sun', 'sat']) or Memembership == 'Gold':
    print("20% Discount")
else:
    print("No Discount")
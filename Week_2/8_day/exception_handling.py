# print("Step 1: Start")

# a = 10
# b = 0
# try:
#  result = a / b #Crash here
# except Exception:
#  print("Operation not performsble")

# print("Step2: Result is", result)

try:
    number = int(input("How many times? : "))
    total = 200 * number
    average = total / number
    print("Average price:", average)
except ZeroDivisionError:
    print("You cannot order 0 times.")
except FileNotFoundError:
    print("File not found")

print("Next code block")
"""
This code demonstrates variable scope in Python.
"""

def order(): # Function to place an order
    food = 'Rice' # Local variable to store the food item
    print('Order received: {food}')

order()

# print(food)
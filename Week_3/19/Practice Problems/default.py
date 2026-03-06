### Assignment 2: Function with Nested Default Arguments

## Define a function that takes two arguments, a and b, where b is a dictionary with a default value of an empty dictionary. The function should add a new key-value pair to the dictionary and return it. Test the function with different inputs.

c = {}
def add(a,b=None):
    if b == None:
        b = {}

    b[a] = a ** 2
    c.update(b)
    return b

# Test
print(add(2))  # {2: 4}
print(add(3, {1: 1}))  # {1: 1, 3: 9}
print(c) # {2: 4, 1: 1, 3: 9}

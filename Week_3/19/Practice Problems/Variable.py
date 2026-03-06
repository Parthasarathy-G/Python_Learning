### Assignment 3: Function with Variable Keyword Arguments

## Define a function that takes a variable number of keyword arguments and returns a dictionary containing only those key-value pairs where the value is an integer. Test the function with different inputs.


def check(**kwargs):
    return {k:v for k,v in kwargs.items() if isinstance(v,int)}

print(check(a=1, b='two', c=3, d=4.5))
print(check(x=10, y='yes', z=20))
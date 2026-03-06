### Assignment 1: Fibonacci Sequence with Memoization

## Define a recursive function to calculate the nth Fibonacci number using memoization. Test the function with different inputs.

def fib(n,memo={}):

    if n <= 1:
        return n
    
    if n in memo:
        return memo[n]
    
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

print(fib(10))
print(fib(1))
print(fib(5))
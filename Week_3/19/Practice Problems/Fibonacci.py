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
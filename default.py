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

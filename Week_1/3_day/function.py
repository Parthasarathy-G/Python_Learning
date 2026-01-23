# def great(name):
#     print(f"Welcome to home {name}")
# great("Parthasarathy")

# def add(a, b):
#     return a + b


def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1,2,5,10,6,6))
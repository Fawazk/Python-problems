# A simple generator for Fibonacci Numbers
def fib(limit):
    print(limit)
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        c = a + b
        a = b
        b = c


# Create a generator object
# x = fib(int(input("Enter a number?")))

# # # Iterating over the generator object using next
# print(next(x)) # In Python 3, __next__()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# Iterating over the generator object using for
# in loop.
for i in fib(int(input("Enter a number?"))):
    print(i, end=" ")
print()

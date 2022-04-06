# Decorators
def twice(func):
    def inner(num1, num2):
        func(num1, num2)
        func(num1, num2)

    return inner


@twice
def multiply(n1, n2):
    print(n1 * n2)


n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))

multiply(n1, n2)


# Generators
def fibonacci_sequence():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


f = fibonacci_sequence()
n = int(input("enter the value of n: "))
for i in range(n):
    print(next(f))

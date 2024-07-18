''''def lamb(x):
    print(f'result of lambda function is {x(5)}')
lamb(lambda y: y*5)

print()'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n=10
print(f'Fibonacci series of {n} is : {fibonacci(n)}')

print()

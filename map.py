num =[1,2,3,4,5]
def square(x):
    for i in x:
        print(i**2)

square (num)
print()

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared= map(square, numbers)

result = list(squared)


numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)


# result_list = list(doubled_numbers)
result_list= list(map(lambda x: x * 2, numbers))

print(result_list)

print()
number1 = [1, 2, 3, 4, 5]
number2 = [10, 20, 30, 40, 50]

doubled_numbers = map(lambda x,y: x * y, number1,number2)

# result_list = list(doubled_numbers)
result_list= list(map(lambda x,y: x * y, number1,number2))

print(result_list)
#ques 1
""" def remove_spaces(s):
    result = ""
    for char in s:
        if char != " ":
            result += char
    return result
s = "Hello World"
result = remove_spaces(s)
print( s)
print (result)"""

#ques 2
"""def check_number(num):
    if num > 0:
        print(f"{num} is positive ")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print(f"{num} is a zero")
num = 10
check_number(num) 
num = 5
check_number(num)  
num= 2
check_number(num)
num= 0
check_number(num)
num= -2
check_number(num)"""

#ques 3
"""def check_number(num):
    if num > 0:
        print(f"{num} is positive")
    else:
        print(f"{num} is negative")

num = 5
check_number(num)"""

#ques 4
"""def print_number():
    num =1 
    while num <= 10:
        print(num)
        num += 1

print_number()"""

#ques 5
"""def cal_sum():
    num = 1
    sum = 0
    while num <= 10:
        sum += num
        num += 1
    return sum
total_sum = cal_sum()
print('The sum of numbers from 1 to 10 is:', total_sum)"""

#ques 6
"""def find_largest (a,b,c):
    if a >= b:
        if a >= c:
            largest = a
        else:
            largest = c
    else:
        if b >= c:
            largest =b 
        else: 
            largest =c
    return largest

num1= 5
num2= 10 
num3=2
largest_num = find_largest(num1,num2,num3)
print(f"{largest_num}")"""
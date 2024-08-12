import random 
random_list = [random.randint(1,100) for _ in range(10)]
odd_list = [num for num in random_list if num % 2 != 0 ]
even_list = [num for num in random_list if num % 2 == 0]

print('random list: ', random_list)
print('odd list: ', odd_list)
print('even list: ', even_list) 
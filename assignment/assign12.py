user_input = input('enter a string: ')
output_str = ''.join(char for char in user_input if char.lower() not in 'aeiou')
print('string after removing vowles : ', output_str)
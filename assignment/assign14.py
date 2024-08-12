friends_dict = {
    'pruthika': '123-456-4567',
    'parnika': '987-345-6788',
    'swaraa': '234-500-2345',
    'manasi': '456-208-5678'
}

for name in sorted(friends_dict):
    print(f'{name}: {friends_dict[name]}')

name = input('\nEnter a name: ')
if name in friends_dict:
    print(f'{name} is in a dictionary. phone number : {friends_dict[name]}')
else:
    friends_dict[name]= input('enter a number :')
    print(f'{name} added.')

print('\nUpdated dictionary: ')
for name in sorted(friends_dict):
    print(f'{name}: {friends_dict[name]}')
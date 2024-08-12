num_lines= 5
for i in range(1, num_lines +1 ):
    for j in range(i):
        print(i, end='')

    for k in range(num_lines - i):
        print('', end='')

    print()
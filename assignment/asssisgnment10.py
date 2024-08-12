def calculate_simple_intrest(p,n,r):
    return(p* n* r)/100
for i in range(1,4):
    p= float(input(f'enter the principal{i}: '))
    n= float(input(f'enter the years {i}: '))
    r= float(input(f'enter the rate{i}: '))
    intrest = calculate_simple_intrest(p,n,r)
    print(f'simple intrest{i}: {intrest}')
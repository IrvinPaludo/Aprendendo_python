
from math import factorial
print('---FATORIAL---')
n1 = int(input('digite um numero:'))
c = 0
print(f'{n1}! = ',end=(''))
while n1-c != 0:
    
    print(f'{n1-c} ',end=(''))
    if n1-c != 1:
        print(' * ',end=(''))
    c += 1
print(f'= {factorial(n1)}')


n1 = int(input('Digite um numero: '))
r = True
for c in range(2,n1):
    if n1 % c == 0:
        r = False
        break

if r and n1 > 1:
    print(f'O numero {n1} é primo')
else:
    print(f'O numero {n1} não é primo')
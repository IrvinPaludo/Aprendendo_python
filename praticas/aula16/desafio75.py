num= (int(input('Digite um numero: ')),int(input('Digite um numero: ')),
      int(input('Digite um numero: ')),int(input('Digite um numero: ')),
      int(input('Digite um numero: ')))

    
print(f'Foi digitado {num.count(9)} mumeros 9')
if 3 in num :
    print(f'O primeiro numero 3 está: {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares são: ',end='')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')
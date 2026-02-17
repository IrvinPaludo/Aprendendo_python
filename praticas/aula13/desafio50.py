soma = 0
print('digite só numeros')
for c in range(1,7):
    n = int(input('Digite o {}º número: '.format(c)))   
    if n % 2 == 0:
        soma += n
if soma != 0:
    print(f'A soma dos números pares é: {soma}')
else:
    print('você não digitou numeros pares')
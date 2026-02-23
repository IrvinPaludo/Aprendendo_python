'''Aprimore o desafio anterior 
a- some todos os valores pares digitados
b- some todos os valores da 3ª coluna
c- o maior numero da 2ª coluna'''


matriz = [[0,0,0],[0,0,0],[0,0,0]]
maior= par = soma = 0



for l in range(0,3):
   for c in range(0,3):
       matriz[l][c]=int(input(f'Digite o numero da posição [{l}] [{c}]: '))
       if matriz[l][c] % 2 == 0:
           par += matriz[l][c] 
       if l == 1:
           if maior < matriz[l][c] :
               maior = matriz[l][c]                 
       if c == 2:
           soma += matriz[l][c] 
           print(f'{matriz[l][c] }')

for l in range(0,3):
   for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
   print('')

print(f'A soma dos numeros pares é {par}')
print(f'O maior numero da 2ª linha é: {maior}')
print(f'A soma da 3ª coluna é {soma}')
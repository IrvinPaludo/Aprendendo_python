'''Crie uma matriz de dimensão 3x3 e prencha com valores lidos pelo teclado
No final motre a matriz natela, com a formatação correta '''

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
   for c in range(0,3):
       matriz[l][c]=int(input(f'Digite o numero da posição [{l}] [{c}]: '))

for l in range(0,3):
   for c in range(0,3):
        print(f'{matriz[l][c]:^5}',end=' ')
   print('')
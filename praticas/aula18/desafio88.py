'''faça um programa que ajude um jogador da mega sena a criar palpites
o programa vai perguntar quantos jogos vão ser 
cadastrando tudo em uma lista composta'''
from random import randint
from time import sleep

jogos = []
sorteio = []

q = 0 
print('-=-'*11)
print(f'{'JOGA NA MEGASENA':^33}')
print('-=-'*11)
q = int(input('Quantos jogos você quer: '))

for c in range(0,q):
   cont = 0
   while True:
        num = randint(1,60)
        if num not in sorteio:
            sorteio.append(num)
            cont += 1
        if cont >= 6:
           break 
   sorteio.sort()
   jogos.append(sorteio[:])
   sorteio.clear()
print(f'Sorteando {q} Jogos')
for j in range(1,q+1):
    print(f'{f'{j}º Jogo:':<8} {'.'*3} {f'{jogos[j-1]}':<25}')
    print('')
    sleep(0.8)
#print(f'{jogos}')
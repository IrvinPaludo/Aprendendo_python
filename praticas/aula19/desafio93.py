''' Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols
 feitos durante o campeonato.'''

jogador={}
gols=[]
total = 0
jogador['nome']= str(input(f'Qual é o nome do jogador: '))
jogador['jogos']=int(input(f'Quantos jogos o {jogador["nome"]} jogou: '))
for j in range(1,jogador['jogos']+1):
    gols.append(int(input(f'Quantos gols ele fez no jogo {j}: ')))

jogador['gols'] = gols
for g in gols:
    total += g
jogador['total'] = total
print('-=-'*10)
print(jogador)
print('-=-'*10)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-'*10)

print(f'O {jogador["nome"]} jogou {jogador["jogos"]} partidas.')

for j in range(1,jogador['jogos']+1):
    print(f'=> Na partida {j}, fez {gols[j-1]}')
print(f'Foi um total de {jogador["total"]}')
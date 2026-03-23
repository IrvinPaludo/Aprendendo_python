''' Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de 
cada jogador.'''
jogadores = []
jogador={}
gols=[]
total = 0
m = ''
numero = 0
while True:
    gols=[]
    total = 0
    jogador.clear()
    jogador['nome']= str(input(f'Qual é o nome do jogador: '))
    jogador['jogos']=int(input(f'Quantos jogos o {jogador["nome"]} jogou: '))
    for j in range(1,jogador['jogos']+1):
        gols.append(int(input(f'Quantos gols ele fez no jogo {j}: ')))

    jogador['gols'] = gols
    for g in gols:
        total += g
    jogador['total'] = total
    jogadores.append(jogador.copy())

    while True:
        m = str(input('Quer continuar: S/N ')).upper()[0]
        if m in 'nNsS':            
            break
        elif m not in  'nNSs':
            print('ERRO! Porfavor digite apenas [S/N]')
    if m in 'nN':
        break
print('-=-'*10)
print(f'{"Lista de jogadores:":^30}')
print('-=-'*10)

for i,j in enumerate(jogadores):
    print(f"{i:<2}: {j['nome']:.^15} {j['total']}")

while True:
    numero = int(input('Qual jogador você quer olhar: (999 sair) '))
    if numero == 999:
        break
    print('-=-'*15)
    if numero >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {numero}!')
    else:
        print(f'{numero}: {jogadores[numero]["nome"]}...{jogadores[numero]["total"]}')
        for i, j in enumerate(jogadores[numero]['gols']):
            print(f'jogo {i} fez {j}')
        print('-=-'*15)
print('SAINDO.')
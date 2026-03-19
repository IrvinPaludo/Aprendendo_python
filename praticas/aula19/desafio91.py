'''cre um programa onde 4 jogadores vão jogar um dado e tenham resultados aleatorios. Guarde estes valores em dicionario.
No final coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior número  '''
from random import randint
from time import sleep
from operator import itemgetter

jogadores={'jogador1':randint(1,6),'jogador2':randint(1,6),'jogador3':randint(1,6),'jogador4':randint(1,6)}

ranking= {}
print(f'Valor Sorteados')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)

ranking=sorted(jogadores.items(),key=itemgetter(1),reverse=True)
print('-=-'*10)
print(f'{'= Ranking =':^30}')
for k, v in enumerate(ranking):
    print(f'O {k+1}° lugar: {v[0]} com {v[1]}')
    sleep(0.5)
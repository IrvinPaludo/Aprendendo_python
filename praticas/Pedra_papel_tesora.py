from random import randint
from time import sleep

itens = ('Pedra','Papel','Tesoura')

print('Jogo Pedra papel tesora')
print('opções: \n [0] PEDRA \n [1] PAPEL \n [2] TESOURA ')

jogador = int(input('Qual sua jogada? '))

print('JO ')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
computador = randint(0,2)
print('-=-'*11)
print('jogador escolheu {}'.format(itens[jogador]))
sleep (1)
print('computador escolheu {}'.format(itens[computador]))
sleep(1)


if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('O Jogador ganho !!')
    elif jogador == 2:
        print('O Computador ganho !!')
    else:
        print('jogada invalida')
elif computador == 1:
    if jogador == 0:
        print('O Computador ganho !!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('O Jogador ganho !!')
    else:
        print('jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('O Jogador ganho !!')
    elif jogador == 1:
        print('O Computador ganho !!')
    elif jogador == 2:
        print('Empate')
    else:
        print('jogada invalida')
print('-=-'*11)

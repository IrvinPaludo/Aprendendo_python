'''Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros opcionais: o nome de um jogador 
e quantos gols ele marcou. O programa deverá ser capaz de
 mostrar a ficha do jogador, mesmo que algum dado não 
 tenha sido informado corretamente.
'''

def ficha(j=0,g=0):


    if j != 0:
        print(f'O jogador {j} fez {g} gols')
    else:
        print(f'O jogador <desconhecido> fez {g} gols')

jogador = str(input('Nome do jogador: '))
gol = 0
if jogador != 0:    
    gol=input(f'Quantos gols {jogador} fez: ')
else:
    gol=input(f'Quantos gols <Deconhecido> fez: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

ficha(jogador,gol)

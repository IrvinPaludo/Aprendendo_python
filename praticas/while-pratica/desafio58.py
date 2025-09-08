from random import randint 

nl = randint(1,11)
vitoria = 0
contador = 0
p = 0

print('-=- Jogo da adivinhação: (1,10) -=-')

while nl != p :
    p = int(input('Tente a sorte:'))
    contador +=1
    print('-=-'*10)

print('-=- Você acertou !!! -=- ')
print(f'O numero era: {nl}')
print(f'Você tentou: {contador}')

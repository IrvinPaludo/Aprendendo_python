from random import randint 

nl = randint(1,11)
contador = 0
p = 0

print('-=- Jogo da adivinhação: (1,10) -=-')

while nl != p :
    p = int(input('Tente a sorte:'))
    if nl !=p:
        if nl < p:
            print('o numro é menor')
        else:
            print('o numero é mairor')
    contador +=1
    print('-=-'*10)

print('-=- Você acertou !!! -=- ')
print(f'O numero era: {nl}')
print(f'Você tentou {contador} vezes')

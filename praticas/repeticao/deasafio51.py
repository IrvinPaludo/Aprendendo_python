from time import sleep

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite a razão: '))

for c in range(0,10):
    print(f'{n1+(c)*n2}')
    sleep(0.5)
print('FIM')
#Desafio 51 - Progressão Aritmética
from time import sleep
print('='*30)
print('   10 TERMOS DE UM PA')
print('='*30)
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite a razão: '))

for c in range(0,10):
    print(f'{n1+(c)*n2}', end=" -> " )
    
print('FIM')
#Desafio 51 - Progressão Aritmética

from time import sleep
print('='*30)
print('   10 TERMOS DE UM PA')
print('='*30)
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite a razão: '))
c= 0

while c <= 9:
    print(f'{n1+(c)*n2}', end=" -> " )
    c+=1
print('FIM')
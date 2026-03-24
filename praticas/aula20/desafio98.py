'''Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo. Seu programa 
tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep
def lin(a):
    print('')
    print('-=-'*a)
    
def contador(a,b,c):
    lin(10)
    
    
    print(f'Contagem de {a} até {b} de {abs(c)} em {abs(c)}')
    sleep(3)
    if a > b :
        b-=1
        if c > 0 :
            c*=-1
    else:
        b+=1
        c = abs(c)
    for valor in range(a,b,c):
        print(f'{valor}', end=' ',flush=True )
        sleep(0.3)
    lin(10)

contador(1,10,1)

contador(10,0,2)

print('Sua ves de personalizar a contagem!')
i= int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if p == 0:
    p =1

contador(i,f,p)
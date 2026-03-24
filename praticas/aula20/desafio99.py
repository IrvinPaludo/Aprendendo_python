'''Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros. Seu programa 
tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep
def lin(a):
    sleep(1.5)
    print('')
    print('-=-'*a)
    print('')
    

def maior(*num):
    cont = maior = 0
    print(f'Os numeros digitados foram:',flush=True)
    sleep(1)
    for valor in num:
        
        print(f'{valor}', end=' ',flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'Foram digitados {cont} e o maior é {maior}')
    
           
lin(10)
maior(1,9,5,2)
lin(10)
maior(3,5,6,7)
lin(10)
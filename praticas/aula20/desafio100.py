''' Faça um programa que tenha uma lista chamada números e 
duas funções chamadas sorteia() e somaPar(). A primeira função 
vai sortear 5 números e vai colocá-los dentro da lista e a segunda 
função vai mostrar a soma entre todos os valores pares sorteados 
pela função anterior.'''
from random import randint
from time import sleep
def sorteia():
    print('-=-'*10)
    print(f'Números sorteados')
    for c in range(0,5):
        n = randint(0,10)
        print(f'{n}',end=' ', flush=True)
        sleep(0.3)
        numero.append(n)
def somapar(v):
    par = 0
    for n in v:
        if n % 2 == 0:
            par += n
    print(f'\nA soma dos numeros pares é: {par}')
    sleep(0.3)
numero =[]


sorteia()
somapar(numero)
#print(numero)

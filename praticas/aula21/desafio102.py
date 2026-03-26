'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
 o primeiro que indique o número a calcular e outro chamado show, que será um 
 valor lógico (opcional) indicando se será mostrado ou não na tela o processo 
 de cálculo do fatorial'''

def fatorial(n=1,show=False):
    """
     fatorial(n,show=false)
        ->Calcula o fatorial de um numero
        :para n: O numero a ser calculado
        :para show:(opcional): mostra ou não a conta 
        
    """
    
    f = 1
    cont = n
    for v in range(n,0,-1):
        if show == 'S':
            print(f'{v}', end='')
            if v > 1:
                print('x',end='')
            else:
                print(f'=',end='')
        f *= v
    return f'{f}'  
 

help(fatorial)
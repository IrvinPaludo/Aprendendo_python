'''Crie um programa que tenha uma função chamada voto() que vai 
receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(a):
    from datetime import date
    idade = date.today().year-a

    if idade < 16 :
        return f'Com {idade} anos Não vota'
    elif 16 <= idade < 18 or idade >=65 :
        return f'Com {idade} anos o voto é: Opcional'
    elif idade < 60 :
        return f'Com {idade} anos o voto é: Obrigatorio'
    
    


ano = int(input('Em que ano você naceu? '))

print(voto(ano))

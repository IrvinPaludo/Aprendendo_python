from random import randint
verde = '\033[32m'
vermelho = '\033[31m'
limpa = '\033[m'
n1 = s = cv = cj = 0
n2 = v = ' '
print('Vamos jogar Par ou impar')
while True :
    print('-=-'*20)
    com1 = randint(0,10)
    n1 = int(input('Qual numero você quer: '))
    #print(n2)
    n2 = ' '
    while n2 not in 'PI':
        n2 = str(input('PAR OU IMPAR:(I/P) ')).upper().strip()
    s = com1 + n1
    cj+=1
    if s%2 == 0:
        v = 'P'
    else:
        v = 'I'
    if n2 != v:   
        break
    else:
        print(f'{verde}Vitoria!{limpa}')
        cv+=1

print('-=-'*20)
print(f'{vermelho}Você perdeu{limpa}')
print(f'Você jogou {n1} {n2} e o computador {com1}: A som é {s} e é {v}')
print(f'Voce ganhou {cv} de {cj} jogos')

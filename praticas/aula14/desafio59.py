
n1 = n2 = n3 = 0

comando = 0

while comando != 5:
    
    n1 = float(input('Digite o primeiro numero: '))
    n2 = float(input('Digite o segundo numero: '))
    print('O que você quer fazer: ')
    comando = int(input(' (1)Somar\n (2)Multiplicar\n (3)Maior\n (4)Novos numeros\n (5)Sair do programa\n '))
    if comando == 1:
        print(f'A soma dos numeros {n1} e {n2} é {n1+n2}') 
    elif comando == 2:
        print(f'A multiplicação de  {n1} e {n2} é {n1*n2}')
    elif comando == 3:
        if n1 > n2 :
            print(f'O maior numero entre {n1} e {n2} é {n1}')
        else:
            print(f'O maior numero entre {n1} e {n2} é {n2}')
    comando = int(input('Quer continuar, sim(1) não(5): '))
print('FIM!')

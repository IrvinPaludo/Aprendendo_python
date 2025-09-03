#variaveis
n1 = int(input('Digite um numero: ')) #numero testado
r = True #variavel resposta

for c in range(2,n1): #testa todos os numeros de 2 até n1-1

    if n1 % c == 0: #se o resto da divisão for 0, não é primo
        r = False
        break

if r and n1 > 1: #se r continuar True e n1 for maior que 1, é primo
    print(f'O numero {n1} é primo')
else:
    print(f'O numero {n1} não é primo')
from desafio108pasta import moeda

n = int(input('Digite um numero: '))
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n)}')
print(f'O Dobro de {moeda.moeda(n)} é {moeda.dobro(n)}')
print(f'Aumentando 10%, temos {moeda.aumentar(n,10)}')
print(f'Reduzindo 13%, temos {moeda.reduzir(n,13)}')
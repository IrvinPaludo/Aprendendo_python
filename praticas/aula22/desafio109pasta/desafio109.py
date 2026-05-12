import moeda

n = float(input('Digite um numero:R$'))
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n,)}')
print(f'O Dobro de {moeda.moeda(n)} é {moeda.dobro(n,False)}')
print(f'Aumentando 10%, temos {moeda.aumentar(n,10)}')
print(f'Reduzindo 13%, temos {moeda.reduzir(n,13)}')
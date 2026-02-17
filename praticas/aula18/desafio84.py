'''
Faça um progama que leia o nome e o peso de varias pessoas,quardando tudo em uma lista .No final,mostre:
A)Quantas pessoas foram cadastradas 
B)Uma lista com as pessoas mais pesadas 
C)Uma lista com as pessoas mais leves
'''
dados = []
pessoas = []
pesadas = []
leves = []
m = 'S'
quant = media = totalpeso = 0

while True:
    if m == 'S':
        dados.append(input('Nome: '))
        dados.append(int(input('Peso: ')))
        pessoas.append(dados[:])
        totalpeso += dados[1]
        dados.clear()
        quant +=1
    elif m == 'N':
        break
    m = input('Quer cadastras mais alguem? [S/N] ').upper()

media = totalpeso/quant
#print(pessoas)
print('-=-'*25)
print(f'Foram cadastrados {quant} pessoas')
print('-=-'*25)
for p in pessoas:
    if p[1] >= media:
        pesadas.append(p[0])
    else:
        leves.append(p[0])

print(f'As pesso mais pesadas são: {pesadas}')
print(f'As pesso mais leves são: {leves}')
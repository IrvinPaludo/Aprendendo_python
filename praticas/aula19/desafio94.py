''' Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados 
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
pessoas = []
acima = []
dados = {}
soma = mulheres =  media = 0

while True:
    dados['nome']= str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: (M/F) ')).upper()[0]
        if dados['sexo'] in 'MmfF':
            break
        else:
            print('ERRO! Porfavor digite apenas [M/F]')
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())

    while True:
        m = str(input('Quer continuar: S/N ')).upper()[0]
        if m in 'nNsS':            
            break
        elif m not in  'nNSs':
            print('ERRO! Porfavor digite apenas [S/N]')
    if m in 'nN':
        break

print('-=-'*10)
print('Dados cadastrados'^30)
print(f'Foram cadastradas {len(pessoas)}')

for p in pessoas:
    soma += p['idade']
media = soma/len(pessoas)
print(f'A media da idade é {media}')

for p in pessoas:
    if p['sexo'] == 'F':
        mulheres +=1
print(f'Foram cadastradas {mulheres}')

for p in pessoas:
    if p['idade'] >= media:
        acima.append(p['nome'])     
print(f'Pessoas acima da idade media:')
for p in acima:
    print(f'{p}' , end=' - ')

#print(pessoas)
print('-=-'*10)

nome = ''
idade = 0
sexo = 0
maisvelho = ''
mulnovas = 0
somaidade = 0
id_maisvelho = 0

for c in range (1,5):
    print(f'--- {c}ª pessoa ---')
    nome = str(input('Qual é seu nome? '))
    idade = int(input('Qual é sua idade? '))
    sexo = str(input('Qual é seu sexo? (M)Home (F)Mulher ')).upper().strip()
    print('\n')

    somaidade += idade 
    mediaidade = somaidade/c

    if sexo == 'M':
        if idade > id_maisvelho:
            maisvelho = nome
            id_maisvelho = idade
    else:
        if idade < 20:
            mulnovas +=1

print(f'A média da idade é {mediaidade}')
print(f'O homem mais velho é {maisvelho} e ele tem {id_maisvelho}')
if mulnovas ==1:
    print(f'Há {mulnovas} mulher menor de 20 anos')
else:
    print(f'Há {mulnovas} mulheres menores de 20 anos')
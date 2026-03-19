from time import sleep
aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media']>= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
sleep(0.5)
print(f'O nome é {aluno["nome"]}')
print(f'A média foi {aluno["media"]}')
print(f'A sitiação {aluno["situação"]}')
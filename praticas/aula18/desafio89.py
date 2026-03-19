'''crie um programa que leia nome e duas notas de varios alunos e quarde
tudo em uma lista composta.No final mostre um boletim contendo amédia de
cada aluno, permitindo que o usuarui possa mostrar as notas de cada aluno individualmente'''
alunos = []
dados = []
m = ''
print('Cadastro de notas de alunos ')

while True:
    dados.append(str(input('Nome do aluno: ')))
    dados[1].append(float(input('1ª nota: ')))
    dados[1].append(float(input('2ª nota: ')))
            
    alunos.append(dados[:])
    dados.clear()
                    
    m = str(input('Quer continuar: Sim(S)/Não(N) ')).upper()
    if m == 'N':
        m = ''
        break
print('Boletim:')
for c in range(len(alunos)):
    print(f'(ID:{c+1:^3}){alunos[c][0]:.<15}:{(alunos[c][1][1]+alunos[c][1][2])/2:^3.2f}')
    while True:
        n = int(input('Quer ver as notas de qual aluno:(ID) '))-1
        if n in range(len(alunos)):
            print(f'(ID:{n+1:^3}){alunos[n][0]:.<15}:{alunos[n][1][1]:^3.2f}  {alunos[n][1][2]:^3.2f}')
        else:
            print('Valor invalido')
        m = str(input('Quer continuar: Sim(S)/Não(N) ')).upper()
        if m == 'N':
            break
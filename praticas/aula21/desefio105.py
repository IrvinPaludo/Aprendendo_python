'''Faça um programa que tenha uma função notas() 
que pode receber várias notas de alunos e vai retornar 
um dicionário com as seguintes informações:

Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''


def nota(*n, sit=False):
    """
    Função para avaliar as notas e a situação de uma clase
    :para n:um ou mais notas dos alunos (aceita variavel)
    :para sit:(opcional) demosntra  a situação da clase
    :retun: dicionario com varias informações sobre a situação da clase
    """
    
    clas={}
    clas['total'] = len(n)
    clas['Maior'] = max(n)
    clas['menor'] = min(n)
    clas['Média'] = sum(n)/len(n)

    if sit:
        if clas['Média'] >= 7:
            clas['situação'] = 'BOA'
        elif clas['Média'] >= 5:
            clas['situação'] = 'RAZOÁVEL'
        else:
            clas['situação'] = 'RUIM'
        
    return clas


resp = nota(5.5 ,2.5 ,1.5 ,sit=True )
print(resp)
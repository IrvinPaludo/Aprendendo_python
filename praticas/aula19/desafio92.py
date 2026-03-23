'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import date


pessoa={}
pessoa['nome']=str(input('Qual é seu nome: '))
pessoa['idade']=date.today().year-int(input('Qual seu ano de nacimento: '))
pessoa['CTPS']=int(input('Carteira de Trabalho (0 NÃO TEM): '))

if pessoa['CTPS']!= 0 :
    pessoa['contratação']=int(input('Ano de contratação: '))
    pessoa['salario']=float(input('Salario: '))
    pessoa['aposentadoria']= (35-(date.today().year-pessoa['contratação']))+pessoa['idade']
#print(pessoa)
print('-=-'*10)
for k,v in pessoa.items():
    print(f'- {k} da pessoa é : {v}')
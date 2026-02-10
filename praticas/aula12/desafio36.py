
print('Quer comprar uma casa?')

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o valor do seu salario? '))
meses = int(input('Em quantos anos você quer pagar? '))*12

mensalidade = float(casa/meses)
maximo = (salario*0.3)

'''print(maximo)
print(f'{mensalidade:.2f}')'''

if mensalidade<= maximo:
    print('Seu emprestimo foi aprovado')
else:
    print('Seu emprestimo não foi aprovado')
nome = ''
idade = 0
sexo = ''
mair18 = 0
homens = 0
mulheres = 0
menu = 0
print('Cadastro de pessoas:')
while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo:')).upper().strip()
    if idade >= 18:
        mair18 +=1
    if sexo == "M":
        homens +=1
    else:
        if idade < 20:
            mulheres +=1

    menu = int(input('Quer cadastrar mais uma pessoa: SIM(1) NÂO(2)')) 

    if menu == 2:
        break

print(f'A {mair18} pessoas tem mais de 18 anos')
print(f'A {homens} homes')
print(f'A {mulheres} mulheres menores de 20')
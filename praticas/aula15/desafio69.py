nome = ''
idade = 0
sexo = ''
mair18 = 0
homens = 0
mulheres = 0
menu = 'S'
print('-=-'*15)
print('Cadastro de pessoas:')

while True:
    if menu =='S':
        print('-=-'*15)
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        while sexo != 'F' and sexo != 'M':
            sexo = str(input('Sexo: F/M ')).upper().strip()
        
        if idade >= 18:
            mair18 +=1
        if sexo == "M":
            homens +=1
        else:
            if idade < 20:
                mulheres +=1
        print('-=-'*15)
    sexo = ''
    
    menu = str(input('Quer cadastrar mais uma pessoa: S/N ')).upper().strip()
       
    if menu == "N":
        break

print('-=-'*15)
print(f'A {mair18} pessoas tem mais de 18 anos')
print(f'A {homens} homes')
print(f'A {mulheres} mulheres menores de 20')
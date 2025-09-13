from time import sleep

n1 = 0
maior = 0
menor = 0
media = 0
menu = 1
soma = 0
c = 0
while menu == 1:
    n1=int(input('Digite um numero: '))
    soma +=n1
    if c ==0:
        maior = n1
        menor = n1
    if maior < n1:
        maior = n1
    if menor > n1:
        menor = n1
    c+=1
    menu = int(input('Quer continuar: (1)SIM (2)NÃO '))
print('Calculando ...')
sleep(1)
print('-=-'*25)
print('A média entre os {} valores digitados é : {:.2f}'.format(c,soma/c))
print(f'o maior numero {maior} ')
print(f'o menor numero foi {menor}')
print('-=-'*25)

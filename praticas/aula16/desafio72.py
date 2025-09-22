numeros = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
           'Onze','Doze','Treze','Catorze','Quinze','Dezesei','Dezesete','Dezoito',
           'Dezenove','Vinte')
m='S'
while True:
    if m =='S':
        escolha = int(input('Digite um numero de 0 a 20: ')) 
        if escolha in range (0,21):
            print(F'Você digitou: {numeros[escolha]}')
        else:
            print('NUMERO INVALIDO')
    elif m =='N':
        break
    else:
        print('Letra invalida')
    m = str(input('Quer continuar: S/N ')).upper()
 
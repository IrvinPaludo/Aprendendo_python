
def leiaInt(numero):
    global n
    n = numero
    while True:
        valor = input(n)
        if valor.isnumeric():
         return  int(valor)
            
        
        else:
            print('\033[31mERRO! Digite um numero valido\033[m')
            



n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero: {n}')

def aumentar(numero=0,p=0):
    resultado = (numero*(p/100))+numero
    return resultado

def reduzir(numero=0,p=0):
    resultado = numero-(numero*(p/100))
    return resultado

def dobro(numero=0):
    resultado = numero * 2
    return resultado

def metade(numero=0):
    resultado = numero / 2
    return resultado

def moeda(valor=0, moeda= 'R$'):
    return f'{moeda}{valor:.2}'.replace('.',',')


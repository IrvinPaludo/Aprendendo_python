
def aumentar(numero=0,p=0,f=True):
    resultado = (numero*(p/100))+numero
    if f:
        resultado= moeda(resultado)
    return resultado

def reduzir(numero=0,p=0,f=True):
    resul = numero-(numero*(p/100))
    if f:
        resul = moeda(resul)
    return resul

def dobro(numero=0,f=True):
    resultado = numero * 2
    if f:
        resultado = moeda(resultado)
    return resultado

def metade(numero=0,f=True):
    resultado = numero / 2
    if f:
        resultado = moeda(resultado)
    return resultado

def moeda(valor=0.00, moeda= 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')


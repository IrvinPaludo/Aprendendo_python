'''def lin():
    print('-'*30)

lin()
print('irvin')
lin()

def mensagem(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)

mensagem('irvin')'''

def soma(a,b):        
    s = a + b
    print(s)

soma(1,2)
soma(3,3)

def contador(*num):     #empacotar parametro
    c = len(num)
    print(c)


contador(5,4,8,1)
valor = [6,5,4,3,2,1]

def dobra(lst):
    pos= 0 
    while pos < len(lst):
        lst[pos] *= 2
        pos+=1
    print(lst)
dobra(valor)
print(valor)
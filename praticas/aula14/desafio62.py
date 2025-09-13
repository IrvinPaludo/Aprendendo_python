from time import sleep
print('='*30)
print('     10 TERMOS DE UM PA')
print('='*30)
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite a razão: '))
c = 0
c1 = 0
m = 9
q = 9
mais = 0
while m != 0:
    while c1 < m :
        print(f'{n1+(c)*n2}', end=" -> " )
        c+=1
        c1+=1
    print('')
    #print('\n')
    print("="*30)
    #m = int(input('\nQuer continuar? Sim(1) Não(2)'))
    #if m ==1:
    m = int(input('quantos numeros voê quer a mais? '))
    c1=0
    
   
''' print(c1 < q)'''
print('FIM')

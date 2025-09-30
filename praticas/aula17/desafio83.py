list=[]
val = True
list.append(input('Digite uma expreção matematica: '))

if list.count('(') == list.count(')'):
    val= True
else:
    val = False

if val == True :
    print('Expreção valida')
else:
    print('Expreção invalida')
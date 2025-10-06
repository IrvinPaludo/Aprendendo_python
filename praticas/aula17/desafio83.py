list=[]
val = True
list=str(input('Digite uma expreção matematica: '))


#posui um erro se os '()' fosem fechados ')'antes de ser abertos e abertos '('  
#depois constava valido
'''if list.count('(') == list.count(')'):
    val= True
else:
    val = False

if val == True :
    print('Expreção valida')
else:
    print('Expreção invalida')'''

pilha=[]
for sim in list:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break

print(len(pilha))
if len(pilha) == 0 :
    print('Expreção valida')
else:
    print('Expreção invalida')


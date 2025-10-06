num = [31,2,13,4] #lista 
num[2] = 5 #lista podem ser alteradas
num.append(7) #Adisona no final da lista
num.sort(reverse=True) #Aruma a lista em ordm cresente ou (reverse=True) decrecente
num.insert(2,0) #Insere um valor na lista em um local 
num.pop(2) #remove um valor do indise(x)
num.index(2) #mostra onde ocore o primeira aparição de um valor
print('\n')
for n in num:
    print(n,end=' ')
print('\n')
for c,v in enumerate(num):#para cada valor {v} coloca um indice{c}
    print(f'na posição {c} encontrase o valor {v}')
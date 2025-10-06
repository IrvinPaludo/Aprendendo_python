
#dados = ['pedro',25]
#pessoas =[]
#pessoas.append(dados[:])

#pessoas =[['pedro',25],['maria',18],['joao',20]]
#print(pessoas)
#print(pessoas[0][0])
#print(pessoas[1])

test = list()
test.append('irvin')
test.append(26)

galera=[]
galera.append(test[:])#se não colocar o : o valor da referncia gravado muda se for atua lizado depois,
#com : é feito um copia dos dados da referencia 
print(galera)
test[0]='Maria'
test[1]=18
galera.append(test[:])
print(galera)

print('-=-'*20)
pessoas = [['João',17],['Jáco',50],['Antonia',35],['Ana',17]]
#print(pessoas)
#print('-=-'*20)
for a in pessoas:   
    if a[1] >= 18:
        print(f'{a[0]} é maior de idade.')
    else:
        print(f'{a[0]} é menor de idade ')

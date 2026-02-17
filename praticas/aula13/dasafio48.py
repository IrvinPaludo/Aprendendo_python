soma = 0 #iniciando a variavel
cont = 0
for c in  range(1,501,2): #loop
     if c % 3 == 0: #condicao de soma

        soma += c #soma
        cont += 1 

print(soma) #imprime o resultado
print(cont)

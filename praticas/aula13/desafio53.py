

frase = str(input('Digite uma frase: ')).strip().upper().split() #pega a frase, tira os espaços e coloca tudo em maiusculo

frase = ''.join(frase) #junta tudo em uma unica string, sem espaços

print(frase) 
print(len(frase))
r = False #variavel resposta

for c in range(0,len(frase)): #percorre a string do começo ao fim
    
    if frase[c] == frase[len(frase)-1-c]: #compara a letra da posição c com a letra da posição inversa
        r = True 
        
    else:
        r = False
        break
        
if r == True:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
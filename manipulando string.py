frase = 'curso em video de python'

print(frase)

#fatiamento

#printar uma letra
print(frase[9])

#printar de uma letra até o fim
print(frase[9:])

#printar de uma letra até o fim pulando de 2 em 2
print(frase[9::2])

#conta quantos caracteris tem
print(len(frase))

#conta quantas letras(x) tem na frase
print(frase.count('o'))

#conta quantas letras(x) tem na frase dentro de um parte
print(frase.count('o',0,13))

#Achar 'x' dentro da frase
print(frase.find('deo'))

#altera momentaneamente a frase
print(frase.replace('python','Androide'))
print(frase)

#colocar tudo em maiusculo
print(frase.upper())

#colocar tudo em minusculo
print(frase.lower())

#só a letra inicial da frase fica maiuscula
print(frase.capitalize())

#todas letras inicias da frase fica maiuscula
print(frase.title())


frase2 = '   aprenda python  '
print(frase2)

#remove espaços inuteis
print(frase2.strip())

#remove espaços inuteis so na direita
print(frase2.rstrip())

#remove espaços inuteis so na direita
print(frase2.lstrip())

#dividindo a frase
dividida = frase.split()
print(dividida[0][2])

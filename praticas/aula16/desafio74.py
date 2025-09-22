
from random import randint

numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print('Os numeros sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ',end='')
print(f'\nO menor numero foi: {min(numeros)}')
print(f'O maior numero foi: {max(numeros)}')
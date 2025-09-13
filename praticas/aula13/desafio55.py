
pe = 0
pemais = 0
pemenos = 0

for c in range(1,6):
    pe = float(input(f'digite o peso da pesoa {c}: '))
    if c == 1:
        pemais = pe
        pemenos = pe
    else:
        if pe > pemais :
            pemais = pe
        elif pe < pemenos:
            pemenos = pe

print(f'o maior peso foi {pemais}')
print(f'o menor peso foi {pemenos}')
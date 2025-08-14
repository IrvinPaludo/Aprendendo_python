
largura = float(input('Largura da parede:'))
altura = float(input('Altura da parde: '))
area = largura * altura

print('Sua parede tem a dimenção de {}x{} e sua área é de {:.2f}m²'.format(largura,altura,area))

tinta = area/ 2

print('Você vai precisar de {:.2f}l de tinta'.format(tinta))


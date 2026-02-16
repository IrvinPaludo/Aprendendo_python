#from colorama import Fore, Back

volocidade = float(input('qual é a velocidade do seu carro?'))

if volocidade > 80:
    multa = (volocidade - 80) * 7
    print('\033[0;31;45m você esta acima do lumite 80Km/h \033[m')
    print('\033[0;31;45m você tomou uma multa no valor R${:.2f}\033[m '.format(multa))

print('Boa viagem! tome cuidado ')
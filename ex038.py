num = int(input('Digite a distancia da sua viagem em km :'))
if num <=200:
    print('A sua viagem custara {} reais'.format(num * 0.50))
else:
    print('A sua vaigem custara {} reais '.format(num * 0.45))
carro = int(input('Digite a velocidade do carro: '))
if carro == 80 :
    print('Voce esta andando na velocidade correta ')
else:

    print('Voce esta andando acima do limite, voce levara uma multa de {} reais '.format((carro - 80) * 7))


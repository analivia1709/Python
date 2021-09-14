altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
tinta = (1 * area) / 2
print ('Para a area de {} metros, será necessario {:.1f} de tinta'.format(area, tinta) )
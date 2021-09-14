import math
angulo = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(angulo))
cos =  math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O valor do seno é {:.2f} o valor do coseno é {:.2f} o valor da taangente é {:.2f}'.format(seno, cos, tan))

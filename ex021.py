import math
num = float(input('Digite o valor do cateto oposto: '))
num2 = float(input('Digite o valor do cateto adjacente:'))
#hi = (num ** 2 + num2 **2) ** (1/2)
hi= math.hypot(num, num2)
print('A hipotenusa vai medir {:.1f}'.format(hi))